# backend/app/main.py
from fastapi import FastAPI

# Initialize FastAPI application
app = FastAPI(
    title="Personal Finance OS",
    description="Backend API for tracking and explaining personal finance data",
    version="0.1.0"
)

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "ok"}
