FROM python:3.11-slim

WORKDIR /app

# Kopiraj dependencies iz antonio/
COPY antonio/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopiraj ostatak koda iz antonio/
COPY antonio/ .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]