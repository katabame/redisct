# encoding: utf-8
import asyncio
import discord
import json

with open('config.json', encoding="utf-8") as file:
    config = json.load(file)

client = discord.Client()


@client.event
async def on_ready():
    print('------------')
    print('Logged in as {0} ({1})'.format(client.user.name, client.user.id))
    print('Watching: {0}'.format(config["server_id"]))
    print('------------')

@client.event
async def on_member_join(member):
    if member.server.id == str(config["server_id"]):
        print(member.name + " joined!")
        await client.send_message(member, config["message"])
        await client.kick(member)

if __name__ == "__main__":
    client.run(config["email"], config["password"])
