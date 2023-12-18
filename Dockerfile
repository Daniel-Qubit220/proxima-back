# Use an official Python runtime as the base image
FROM --platform=linux/amd64 python:3.8

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r ./app/requirements.txt

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
