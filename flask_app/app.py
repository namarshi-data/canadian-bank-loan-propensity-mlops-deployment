"""Flask API for bank loan propensity scoring."""

from __future__ import annotations

from flask import Flask, jsonify, request

from src.predict import predict_customer

app = Flask(__name__)


@app.get("/")
def home():
    """Health endpoint."""
    return jsonify(
        {
            "service": "Bank Loan Propensity Prediction API",
            "status": "running",
            "version": "2.0.0",
        }
    )


@app.post("/predict")
def predict():
    """Return a customer-level loan propensity score."""
    customer_data = request.get_json(silent=True)

    if not customer_data:
        return jsonify({"success": False, "error": "Request body must be valid JSON."}), 400

    try:
        result = predict_customer(customer_data)
        return jsonify({"success": True, "result": result})
    except Exception as exc:  # Flask returns the validation message to API users.
        return jsonify({"success": False, "error": str(exc)}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
