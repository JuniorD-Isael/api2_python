# import io
from fastapi import FastAPI, UploadFile, File
import pytesseract
import cv2
import numpy as np
# from PIL import Image

app = FastAPI()

@app.post('/process-image')
async def process_image(file: UploadFile = File(...)):
    contents = await file.read()

    nparr = np.frombuffer(contents, np.uint8)

    # image = Image.open(io.BytesIO(contents))
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)


    # gray_image = image.convert('L')
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, thresh_image = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY)

    # brand_name = pytesseract.image_to_string(gray_image)
    brand_name = pytesseract.image_to_string(thresh_image)

    print(f"Texto detectado: {brand_name.strip()}")

    return {'brandName': brand_name.strip()}
