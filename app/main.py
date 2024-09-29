import io
from fastapi import FastAPI, UploadFile, File
import pytesseract
from PIL import Image

app = FastAPI()

@app.post('/process-image')
async def process_image(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))

    gray_image = image.convert('L')


    brand_name = pytesseract.image_to_string(gray_image)

    print(f"Texto detectado: {brand_name.strip()}")

    return {'brandName': brand_name.strip()}
