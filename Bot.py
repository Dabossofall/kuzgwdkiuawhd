# "C:\Users\Damien\Desktop\Desktop\DiscordPython\kuzgwdkiuawhd-master\Bot.py"
import random

import discord

from resources import *


token = ""
prefix = ";"
bot = discord.Client()
IanClientID = 289171968907935746
DamienClientID = 222765804398051329


@bot.event
async def on_message(msg):
	channel = msg.channel
	author = msg.author
	msg = msg.content
	append = ""

	if msg.startswith(prefix):
		# say
		if msg.startswith(prefix + "say"):
			msg = msg.replace(prefix + "say", "")

			await channel.send(msg)
		# iq
		elif msg.startswith(prefix + "iq"):
			iq = random.randint(-500, 5)

			if iq < -300:
				append = "**Big Brain Activiated**"

			await channel.send(f"{author.mention} {iq} {append}")
		# money
		elif msg.startswith(prefix + "money"):
			money = random.randint(3, 100000)
			moneysign = "$"
			negative = "-"
			append = "Well looks like someone spent to much money at the casino :joy:"

			await channel.send(f"{author.mention} {negative}{moneysign}{money} {append}")
		# succ
		elif msg.startswith(prefix + "succ"):
			await channel.send("https://www.youtube.com/watch?v=fPNdWnwuBDI")
		# how thicc
		elif msg.startswith(prefix + "how thicc"):
			thiccness = random.randint(1, 11)
			prethicc = "You're"
			postthicc = "/10"

			if thiccness == 11:
				append = "Damn you thicc as hell"

			await channel.send(f"{author.mention} {prethicc} {thiccness}{postthicc} {append}")
		# die
		elif msg.startswith(prefix + "die"):
			die = "Die!"

			await channel.send(f"{die} {author.mention}")
		# zucc
		elif msg.startswith(prefix + "zucc"):
			await channel.send("https://cdn.discordapp.com/attachments/483793701613600809/529826559788580886/20182F042F042F912F45aa16dc19be439a8366f647c27613ef.png")
		# STOP TIME
		elif msg.startswith(prefix + "STOP TIME"):
			await channel.send("https://cdn.discordapp.com/attachments/483793701613600809/529827466777329674/ZA_WARDUO.gif")
		# Za Warudo
		elif msg.startswith(prefix + "Za Warudo"):
			await channel.send("https://cdn.discordapp.com/attachments/483793701613600809/529827466777329674/ZA_WARDUO.gif")
		# You expected
		elif msg.startswith(prefix + "You expected"):
			await channel.send("https://cdn.discordapp.com/attachments/483793701613600809/529828617136373761/566.png")
		# WhoreCounter
		elif msg.startswith(prefix + "WhoreCounter"):
			Counter.WhoreNum += 1
			pre = "Damien has said Whore"
			post = "times today."

			if Counter.WhoreNum == 1:
				post = "time today"

			await channel.send(f"{pre} {Counter.WhoreNum} {post}")
		# IanWillRememberThat
		elif msg.startswith(prefix + "IanWillRememberThat"):
			Counter.IanRemember += 1
			IanPicture = "https://cdn.discordapp.com/attachments/483793701613600809/529895156091191314/Ianwillrememberthat.png"
			IanWillRememberThat = "```Ian will remember that...```"

			await channel.send(f"{Counter.IanRemember} {IanWillRememberThat} {IanPicture}")
		# IanThreat
		elif msg.startswith(prefix + "IanThreat"):
			Counter.ian += 1
			PreThreatI = "Damien has threated Ian"
			PostThreatI = "times today"

			if Counter.ian == 1:
				PostThreatI = "time today"

			await channel.send(f"{PreThreatI} {Counter.ian} {PostThreatI}")
		# LandonThreat
		elif msg.startswith(prefix + "LandonThreat"):
			Counter.landon += 1

			PreThreat = "Damien has threated Landon"
			PostThreat = "times today"
			if Counter.landon == 1:
				PostThreat = "time today"

			await channel.send(f"{PreThreat} {Counter.landon} {PostThreat}")


@bot.event
async def on_ready():
	print(f"{bot.user.name}\n")

bot.run(token)
