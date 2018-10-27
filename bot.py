import discord
from settings import TOKEN, GUILD_ID
from discord import guild

client = discord.Client()

text_channel_list = []

@client.event
async def on_ready():
    print(f"Logged in as {client.user}\n")

@client.event
async def on_message(message):
    print(
        f"#{message.channel}|{message.author.name}({message.author}):{message.content}"
    )
    # if "hi there" in message.content.lower():
    #     await message.channel.send('Roger that!')

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
                    await message.channel.send('clean_content: ```' + pin.clean_content + '```')

client.run(TOKEN)