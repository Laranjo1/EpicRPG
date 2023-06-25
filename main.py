import discord
from discord.ext import commands
import asyncio
import os
import tensorflow as tf
from tensorflow import keras
from tensorflow import keras
from pathlib import Path
import os
import matplotlib.pyplot as plt
from PIL import Image
import io
import numpy as np
import requests
from IA import *
bot = commands.Bot(command_prefix='>', self_bot=True)
i = 0
temp = 0
pararTudo = False
model = tf.keras.models.load_model("model\\classifier.h5")
class_names = ['apple', 'banana', 'chip', 'coin', 'dragon scale','dungeon key', 'epic coin', 'epic fish', 'fish', 'golden fish', 'life potion', 'mermaid hair', 'ruby', 'unicorn horn', 'wolf skin', 'zombie eye']
num_classes = len(class_names)
arena=884387992159002654
eventos=884387988111523861
caca = 0
aventura = 0
trabalha = 0
looteado = 0
farma = 0
@bot.event
async def on_ready():
  print('We have logged in as {0.user}'.format(bot))
  bot.loop.create_task(cacar())
  await asyncio.sleep(2)
  bot.loop.create_task(trabalhar())
  await asyncio.sleep(2)
  bot.loop.create_task(aventurar())
  await asyncio.sleep(5)
  bot.loop.create_task(loot())
  await asyncio.sleep(3)
  bot.loop.create_task(farm())
  await asyncio.sleep(3)
  bot.loop.create_task(checkChat())
async def checkChat():
  global pararTudo
  while not pararTudo:
    for guild in bot.guilds:
        channel = discord.utils.get(guild.channels, id=arena)
        channel1 = discord.utils.get(guild.channels, id=eventos)
        if channel or channel1:
          if (channel.permissions_for(guild.me).read_messages and channel.permissions_for(guild.me).send_messages == True and channel.permissions_for(guild.me).read_message_history == True) or (channel1.permissions_for(guild.me).read_messages and channel1.permissions_for(guild.me).send_messages == True and channel1.permissions_for(guild.me).read_message_history == True):
            pass
          else:
            pararTudo = True
            print("O bot não tem permissão para ver logo desliga tudo!")
    await asyncio.sleep(3)

async def farm():
  global pararTudo
  global temp
  global farma
  await bot.wait_until_ready()
  channel = bot.get_channel(1120882507181719552) 
  while not bot.is_closed() and not pararTudo:
    await channel.send('rpg farm')
    farma=farma+1
    os.system('cls')
    print(f"cacei: {caca}\ntrabalhei: {trabalha}\nfarmei: {farma}\naventurei: {aventura}\nlootei: {looteado}")
    await asyncio.sleep(600+temp)
    temp = 0

async def aventurar():
  global pararTudo
  global i
  global temp
  global aventura
  await bot.wait_until_ready()
  channel = bot.get_channel(1120882507181719552)
  while not bot.is_closed() and not pararTudo:
    await channel.send("rpg heal")
    await asyncio.sleep(2)
    await channel.send("rpg adventure")
    aventura=aventura+1
    os.system('cls')
    print(f"cacei: {caca}\ntrabalhei: {trabalha}\nfarmei: {farma}\naventurei: {aventura}\nlootei: {looteado}")
    await asyncio.sleep(3601+temp)
    temp = 0


async def trabalhar():
  global pararTudo
  global temp
  global trabalha
  await bot.wait_until_ready()
  channel = bot.get_channel(1120882507181719552) 
  while not bot.is_closed() and not pararTudo:
    await channel.send('rpg axe')
    trabalha=trabalha+1
    os.system('cls')
    print(f"cacei: {caca}\ntrabalhei: {trabalha}\nfarmei: {farma}\naventurei: {aventura}\nlootei: {looteado}")
    await asyncio.sleep(301+temp)
    temp = 0


async def cacar():
  global pararTudo
  global temp
  global caca
  await bot.wait_until_ready()
  channel = bot.get_channel(1120882507181719552) 
  while not bot.is_closed() and not pararTudo:
    await channel.send('rpg hunt')
    caca=caca+1
    os.system('cls')
    print(f"cacei: {caca}\ntrabalhei: {trabalha}\nfarmei: {farma}\naventurei: {aventura}\nlootei: {looteado}")
    await asyncio.sleep(61+temp)
    temp = 0

async def loot():
  global pararTudo
  global temp
  global looteado
  await bot.wait_until_ready()
  channel = bot.get_channel(1120882507181719552) 
  while not bot.is_closed() and not pararTudo:
    await channel.send('rpg buy edgy lootbox')
    looteado=looteado+1
    os.system('cls')
    print(f"cacei: {caca}\ntrabalhei: {trabalha}\nfarmei: {farma}\naventurei: {aventura}\nlootei: {looteado}")
    await asyncio.sleep(10801+temp)
    temp = 0

@bot.event
async def on_message(message):
  global pararTudo
  if message.channel.id == 884387988111523861 and message.components:
    print(message.components)
  if pararTudo == False:
    if (message.channel.id == 884387988111523861 or message.channel.id == 884387992159002654)and message.author.id == 555955826880413696:
      if message.components:
          for child in message.components[0].children:
            if child.custom_id == "arena_join":
              await asyncio.sleep(2)
              await child.click()
            if child.custom_id == "coinrain_join":
              await asyncio.sleep(3)
              await child.click()
            if child.custom_id == "epictree_join":
              await asyncio.sleep(3)
              await child.click()
            if child.custom_id == "megalodon_join":
              await asyncio.sleep(3)
              await child.click()
            if child.custom_id == "lootboxsummoning_join":
              await asyncio.sleep(2)
              await child.click()
            if child.custom_id == "legendaryboss_join":
              await asyncio.sleep(3)
              await child.click()
    if message.channel.id == 1120882507181719552 and message.author.id == 555955826880413696:
      if "remaining HP is" in message.content and "puchila" in message.content:
        start_index = message.content.find("remaining HP is") + len("remaining HP is")
        end_index = message.content.find("/", start_index)
        hp = int(message.content[start_index:end_index].strip())
        if hp < 40:
          global temp
          temp = 3
          await asyncio.sleep(3)
          await message.channel.send("rpg heal")
      if "EPIC GUARD" in message.content:
        pararTudo = True
        if message.attachments:
            img_url = message.attachments[0].url
            img_url = img_url.replace("https://cdn.discordapp.com", "https://media.discordapp.net") + "?width=700&height=200"
            response = requests.get(img_url)
            image_bytes = response.content
            image = Image.open(io.BytesIO(image_bytes))
            image = image.convert('RGB')
            image = np.expand_dims(image, axis=0)
            predictions = model.predict(image)
            class_index = np.argmax(predictions)
            class_label = class_names[class_index]
            probability = predictions[0][class_index]
            print("Classe prevista:", class_label)
            print("Porcentagem de chance:", probability, "%")
            await message.channel.send(class_label)
            await message.channel.send(f"Classe prevista -> {class_label}\nPorcentagem -> {probability}%")
            await asyncio.sleep(3)
      if "Everything seems fine puchila, keep playing"  in message.content:
        pararTudo = False
      
  await bot.process_commands(message)
bot.run("MTEwNTYzMTM3ODM5MDkyNTQ2NA.GeVph_.H31YCRh6h7ytkCGlxglJZo5TA65C_wrr0FyC_0")


