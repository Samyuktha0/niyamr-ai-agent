import os
import json
import re
from openai import OpenAI
from dotenv import load_dotenv

# 1. Load the API Key and Configure Client for OpenRouter
load_dotenv()
openrouter_api_key = os.getenv("OPENROUTER_API_KEY")

try:
    if not openrouter_api_key:
        raise ValueError("OPENROUTER_API_KEY not found in .env file.")

    # Configure the client to use the OpenRouter base URL
    client = OpenAI(
        api_key=openrouter_api_key,
        base_url="https://openrouter.ai/api/v1", # OpenRouter endpoint
        # The HTTP-Referer header is optional but recommended by OpenRouter
        default_headers={"HTTP-Referer": "https://your-app-name.com"} 
    )
except Exception as e:
    print(f"❌ Error initializing OpenRouter client: {e}")
    print("Please ensure OPENROUTER_API_KEY is set in your .env file.")
    exit()

# 2. Load the Text Extracted from Task 1
try:
    # This file should exist from your successful 'python extractor.py' run
    with open("extracted_act_text.txt", "r", encoding="utf-8") as f:
        act_text = f.read()
except FileNotFoundError:
    print("❌ Error: 'extracted_act_text.txt' not found.")
    print("Please run 'python extractor.py' first.")
    exit()

# --- The Super-Prompt (Tasks 2, 3, 4 consolidated) ---
SYSTEM_PROMPT = """
You are a Legislative AI Analyst. Your task is to analyze the provided legal text for the 'Universal Credit Act 2025' and return a single, comprehensive JSON object that STRICTLY adheres to the requested format for all three tasks. DO NOT include any text, notes, or explanations outside of the final JSON object.

--- REQUIRED JSON STRUCTURE ---
{
  "summary": [
    "Purpose of the Act...",
    "Key definitions...",
    "Eligibility criteria...",
    "Obligations...",
    "Enforcement elements..."
  ],
  "sections": {
    "definitions": "...",
    "obligations": "...",
    "responsibilities": "...",
    "eligibility": "...",
    "payments": "...",
    "penalties": "...",
    "record_keeping": "..."
  },
  "rule_checks": [
    {
      "rule": "Act must define key terms",
      "status": "pass" or "fail",
      "evidence": "Section/Clause where evidence is found",
      "confidence": 0-100
    },
    {
      "rule": "Act must specify eligibility criteria",
      "status": "pass" or "fail",
      "evidence": "Section/Clause where evidence is found",
      "confidence": 0-100
    },
    {
      "rule": "Act must specify responsibilities of the administering authority",
      "status": "pass" or "fail",
      "evidence": "Section/Clause where evidence is found",
      "confidence": 0-100
    },
    {
      "rule": "Act must include enforcement or penalties",
      "status": "pass" or "fail",
      "evidence": "Section/Clause where evidence is found",
      "confidence": 0-100
    },
    {
      "rule": "Act must include payment calculation or entitlement structure",
      "status": "pass" or "fail",
      "evidence": "Section/Clause where evidence is found",
      "confidence": 0-100
    },
    {
      "rule": "Act must include record-keeping or reporting requirements",
      "status": "pass" or "fail",
      "evidence": "Section/Clause where evidence is found",
      "confidence": 0-100
    }
  ]
}
"""

USER_PROMPT = f"""
Analyze the following document and generate the JSON report according to the required structure:

--- UNIVERSAL CREDIT ACT 2025 TEXT ---
{act_text}
"""

def generate_report(system_content, user_content):
    """Sends the analysis request to the OpenRouter API."""
    print("⏳ Sending analysis request to OpenRouter (using Claude 3 Haiku) for high reliability...")
    
    # NOTE: You can change the model name to any supported OpenRouter model.
    # Claude 3 Haiku is a good, fast choice for structured JSON.
    # Other options: "openai/gpt-4o-mini", "mistralai/mixtral-8x7b-instruct-v0.1"
    response = client.chat.completions.create(
        model="anthropic/claude-3-haiku", 
        max_tokens=4096, 
        temperature=0.0,
        response_format={"type": "json_object"}, # Force JSON output
        messages=[
            {"role": "system", "content": system_content},
            {"role": "user", "content": user_content}
        ]
    )
    
    # The API is forced to return a JSON object, so we can parse it directly
    json_string = response.choices[0].message.content
    return json.loads(json_string)

# --- Execute ---
if __name__ == "__main__":
    try:
        final_report_data = generate_report(SYSTEM_PROMPT, USER_PROMPT)

        # Save the final JSON output (Deliverable 2)
        output_filename = "final_report.json"
        with open(output_filename, "w", encoding="utf-8") as f:
            json.dump(final_report_data, f, indent=4)
        
        print(f"\n✅ SUCCESS! All analysis complete.")
        print(f"Tasks 2, 3, and 4 are complete. Final structured JSON report saved to {output_filename}")
    
    except Exception as e:
        print(f"\n❌ An error occurred during OpenRouter processing.")
        print(f"Error details: {e}")