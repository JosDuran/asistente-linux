FROM python:3.10-slim

WORKDIR /app
COPY . /app

RUN pip install fastapi uvicorn sentence-transformers numpy

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
