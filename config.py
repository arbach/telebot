import os
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

# Telegram API credentials
# Get your api_id and api_hash from https://my.telegram.org, under API Development
API_ID = int(os.getenv('TELEGRAM_API_ID', '12345'))
API_HASH = os.getenv('TELEGRAM_API_HASH', '0123456789abcdef0123456789abcdef')

# Session configuration
SESSION_NAME = os.getenv('TELEGRAM_SESSION_NAME', 'session_name')

# Default recipient for messages
DEFAULT_RECIPIENT = os.getenv('TELEGRAM_DEFAULT_RECIPIENT', 'username')

# File paths
DEFAULT_FILE_PATH = os.getenv('TELEGRAM_DEFAULT_FILE_PATH', '/home/myself/Pictures/holidays.jpg')

# Validation
if API_ID == 12345 or API_HASH == '0123456789abcdef0123456789abcdef':
    print("Warning: Using default API credentials. Please set your actual credentials in environment variables or .env file.")
    print("Set TELEGRAM_API_ID and TELEGRAM_API_HASH environment variables.")
