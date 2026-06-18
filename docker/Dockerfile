FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY src/ src/
COPY flask_app/ flask_app/

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "flask_app.app:app"]
