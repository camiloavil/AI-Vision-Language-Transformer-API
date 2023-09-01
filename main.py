from src.model import model_ask
from fastapi import FastAPI, UploadFile
from PIL import Image
import io
app = FastAPI()



@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/ask")
def ask(text: str, image: UploadFile):
    content = image.file.read()
    image = Image.open(io.BytesIO(content))
    # image = Image.open(image.file)
    
    result = model_ask(text= text, image= image)
    return {"answer": result}
    
