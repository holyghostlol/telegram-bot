#!/usr/bin/env python3
"""
Telegram Bot for tccUSDT Staking Platform
Handles referral links and WebApp integration
"""

import telebot
from telebot import types
import os
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Bot configuration
BOT_TOKEN = os.getenv('BOT_TOKEN')
WEBAPP_URL = os.getenv('WEBAPP_URL', "https://staking-five-pi.vercel.app")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN environment variable is required")

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize bot
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
    """Handle /start command with optional referral code"""
    try:
        # Get the referral code from the start parameter
        referral_code = None
        if len(message.text.split()) > 1:
            referral_code = message.text.split()[1]
        
        logger.info(f"User {message.from_user.id} started bot with referral code: {referral_code}")
        
        # Create inline keyboard with WebApp button
        keyboard = types.InlineKeyboardMarkup()
        
        if referral_code:
            # If there's a referral code, create button with referral link
            webapp_button = types.InlineKeyboardButton(
                text="🚀 Open Staking App (You were invited!)",
                web_app=types.WebAppInfo(url=f"{WEBAPP_URL}?ref={referral_code}")
            )
            
            keyboard.add(webapp_button)
            
            # Send welcome message with referral info
            welcome_text = f"""
🎉 Welcome to tccUSDT Staking!

You've been invited by someone to join our staking platform!

💰 Earn up to 2.6% daily returns
🤝 Get referral rewards
🔒 Secure and reliable

Click the button below to start staking with your referral bonus!

Referral Code: <code>{referral_code}</code>
            """
            
        else:
            # No referral code, regular welcome
            webapp_button = types.InlineKeyboardButton(
                text="🚀 Open Staking App",
                web_app=types.WebAppInfo(url=WEBAPP_URL)
            )
            
            keyboard.add(webapp_button)
            
            welcome_text = f"""
🎉 Welcome to tccUSDT Staking!

💰 Earn up to 2.6% daily returns
🤝 Get referral rewards  
🔒 Secure and reliable

Click the button below to start staking!
            """
        
        # Send image with caption
        try:
            # You can replace this URL with your actual image URL
            image_url = "https://i.ibb.co/s9DmmLZP/photo-2025-09-02-20-30-24.jpg"  # Your logo image
            
            bot.send_photo(
                message.chat.id,
                photo=image_url,
                caption=welcome_text,
                reply_markup=keyboard,
                parse_mode='HTML'
            )
        except Exception as e:
            logger.warning(f"Could not send image, sending text only: {e}")
            # Fallback to text message if image fails
            bot.send_message(
                message.chat.id,
                welcome_text,
                reply_markup=keyboard,
                parse_mode='HTML'
            )
        
    except Exception as e:
        logger.error(f"Error handling start command: {e}")
        bot.send_message(
            message.chat.id,
            "❌ Sorry, something went wrong. Please try again later."
        )

@bot.message_handler(commands=['help'])
def handle_help(message):
    """Handle /help command"""
    help_text = """
🤖 tccUSDT Staking Bot Commands:

/start - Open the staking app
/help - Show this help message
/info - Get platform information

💡 To invite friends, share your referral link from the app!
    """
    
    keyboard = types.InlineKeyboardMarkup()
    webapp_button = types.InlineKeyboardButton(
        text="🚀 Open Staking App",
        web_app=types.WebAppInfo(url=WEBAPP_URL)
    )
    keyboard.add(webapp_button)
    
    bot.send_message(
        message.chat.id,
        help_text,
        reply_markup=keyboard
    )

@bot.message_handler(commands=['info'])
def handle_info(message):
    """Handle /info command"""
    info_text = """
📊 tccUSDT Staking Platform Info:

💰 Daily Returns: Up to 2.6%
🔒 Security: Industry-standard protection
🤝 Referral System: 5-level commission structure
⏰ Claim Frequency: Every 24 hours
💎 Token: tccUSDT (0.65 USDT rate)

Start staking today and earn passive income!
    """
    
    keyboard = types.InlineKeyboardMarkup()
    webapp_button = types.InlineKeyboardButton(
        text="🚀 Start Staking Now",
        web_app=types.WebAppInfo(url=WEBAPP_URL)
    )
    keyboard.add(webapp_button)
    
    bot.send_message(
        message.chat.id,
        info_text,
        reply_markup=keyboard
    )

@bot.message_handler(func=lambda message: True)
def handle_other_messages(message):
    """Handle all other messages"""
    keyboard = types.InlineKeyboardMarkup()
    webapp_button = types.InlineKeyboardButton(
        text="🚀 Open Staking App",
        web_app=types.WebAppInfo(url=WEBAPP_URL)
    )
    keyboard.add(webapp_button)
    
    bot.send_message(
        message.chat.id,
        "👋 Hi! Use the button below to access the staking app, or type /help for commands:",
        reply_markup=keyboard
    )

def main():
    """Main function to start the bot"""
    try:
        logger.info("Starting tccUSDT Staking Bot...")
        logger.info(f"WebApp URL: {WEBAPP_URL}")
        
        # Get bot info
        bot_info = bot.get_me()
        logger.info(f"Bot @{bot_info.username} is running!")
        
        # Start polling
        bot.polling(none_stop=True, interval=0, timeout=20)
        
    except Exception as e:
        logger.error(f"Error starting bot: {e}")
        raise

if __name__ == "__main__":
    main()
