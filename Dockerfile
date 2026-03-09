FROM python:3.11-slim

WORKDIR /app

COPY sample.py .

CMD ["python", "sample.py"]
