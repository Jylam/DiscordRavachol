# Copyright © 2021-2022  Jylam <github@frob.fr>
# This work is free. You can redistribute it and/or modify it under the
# terms of the Do What The Fuck You Want To Public License, Version 2,
# as published by Sam Hocevar. See the COPYING file for more details.

import os
import discord
import urllib, json
import urllib.request
import re
import random

GUILD = 'Ostinautoscope'

TOKEN = os.environ.get('RAVACHOL_TOKEN')
intents = discord.Intents.all()
client = discord.Client(intents=intents)

def findWholeWord(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search


@client.event
async def on_ready():
        for guild in client.guilds:
            if guild.name == GUILD:
                    break
        print("Ready.")
@client.event
async def on_message(message):
        macron_list = ["MACRON DEMISSION !", "♬ ON EST LÀÀÀ ON EST LÀÀÀ MÊME SI MACRON NE VEUT PAS NOUS ON EST LÀÀÀ ♬", "Macron explosion !"]
        gibouin_list = ["TA GUEUUULE CONNNAAAAARD", "Elle a son attestation madame Gibouin ?", "♬ Bon ben ça fera 135 euros ♬"]

        if message.author == client.user:
            return

        print("Message from", message.author,":", message.content)

        if findWholeWord('darmanin')(message.content) != None:
            response = "Le sale violeur ?"
            await message.channel.send(response)
        if findWholeWord('valls')(message.content) != None:
            response = "Qui ?"
            await message.channel.send(response)
        if findWholeWord('blanquer')(message.content) != None:
            response = "Le Beluga blanc ?"
            await message.channel.send(response)
        if findWholeWord('zemmour')(message.content) != None:
            response = "Le candidat fasciste ?"
            await message.channel.send(response)
        if findWholeWord('Ciotti')(message.content) != None:
            response = "Celui qui est chauve ?"
            await message.channel.send(response)
        if findWholeWord('macron')(message.content) != None:
            r = random.randint(0, 3)
            print("MACRON R : %d"%(r))
            if(r == 0):
                response = random.choice(macron_list)
                await message.channel.send(response)
        elif message.content == 'Syndiquez vous':
            response = "Absolument mon bon Michel."
            await message.channel.send(response)
        elif message.content == '!sarouel':
            response = "p'tit terr pour fêter ça ?"
            await message.channel.send(response)
        if findWholeWord('sarouel')(message.content) != None:
            response = "@bubuchenbois ?"
            await message.channel.send(response)
        if findWholeWord('coupable')(message.content) != None:
            response = "sauf Carlos Ghosn !"
            await message.channel.send(response)
        if findWholeWord('jambon')(message.content) != None or findWholeWord('fromage')(message.content) != None:
            response = "des choses concrètes"
            await message.channel.send(response)
        if (findWholeWord('gibouin')(message.content) != None) or (message.content == '!mmegibouin'):
            response = random.choice(gibouin_list)
            await message.channel.send(response)
        if findWholeWord('mediapart')(message.content) != None:
            response = "edwy moustache"
            await message.channel.send(response)
        if findWholeWord('roussel')(message.content) != None:
            response = "🥩 🥓 🍖 🍷"
            await message.channel.send(response)
print("Running client...")
client.run(TOKEN)
print("Done")

