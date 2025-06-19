FROM python:3-slim

WORKDIR /app

COPY main.py /app/main.py

CMD ["python3", "main.py"]
