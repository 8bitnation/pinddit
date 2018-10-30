import os
from dotenv import load_dotenv
load_dotenv(verbose=True)

# DISCORD #
# The token for the discord bot
TOKEN = os.getenv("DISCORD_PINDDIT_TOKEN")
# The Client ID for the discord client
CLIENT_ID = int(os.getenv("DISCORD_PINDDIT_CLIENT_ID"))
# Guild ID
GUILD_ID = int(os.getenv("GUILD_ID"))

# REDDIT #
# Reddit Client ID
REDDIT_ID=os.getenv("PINDDIT_REDDIT_ID")
# Reddit Secret
REDDIT_SECRET=os.getenv("PINDDIT_REDDIT_SECRET")
# Reddit user agent
REDDIT_USER_AGENT="pinddit bot for 8bitnation:v1.0.0 (by /u/kpax)"
# Reddit username
REDDIT_USERNAME=os.getenv("REDDIT_USERNAME")
# Reddit password
REDDIT_PASSWORD=os.getenv("REDDIT_PASSWORD")
# Subreddit to crosspost/autopost to
SUB_REDDIT=os.getenv("SUB_REDDIT")

print("Settings loaded!")