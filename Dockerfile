# FROM python:3.9-slim
FROM python:3.9

WORKDIR /app
COPY requirements.txt .
# RUN apt-get update && apt-get install libgl1 libglib2.0-0 -y
RUN pip install --no-cache-dir --upgrade -r requirements.txt
# COPY . .
# CMD bash -c "while true; do sleep 1; done"
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]