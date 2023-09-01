from transformers import ViltProcessor, ViltForQuestionAnswering
from PIL import Image
# import requests

# url = "http://images.cocodataset.org/val2017/000000039769.jpg"
# image = Image.open(requests.get(url, stream=True).raw)
# text = "How many cats are there?"
# text = "what kind of animal is this?"
# text = "what are doing in this picture?"
# text = "tell me the principal color of the picture"
# text = "describe the picture"

processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
model = ViltForQuestionAnswering.from_pretrained("dandelin/vilt-b32-finetuned-vqa")

def model_ask(text: str, image: Image):
    # prepare inputs
    encoding = processor(image, text, return_tensors="pt")
    # forward pass
    outputs = model(**encoding)
    logits = outputs.logits
    idx = logits.argmax(-1).item()
    # print("Predicted answer:", model.config.id2label[idx])
    return model.config.id2label[idx]
