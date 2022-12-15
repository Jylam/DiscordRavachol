import os
import discord
import urllib, json
import urllib.request
import re
import random

GUILD = 'Ostinautoscope'
client = None

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

        print("Message from '%s' : '%s'",(message.author, message.content))

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
        if message.content == '!pontivy':
            print("Pontivy")
            response = urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?appid="+OPENWMAP_TOKEN+"&q=pontivy")

            data = json.loads(response.read().decode('utf-8'))
            if data["cod"] != "404":
                d = data["main"]
                print(d)
                temp = d["temp"] - 273.15
                humi = d["humidity"]
                tempr = d["feels_like"] - 273.15
                macron_list = ["MACRON DEMISSION !", "♬ ON EST LÀÀÀ ON EST LÀÀÀ MÊME SI MACRON NE VEUT PAS NOUS ON EST LÀÀÀ ♬"]
                response = "Meteo de Pontivy: %.1f°C, humidité %.1f%%, température ressentie %.1f°C.\nLe Napoleonoscope n'est pour le moment toujours pas confirmé."%(temp, humi, tempr)
                await message.channel.send(response)
            else:
                print("Error getting weather")

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

def main():
    global client
    global OPENWMAP_TOKEN
    TOKEN = os.environ['RAVACHOL_TOKEN']
    OPENWMAP_TOKEN = os.environ['OPENWMAP_TOKEN']
    print("Running client...")
    intents = discord.Intents.all()
    client = discord.Client(intents=intents)
    client.run(TOKEN)
    print("Done")



if __name__ == '__main__':
    main()
