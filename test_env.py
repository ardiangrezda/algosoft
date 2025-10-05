import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Print some environment variables to verify they loaded correctly
print("Environment Variables Test:")
print("-" * 30)
print(f"SECRET_KEY exists: {'SECRET_KEY' in os.environ}")
print(f"EMAIL_HOST_USER exists: {'EMAIL_HOST_USER' in os.environ}")
print(f"EMAIL_HOST_PASSWORD exists: {'EMAIL_HOST_PASSWORD' in os.environ}")
print("-" * 30)
print("Test completed!")