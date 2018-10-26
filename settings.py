import os
from dotenv import load_dotenv
load_dotenv(verbose=True)

# The token for the discord bot
TOKEN = os.getenv("DISCORD_PINDDIT_TOKEN")
# The Client ID for the discord client
CLIENT_ID = int(os.getenv("DISCORD_PINDDIT_CLIENT_ID"))
# Guild ID
GUILD_ID = int(os.getenv("GUILD_ID"))