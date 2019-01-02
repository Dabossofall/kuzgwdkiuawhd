import random
import discord
import globals
import test

token = " "
prefix = ";"
bot = discord.Client()
IanClientID = 289171968907935746
DamienClientID = 222765804398051329
globals.initialize()

@bot.event
async def on_message(msg):
	channel = msg.channel
	author = msg.author
	msg = msg.content
	append = " "
	if msg.startswith(prefix):
		if msg.startswith(prefix + "say"):
			msg = msg.replace(prefix + "say", "")

			await channel.send(msg)
		elif msg.startswith(prefix + "iq"):
			iq = random.randint(-500, 5)

			if iq < -300:
				append = "**Big Brain Activiated**"

			await channel.send(f"{author.mention} {iq} {append}")
		elif msg.startswith(prefix + "money"):
			money = random.randint(3, 100000)
			moneysign = "$"
			negative = "-"
			append = "Well looks like someone spent to much money at the casino :joy:"

			await channel.send(f"{author.mention} {negative}{moneysign}{money} {append}")

		elif msg.startswith(prefix + "succ"):

			await channel.send("https://www.youtube.com/watch?v=fPNdWnwuBDI")

		elif msg.startswith(prefix + "how thicc"):
			thiccness = random.randint(1, 11)
			prethicc = "You're"
			postthicc = "/10"
			if thiccness > 10:
				append = "Damn you thicc as hell"

			await channel.send(f"{author.mention} {prethicc} {thiccness}{postthicc} {append}")

		elif msg.startswith(prefix + "die"):
			die = "Die!"
			await channel.send(f"{die} {author.mention}")

		elif msg.startswith(prefix + "zucc"):

			await channel.send("https://cdn.discordapp.com/attachments/483793701613600809/529826559788580886/20182F042F042F912F45aa16dc19be439a8366f647c27613ef.png")

		elif msg.startswith(prefix + "STOP TIME"):

			await channel.send("https://cdn.discordapp.com/attachments/483793701613600809/529827466777329674/ZA_WARDUO.gif")

		elif msg.startswith(prefix + "Za Warudo"):

			await channel.send("https://cdn.discordapp.com/attachments/483793701613600809/529827466777329674/ZA_WARDUO.gif")

		elif msg.startswith(prefix + "You expected"):

			await channel.send("https://cdn.discordapp.com/attachments/483793701613600809/529828617136373761/566.png")

		elif msg.startswith(prefix + "WhoreCounter"):
			test.increment4()
			PreWhore = "Damien has said Whore"
			WhoreNum = globals.WhoreNum
			PostWhore = "times today."
			if WhoreNum == 1:
				PostWhore = "time today"
			await channel.send(f"{PreWhore} {WhoreNum} {PostWhore}")

		elif msg.startswith(prefix + "IanWillRememberThat"):
			IanPicture = "https://cdn.discordapp.com/attachments/483793701613600809/529895156091191314/Ianwillrememberthat.png"
			IanWillRememberThat = "```Ian will remember that...```"
			test.increment3()
			await channel.send(f"{globals.IanRemember} {IanWillRememberThat} {IanPicture}")

		elif msg.startswith(prefix + "IanThreat"):
			test.increment2()
			PreThreatI = "Damien has threated Ian"
			PostThreatI = "times today"
			if globals.num2 == 1:
				PostThreatI = "time today"
			await channel.send(f"{PreThreatI} {globals.num2} {PostThreatI}")

		elif msg.startswith(prefix + "LandonThreat"):
			test.increment()
			PreThreat = "Damien has threated Landon"
			PostThreat = "times today"
			if globals.num == 1:
				PostThreat = "time today"
			await channel.send(f"{PreThreat} {globals.num} {PostThreat}")

@bot.event
async def on_ready():
    print("TestBot\n")

bot.run(token)
#/ "C:\Users\Damien\Desktop\Desktop\DiscordPython\DJ Bot\Bot.py""C:\Users\Damien\Desktop\Desktop\DiscordPython\DJ Bot\Bot.py""C:\Users\Damien\Desktop\Desktop\DiscordPython\DJ Bot\Bot.py"