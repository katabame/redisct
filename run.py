# encoding: utf-8
import asyncio
import discord
import json

with open('config.json', encoding="utf-8") as file:
    config = json.load(file)

client = discord.Client()

embed_hello = discord.Embed(title=config["hello_title"], colour=discord.Colour.blue(), description=config["hello_description"])
embed_hello.set_author(name="This message sent by redisct system.", url="https://github.com/katabame/redisct", icon_url="https://twemoji.maxcdn.com/2/72x72/1f517.png")


embed_done = discord.Embed(title=config["done_title"], colour=discord.Colour.green(), description=config["done_description"])
embed_done.set_author(name="This message sent by redisct system.", url="https://github.com/katabame/redisct", icon_url="https://twemoji.maxcdn.com/2/72x72/1f517.png")

embed_timeout = discord.Embed(title=config["timeout"], colour=discord.Colour.red(), description=config["timeout_description"])
embed_timeout.set_author(name="This message sent by redisct system.", url="https://github.com/katabame/redisct", icon_url="https://twemoji.maxcdn.com/2/72x72/1f517.png")


@client.event
async def on_ready():
    print('------------------------')
    print('Logged in as {0} ({1})'.format(client.user.name, client.user.id))
    print('Watching: {0}'.format(config["guild_id"]))
    print('------------------------')

@client.event
async def on_member_join(member):
    if member.guild.id == config["guild_id"]:
        print("[Join] " + member.name)
        message = await member.send(embed=embed_hello)
        await member.kick()

        try:
            relationship = await client.wait_for('relationship_add', timeout=config["wait_time"])
        except asyncio.TimeoutError:
            print("[Timeout] " + member.name)
            await relationship.delete()
            await message.edit(embed=embed_timeout)
        else:
            if relationship.user.id == member.id and relationship.type == discord.RelationshipType.incoming_request:
                print("[Relationship] " + member.name)
                await relationship.accept()
                await message.edit(embed=embed_done)

if __name__ == "__main__":
    client.run(config["token"], bot=False)
