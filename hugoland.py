import discord, asyncio, varHugoland, urllib.request
from bs4 import BeautifulSoup

class HugoBot(discord.Client):
	def __init__(self):
		super().__init__()
		self.version = "1.3.2"
		
	async def on_ready(self):
		print(self.user.name)
		print(self.user.id)
		
	async def on_message(self,message):
		if message.author.id == "307984283774222348":
			msg = message.content.lower()
			if "ok" in msg or "\U0001F197" in msg or ("\U0001F1F4" in msg and "\U0001F1F0" in msg):
				await self.delete_message(message)
		if message.content.startswith("!wiki"):
			if len(message.content) == 5 or len(message.content) == 6:
				await self.send_message(message.channel,"ERREUR : Utilise !wiki <recherche>")
			else:
				msg = message.content.split(" ")
				keyWords=""
				for i in range(1, len(msg)):
					if i == len(msg)-1:
						keyWords += msg[i]
					else:
						keyWorlds += msg[i] + " "
				adresse = "http://fr.hugoland-minecraft.wikia.com/wiki/Spécial:Recherche?query="+keyWords
				await self.send_message(message.channel,adresse)
		if message.content.startswith("!ping"):
			await self.send_message(message.channel, "Pong ! Je suis toujours là")
		if message.content.startswith("!help"):
			aide = discord.Embed(title="HugoBot - Help System V" + self.version, description="Système d'assistance d'HugoBot", colour = 0x2ecc71)
			aide.set_footer(text="HugoBot - Help System V" + self.version,icon_url="https://cdn4.iconfinder.com/data/icons/meBaze-Freebies/512/info.png")
			aide.add_field(name = "- !help", value = "Commande actuelle", inline = False)
			aide.add_field(name = "- !info", value = "Informations sur moi", inline = False)
			aide.add_field(name = "- !staff", value = "Le Staff de la communauté", inline = False)
			aide.add_field(name = "- !ping", value = "Pour savoir si je suis là", inline = False)
			aide.add_field(name = "- !haddock", value = "Génère aléatoirement un juron façon Cpt. Haddock", inline = False)
			aide.add_field(name = "- !wiki <article>", value = "Poste le lien d'un article du wiki", inline = False)
			aide.add_field(name = "- !màj <article>", value = "Poste la dernière mise à jour d'un article du wiki dans le salon #actu-wiki", inline = False)
			aide.add_field(name = "- !cours <id bloc/item>", value = "Poste les prix actuels du bloc/item ayant l'id donné", inline = False)
			await self.send_message(message.channel,embed=aide)
		if message.content.startswith("!info"):
			info = discord.Embed(title="HugoBot", description="Bot d'Hugoland", colour = 0x3498db)
			info.set_footer(text="HugoBot",icon_url="https://cdn4.iconfinder.com/data/icons/meBaze-Freebies/512/info.png")
			info.add_field(name = "Codé par",value = "LavaPower et Spyromain")
			info.add_field(name = "Version",value=self.version)
			await self.send_message(message.channel,embed=info)
		if message.content.startswith("!staff"):
			staff = discord.Embed(title="Staff", description="Staff d'Hugoland", colour = 0x3498db)
			staff.set_footer(text="Staff",icon_url="https://cdn4.iconfinder.com/data/icons/meBaze-Freebies/512/info.png")
			staff.add_field(name = "Administrateur",value="Hugo7", inline = False)
			staff.add_field(name = "Modérateur",value="LavaPower", inline = False)
			staff.add_field(name = "Développeur",value="Spyromain", inline = False)
			await self.send_message(message.channel,embed=staff)
		if message.content.startswith("!haddock"):
			with urllib.request.urlopen("http://data.hugoland.fr/haddock.php?method=clair") as response:
				haddock = response.read().decode('utf8')
				await self.send_message(message.channel, haddock)
		if message.content.startswith("!màj"):
			if message.content == "!màj":
				await self.send_message(message.channel, "Usage : !màj <article>")
			elif len(message.content) > 4 and message.content[4] != " ":
				await self.send_message(message.channel, "Commande inconnue. Peut-être souhaitiez-vous utiliser la commande !màj <article> ?")
			else:
				arg = message.content[5:]
				if not arg:
					await self.send_message(message.channel, "Usage : !màj <article>")
				else:
					url = "http://fr.hugoland-minecraft.wikia.com/wiki/" + urllib.parse.quote(arg)
					history = url + "?action=history"
					with urllib.request.urlopen(history) as response:
						try:
							data = response.read().decode("utf8")
							soup = BeautifulSoup(data, "html.parser")
							author = soup.find("a", class_="mw-userlink").text
							comment = soup.find("span", class_="comment").text
							msg = "**MÀJ** <" + url + ">\n" \
								+ "Par " + author + " : " + comment
							await self.send_message(self.get_channel("356129617779621890"), msg)
						except:
							await self.send_message(message.channel, "Article introuvable")
		if message.content.startswith("!cours"):
			if message.content == "!cours":
				await self.send_message(message.channel, "Usage : !cours <id bloc/item>")
			elif len(message.content) > 6 and message.content[6] != " ":
				await self.send_message(message.channel, "Commande inconnue. Peut-être souhaitiez-vous utiliser la commande !cours <id bloc/item> ?")
			else:
				arg = message.content[7:]
				if not arg:
					await self.send_message(message.channel, "Usage : !cours <id bloc/item>")
				else:
					url = "http://data.hugoland.fr/mc/cours.php?id=" + urllib.parse.quote(arg)
					with urllib.request.urlopen(url) as response:
						data = response.read().decode("utf8")
						soup = BeautifulSoup(data, "html.parser")
						msg = ""
						if arg == "172":
							msg += "**Attention :** les blocs d'argile durcie colorée se " \
								+ "calculent comme ceci : prix du bloc d'argile durcie auquel on " \
								+ "ajoute une valeur de quelques pièces par demi-stack par " \
								+ "niveau de rareté\n"
						prix1 = soup.find("span", id="prix1")
						if prix1:
							prix1 = prix1.text
							if arg == "122":
								prix6 = soup.find("span", id="prix6").text
								prix12 = soup.find("span", id="prix12").text
								msg += "**~~Easteregg~~ DRAGONEGG**\n" \
									+ "**== ID " + arg + " ==**\n" \
									+ "Prix à l'unité : " + prix1 + "p\n" \
									+ "Prix à la demi-douzaine : " + prix6 + "p\n" \
									+ "Prix à la douzaine : " + prix12 + "p"
							else:
								prix8 = soup.find("span", id="prix8").text
								prix16 = soup.find("span", id="prix16").text
								prix64 = soup.find("span", id="prix64").text
								msg += "**== ID " + arg + " ==**\n" \
									+ "Prix à l'unité : " + prix1 + "p\n" \
									+ "Prix pour 8 : " + prix8 + "p\n" \
									+ "Prix pour 16 : " + prix16 + "p\n" \
									+ "Prix pour 64 : " + prix64 + "p"
						else:
							msg += "Aucun coefficient n'est attribué à cet id"
						await self.send_message(message.channel, msg)
		
	async def on_message_edit(self, before, after):
		if after.author.id == "307984283774222348":
			msg = after.content.lower()
			if "ok" in msg or "\U0001F197" in msg or ("\U0001F1F4" in msg and "\U0001F1F0" in msg):
				await self.delete_message(after)
		
	async def on_reaction_add(self, reaction, user):
		if user.id == "307984283774222348" and all(letter in [x.emoji for x in reaction.message.reactions] for letter in ("\U0001F1F4", "\U0001F1F0")):
			await self.remove_reaction(reaction.message, reaction.emoji, user)


client = HugoBot()
client.run(varHugoland.getVar())
