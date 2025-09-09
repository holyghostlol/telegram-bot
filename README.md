# Telegram Bot for tccUSDT Staking Platform

A Telegram bot that handles referral links and WebApp integration for the tccUSDT staking platform.

## Features

- **Referral System**: Handles referral codes passed through `/start` command
- **WebApp Integration**: Opens the staking platform directly in Telegram
- **User Management**: Tracks user interactions and referral usage
- **Secure Configuration**: Uses environment variables for sensitive data

## Setup

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd telegram-bot
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**:
   - Copy `.env.example` to `.env`
   - Fill in your actual bot token and other configuration values
   ```bash
   cp .env.example .env
   ```

4. **Edit the `.env` file**:
   ```
   BOT_TOKEN=your_actual_bot_token_here
   WEBAPP_URL=https://staking-five-pi.vercel.app
   ```

5. **Run the bot**:
   ```bash
   python telegram_bot.py
   ```

## Usage

- Send `/start` to interact with the bot
- Send `/start <referral_code>` to use a referral link
- The bot will provide a button to open the staking WebApp

## Security

- Never commit your `.env` file
- Keep your bot token secure
- The `.env.example` file shows the required environment variables

## Deployment

This bot can be deployed on various platforms like Heroku, Railway, or any VPS that supports Python applications.

## License

This project is for educational purposes.
