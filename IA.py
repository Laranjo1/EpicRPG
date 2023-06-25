import discord
import json
import os
import requests

JSON_FILE = "imgs.json"
EPIC_GUARD_ID = 555955826880413696


def enviar_imagens(img_url):
	hook = 'https://discord.com/api/webhooks/1121509935520436304/8LaFkv7_L4CYowblqiGmz3Qkf86ueaIDptu9k5gj_nI8I15bDGqGacmLCgvEZgKRtAYA'
	requests.post(hook, data={"content": img_url})



## Verificar mensagem
def its_epic_guard(msg: discord.Message):
	
	check = ":police_car: **EPIC GUARD**: stop there,"
	content = msg.content

	if msg.author.id == EPIC_GUARD_ID and content.startswith(check):		
		if msg.attachments:
			return True

	return False
