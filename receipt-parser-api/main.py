from fastapi import FastAPI, File, UploadFile
from receipt_parser import extract_receipt_info_with_solar, ocr_image

app = FastAPI()

@app.post("/parse_receipt")
async def parse_receipt(file: UploadFile = File(...)):
    file_bytes = await file.read()
    ocr_result = ocr_image(file_bytes)
    text = ocr_result.get("text", "").strip()
    result = extract_receipt_info_with_solar(text)
    return result
