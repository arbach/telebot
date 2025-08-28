# Telegram Bot

A Telegram bot built with Telethon library.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Get your Telegram API credentials:
   - Go to https://my.telegram.org
   - Log in with your phone number
   - Go to "API Development"
   - Create a new application
   - Copy your `api_id` and `api_hash`

3. Set up your configuration:

   **Option 1: Environment Variables**
   ```bash
   export TELEGRAM_API_ID=your_api_id_here
   export TELEGRAM_API_HASH=your_api_hash_here
   export TELEGRAM_SESSION_NAME=your_session_name
   export TELEGRAM_DEFAULT_RECIPIENT=username_or_chat_id
   ```

   **Option 2: .env file**
   Create a `.env` file in the project root:
   ```
   TELEGRAM_API_ID=your_api_id_here
   TELEGRAM_API_HASH=your_api_hash_here
   TELEGRAM_SESSION_NAME=your_session_name
   TELEGRAM_DEFAULT_RECIPIENT=username_or_chat_id
   TELEGRAM_DEFAULT_FILE_PATH=/path/to/your/file
   ```

4. Run the bot:
```bash
python client.py
```

## Security Notes

- Never commit your actual API credentials to version control
- The `.env` file is already in `.gitignore` to prevent accidental commits
- Use environment variables in production environments
- Keep your `api_hash` secret and secure

## Configuration Options

All configuration options can be found in `config.py` and can be overridden using environment variables:

- `TELEGRAM_API_ID`: Your Telegram API ID
- `TELEGRAM_API_HASH`: Your Telegram API hash
- `TELEGRAM_SESSION_NAME`: Session name for the client
- `TELEGRAM_DEFAULT_RECIPIENT`: Default recipient for messages
- `TELEGRAM_DEFAULT_FILE_PATH`: Default file path for file operations
