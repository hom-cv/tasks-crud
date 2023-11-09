FROM python:3.8-slim

WORKDIR /code

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY app/ ./app

COPY . .

CMD ["python", "app.py"]

EXPOSE 5000