import discord, asyncio, varHugoland
import urllib.request

class HugoBot(discord.Client):
    def __init__(self):
        super().__init__()
        self.version = "1.1.0-DEV"
        
    async def on_ready(self):
        print(self.user.name)
        print(self.user.id)
        
    async def on_message(self,message):
        if message.author.id == "307984283774222348":
            msg = message.content.lower()
            if "ok" in msg:
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
            aide = discord.Embed(title="HugoBot - Help System V1.0", description="Système d'assistance d'HugoBot", colour = 0x2ecc71)
            aide.set_footer(text="HugoBot - Help System V1.0",icon_url="https://cdn4.iconfinder.com/data/icons/meBaze-Freebies/512/info.png")
            aide.add_field(name = "- !help", value = "Commande actuelle", inline = False)
            aide.add_field(name = "- !info", value = "Informations sur moi", inline = False)
            aide.add_field(name = "- !staff", value = "Le Staff de la communauté", inline = False)
            aide.add_field(name = "- !ping",value = "Pour savoir si je suis là", inline = False)
            await self.send_message(message.channel,embed=aide)
        if message.content.startswith("!info"):
            info = discord.Embed(title="HugoBot", description="Bot d'Hugoland", colour = 0x3498db)
            info.set_footer(text="HugoBot",icon_url="https://cdn4.iconfinder.com/data/icons/meBaze-Freebies/512/info.png")
            info.add_field(name = "Codé par",value = "LavaPower")
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


client = HugoBot()
client.run(varHugoland.getVar())
