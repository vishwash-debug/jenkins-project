FROM python:3.11-slim

WORKDIR /app

COPY sample.py .

# (Optional but safe)
RUN pip install flask

EXPOSE 8080

CMD ["python", "sample.py"]
