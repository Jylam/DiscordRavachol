# Copyright © 2021-2022  Jylam <github@frob.fr>
# This work is free. You can redistribute it and/or modify it under the
# terms of the Do What The Fuck You Want To Public License, Version 2,
# as published by Sam Hocevar. See the COPYING file for more details.

import discord
import os
import sys
import urllib
import urllib.request
import re
import random
import yaml

GUILD = 'Ostinautoscope'
TOKEN = os.environ.get('RAVACHOL_TOKEN')
COMMAND_FILE="commands.yaml"
data = None



def findWholeWord(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

def run_command(input_dict):
    print("Running command for", input_dict)
    if "random" in input_dict:
        random_value = int(input_dict["random"])
        if random_value > 0:
            to_print = random.randint(0, random_value-1)
            if to_print != 0:
                return None

    if "responses" in input_dict:
        length = len(input_dict["responses"])
        offset = 0;
        random_str = random.randint(0, length-1)
        return input_dict["responses"][random_str]
    return None

def findWholeWord(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

def find_and_run_command(input_str):
    for name in data:
        if name == "single":
            for command in data[name]:
                if command == input_str:
                    return run_command(data[name][command])
        if name == "match":
            for command in data[name]:
                if findWholeWord(command)(input_str) != None:
                    return run_command(data[name][command])

    return None



intents = discord.Intents.all()
client = discord.Client(intents=intents)
@client.event
async def on_ready():
    global data
    print("Client ready")
    for guild in client.guilds:
        if guild.name == GUILD:
                break
    try:
        with open(COMMAND_FILE, 'r') as f:
            data = yaml.load(f)
            print("Loaded yaml")
    except:
        print("Can't open", COMMAND_FILE, ". Exiting.")
        sys.exit(1)

    print("Ready.")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    resp = find_and_run_command(message.content)
    if resp != None:
        print("Message from", message.author,":", message.content)
        await message.channel.send(resp)



print("Running client with token", TOKEN)
client.run(TOKEN, reconnect=True)
print("Done")


