from fastapi import FastAPI, UploadFile, File
from PIL import Image
import io, torch
from transformers import AutoImageProcessor, AutoModelForImageClassification

app = FastAPI()

processor = AutoImageProcessor.from_pretrained("ashaduzzaman/vit-finetuned-food101")
model = AutoModelForImageClassification.from_pretrained("ashaduzzaman/vit-finetuned-food101")
model.eval()

@app.post("/predict_food")
async def predict_food(file: UploadFile = File(...)):
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    inputs = processor(images=image, return_tensors="pt")
    with torch.no_grad():
        logits = model(**inputs).logits
    idx = logits.argmax(-1).item()
    label = model.config.id2label[idx]
    return {"food_label": label}
