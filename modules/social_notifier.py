import os
import requests
from slack_sdk.webhook import WebhookClient
import tweepy

class SocialNotifier:
    def __init__(self):
        # Load environment variables
        self.discord_url = os.environ.get("DISCORD_WEBHOOK_URL")
        self.slack_url = os.environ.get("SLACK_WEBHOOK_URL")
        self.telegram_token = os.environ.get("TELEGRAM_BOT_TOKEN")
        self.telegram_chat_id = os.environ.get("TELEGRAM_CHAT_ID")
        
        # Initialize X (Twitter) Client if keys are present
        try:
            self.x_client = tweepy.Client(
                consumer_key=os.environ.get("X_API_KEY"),
                consumer_secret=os.environ.get("X_API_SECRET"),
                access_token=os.environ.get("X_ACCESS_TOKEN"),
                access_token_secret=os.environ.get("X_ACCESS_SECRET")
            )
        except Exception:
            self.x_client = None

    def post_to_discord(self, message):
        """Broadcasts a payload to a Discord channel via Webhook."""
        if self.discord_url:
            requests.post(self.discord_url, json={"content": message})
            print("[*] Posted to Discord.")

    def post_to_slack(self, message):
        """Broadcasts a payload to a Slack workspace."""
        if self.slack_url:
            webhook = WebhookClient(self.slack_url)
            webhook.send(text=message)
            print("[*] Posted to Slack.")

    def post_to_telegram(self, message):
        """Sends a message to a specific Telegram Chat/Channel."""
        if self.telegram_token and self.telegram_chat_id:
            url = f"https://api.telegram.org/bot{self.telegram_token}/sendMessage"
            payload = {"chat_id": self.telegram_chat_id, "text": message, "parse_mode": "Markdown"}
            requests.post(url, json=payload)
            print("[*] Posted to Telegram.")

    def post_to_x(self, message):
        """Publishes a Tweet via the X API."""
        if self.x_client:
            # X limits character count, ensure the message is truncated if necessary
            tweet = message[:277] + "..." if len(message) > 280 else message
            self.x_client.create_tweet(text=tweet)
            print("[*] Posted to X.")

    def broadcast_everywhere(self, message):
        """Triggers the bot to post the payload across all connected platforms simultaneously."""
        print("\n[*] Initializing multi-platform broadcast...")
        self.post_to_discord(message)
        self.post_to_slack(message)
        self.post_to_telegram(message)
        self.post_to_x(message)
        print("[*] Broadcast complete.")
