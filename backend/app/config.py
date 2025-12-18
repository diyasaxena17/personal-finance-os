# backend/app/config.py
from dotenv import load_dotenv
import os
# Load environment variables from .env file
load_dotenv()

# Application configuration
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
