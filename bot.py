import discord
from settings import TOKEN, GUILD_ID
from discord import guild
from pintoreddit import reddit, sub_reddit
import time

client = discord.Client()

text_channel_list = []

# vars for Reddit
pinid = ""
author = ""
title = ""
clean_content = ""
embed_url = ""
embed_title = ""
embed_type = ""
jump_url = ""
embed_desc = ""

@client.event
async def on_ready():
    print(f"Logged in to Discord as {client.user}\n")

@client.event
async def on_message(message):
    print(
        f"#{message.channel}|{message.author.name}({message.author}):{message.content}"
    )
    
    # get a listing of channels in the server
    if "!channels" in message.content.lower():
        channel_generator = client.get_all_channels()
        for channel in channel_generator:
            if (channel.name.lower() != 'text channels') and (channel.name.lower() != 'voice channels'):
                text_channel_list.append(channel.name)
        await message.channel.send(text_channel_list)

    # use the keyword 'pins' to get pinned content
    if "!pins" in message.content.lower():
        myGuild = client.get_guild(GUILD_ID)
        for textChannel in myGuild.text_channels:
            #await message.channel.send('#'+ textChannel.name)
            for pin in await textChannel.pins():

                # Pin ID (never None)
                # content (never None)
                # jump_url into Discord (never None)
                # Attachments, if any (could be None)
                # embed title (could be None)
                # embed URL (could be None)
                # embed type (could be None)
                
                # Get Pin ID
                pinid = pin.id
                await message.channel.send('pin: ```' + str(pin.id) + '```')

                # Get the author details
                if pin.author:
                    author = pin.author
                    await message.channel.send("author = " + str(author))

                if pin.content:
                    title = pin.content
                    await message.channel.send("content = " + str(pin.content))

                if pin.jump_url:
                        jump_url = pin.jump_url
                        #await message.channel.send("jump_url = " + str(jump_url))

                # Get embeds from within the Pin
                if hasattr(pin, "embeds") and len(pin.embeds) > 0:
                    try:
                        for embed in pin.embeds:
                            if hasattr(embed, "title"):
                                embed_title = embed.title
                                #await message.channel.send("Embedded title = " + str(embed_title))
                            if hasattr(embed, "url"):
                                embed_url = embed.url
                                #await message.channel.send("Embedded URL = " + str(embed_url))
                            if hasattr(embed, "type"):
                                embed_type = embed.type
                                #await message.channel.send("Embedded type = " + str(embed_type))
                                if embed_type=="rich":
                                    embed_desc=embed.description
                                    reddit.subreddit(sub_reddit).submit(embed_desc[0:50]+"..."+" (via "+str(author)+")", selftext="{}".format(embed_url))
                                    print("Submitted pin with ID = ", pinid, " to Reddit")
                                else:
                                    reddit.subreddit(sub_reddit).submit(embed_title+" (via "+str(author)+")", selftext="{}".format(embed_url))
                                    print("Submitted pin with ID = ", pinid, " to Reddit")
                    except:
                        AttributeError
                elif hasattr(pin, "attachments") and len(pin.attachments) > 0:
                    for attachment in pin.attachments:
                        #await message.channel.send("Attachment = " + str(attachment.url))
                        # Post each pin to Reddit
                        reddit.subreddit(sub_reddit).submit(title+" (via "+str(author)+")", selftext="{}".format(attachment.url))
                        print("Submitted pin with ID = ", pinid, " to Reddit")
                else:
                    reddit.subreddit(sub_reddit).submit(title+" (via "+str(author)+")", selftext="")
                    print("Submitted pin with ID = ", pinid, " to Reddit")

client.run(TOKEN)