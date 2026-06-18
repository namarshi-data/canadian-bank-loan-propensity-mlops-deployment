FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r /app/requirements.txt

COPY src /app/src
COPY flask_app /app/flask_app

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "flask_app.app:app"]
