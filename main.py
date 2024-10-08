from model_hf import model_pipeline

from fastapi import FastAPI, UploadFile
import io
from PIL import Image

app = FastAPI()


@app.post("/ask")
def ask(text: str, image: UploadFile):
    content = image.file.read()
    image = Image.open(io.BytesIO(content))
    result = model_pipeline(text, image)
    return {"answer": result}

