import os
import json
import requests
from openai import OpenAI

API_KEY = os.getenv("UPSTAGE_API_KEY")

if not API_KEY:
    raise ValueError("Missing UPSTAGE_API_KEY environment variable.")

HEADERS = {"Authorization": f"Bearer {API_KEY}"}
OCR_URL = "https://api.upstage.ai/v1/document-digitization"
SOLAR_CLIENT = OpenAI(api_key=API_KEY, base_url="https://api.upstage.ai/v1")

def ocr_image(file_bytes):
    files = {"document": ("receipt.jpg", file_bytes)}
    data = {"model": "ocr"}
    response = requests.post(OCR_URL, headers=HEADERS, files=files, data=data)
    response.raise_for_status()
    return response.json()

def extract_receipt_info_with_solar(context_text):
    prompt = (
        "You are a receipt parser AI.\n"
        "Extract the following fields from the receipt OCR text:\n"
        "- restaurant_name\n"
        "- address\n"
        "- date (of visit or receipt)\n"
        "Return a JSON object with keys: restaurant_name, address, date.\n\n"
        f"Receipt OCR Text:\n{context_text}\n\nExtracted JSON:"
    )

    response = SOLAR_CLIENT.chat.completions.create(
        model="solar-pro",
        messages=[{"role": "user", "content": prompt}],
        stream=False
    )

    content = response.choices[0].message.content.strip()
    if content.startswith("```json"): content = content[len("```json"):].strip()
    if content.endswith("```"): content = content[:-3].strip()

    try:
        return json.loads(content)
    except json.JSONDecodeError:
        return {"error": "Could not parse receipt info"}
