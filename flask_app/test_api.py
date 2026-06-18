"""Local smoke test for the Flask API.

Run after starting the API with:
    python flask_app/app.py
"""

from __future__ import annotations

import json
from pathlib import Path

import requests


payload = json.loads(Path("flask_app/sample_request.json").read_text())

response = requests.post(
    "http://localhost:5000/predict",
    json=payload,
    timeout=10,
)

print(response.status_code)
print(response.json())
