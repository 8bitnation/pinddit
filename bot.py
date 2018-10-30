import discord
from settings import TOKEN, GUILD_ID
from discord import guild
from pintoreddit import reddit, sub_reddit
import time

client = discord.Client()

text_channel_list = []

@client.event
async def on_ready():
    print(f"Logged in to Discord as {client.user}\n")

@client.event
async def on_message(message):
    print(
        f"#{message.channel}|{message.author.name}({message.author}):{message.content}"
    )
    
    if "!channels" in message.content.lower():
        channel_generator = client.get_all_channels()
        for channel in channel_generator:
            if (channel.name.lower() != 'text channels') and (channel.name.lower() != 'voice channels'):
                text_channel_list.append(channel.name)
        await message.channel.send(text_channel_list)

    if "!pins" in message.content.lower():
        myGuild = client.get_guild(GUILD_ID)
        for textChannel in myGuild.text_channels:
            await message.channel.send('#'+ textChannel.name)
            for pin in await textChannel.pins():
                await message.channel.send('pin: ```' + str(pin) + '```')
                if pin.content:
                    await message.channel.send('content: ```' + pin.content + '```')
                if pin.clean_content:
                    #await message.channel.send('clean_content: ```' + pin.clean_content + '```')
                    #await reddit.subreddit(sub_reddit).submit("{}:{}".format(str.join('Pinddit: ', pin.clean_content), pin.clean_content),selftext="Pinddit{}".format(time.now()))
                    reddit.subreddit(sub_reddit).submit("Pinddit", selftext="{}".format(pin.clean_content))
                    print('Posted!\n')
                for embed in pin.embeds:
                    await message.channel.send('embed: ```' + str(embed.to_dict()) + '```')

client.run(TOKEN)