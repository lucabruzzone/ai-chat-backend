FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONPATH=/app/src

EXPOSE 5500

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "5500", "--reload"]
