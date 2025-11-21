import PyPDF2
import os

def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF file and returns a cleaned, structured string."""
    text = ""
    try:
        # Open the PDF file in binary read mode ('rb')
        with open(pdf_path, 'rb') as file:
            # Create a PDF reader object
            # Note: PyPDF2.PdfReader is used for reading; PdfWriter for writing.
            reader = PyPDF2.PdfReader(file)
            
            # Loop through all pages and extract text
            for i, page in enumerate(reader.pages):
                # Add a marker for new pages to help structure the text
                text += f"\n--- PAGE {i+1} ---\n"
                
                # Extract text content
                page_text = page.extract_text()
                
                # Handle cases where extract_text() returns None or is empty
                if page_text:
                    text += page_text
            
            # Simple cleanup: remove excessive empty lines and collapse multiple spaces 
            # Note: More advanced cleanup (like handling hyphenated words) may be needed 
            # depending on the actual PDF structure.
            clean_text = os.linesep.join([s for s in text.splitlines() if s.strip()])
            
            return clean_text
            
    except FileNotFoundError:
        return f"Error: PDF file not found at {pdf_path}. Please check the filename."
    except Exception as e:
        return f"An error occurred during extraction: {e}"

# --- Execution Block ---
# *CRITICAL:* Ensure your PDF file is named exactly this and is in the same folder.
pdf_file_path = "Universal_Credit_Act_2025.pdf" 
extracted_content = extract_text_from_pdf(pdf_file_path)

if "Error" not in extracted_content:
    # Save the extracted text to a file for review
    output_filename = "extracted_act_text.txt"
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(extracted_content)
        
    print(f"✅ Text extraction complete. Saved to {output_filename}")
    print("This completes Task 1.")
else:
    print(f"❌ Extraction Failed: {extracted_content}")