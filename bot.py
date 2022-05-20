
#installs all nessisary pips (removed so that code can run on rasberry pi)
"""
try:
    import lightbulb
    import hikari
    from dotenv import load_dotenv
    import requests 
except ImportError:
    print("NEED TO PIP INSTALL LIGHTBULB HIKARI DOTENV AND REQUESTS")
"""
#imports pips
from ctypes import Union
import lightbulb
import hikari
import datetime
from dotenv import load_dotenv
import requests 
from random import seed
from random import randint

#token stripping (please add your own token below!)
TOKEN = "OTY5MzI3NzUxNzc1NTMxMDQ4.  Ymry0Q.rVeFlbGXxc10HQrPQrjLJ_Xa8Hk"
print(TOKEN)
TOKEN = TOKEN.replace(" ", "")
seed(1)


#bad bad bad enifficent code
#I GIVE UP IF IT WORKS IT WORKS
def verse_funct_text(r):
    

    #getting the text of the verse
    finaltxt = str(r.text)
    finaltxt = finaltxt.split("bilingual-left", 1)
    finaltxt = finaltxt[1]
    finaltxt = finaltxt.split("div", 1)
    finaltxt = finaltxt[0]
    finaltxt = finaltxt.replace(">", "") 
    finaltxt = finaltxt.replace("<", "") 
    final_verse_text = finaltxt + '"'
    

    #getting the verse number(id? idk) of the verse
    finaltxt = str(r.text)
    finaltxt = finaltxt.split("Verse of the Day:", 1)
    finaltxt = finaltxt[1]
    finaltxt = finaltxt.split('"/>', 1)
    finaltxt = finaltxt[0]
    final_verse_text =  final_verse_text +" -" + finaltxt

    print(final_verse_text)
    return(final_verse_text)

def verse_funct_image(r):

    #getting the image of the verse
    finaltxt = str(r.text)
    finaltxt = finaltxt.split("fb-comments", 1)
    finaltxt = finaltxt[1]
    finaltxt = finaltxt.split("data-num-posts=", 1)
    finaltxt = finaltxt[0]
    finaltxt = finaltxt.replace('" data-href="', "") 
    final_verse_image = finaltxt.replace('"', "") 

    print(final_verse_image)
    return(final_verse_image)


#calculating days until next camp
today = datetime.date.today()
#why is the date randomly 1-2 days off IDK BUT IT SURE AS HELL IS ANNOYING
future = datetime.date(2022,7,17)
diff = future - today
days_until = str(diff.days)


#authing discord bot and adding servers
bot = lightbulb.BotApp(
    token=TOKEN,
    default_enabled_guilds=(733440457618620417, 952065165988339722, 794686304810041345)
)


#check for the discord bot starting
@bot.listen(hikari.StartedEvent)
async def on_start(event):
    print("dish bot Esh workin")


#DAYS UNITL CAMP COMMAND
@bot.command
@lightbulb.command("time-until-camp", "tells you the ammount of days until the next camp")
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond("It is {} days until camp!" .format(days_until))

#WEBSITE COMMAND
@bot.command
@lightbulb.command("website", "the bot github website!")
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond("https://github.com/Ethaisa123/Willow-discord-bot")


#JESUS COMMAnD
@bot.command
@lightbulb.command("jesus", "jesus!")
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    value = randint(0, 3)
    jesus = [
    "https://upload.wikimedia.org/wikipedia/en/d/de/Piss_Christ_by_Serrano_Andres_%281987%29.jpg",
    "https://static.wikia.nocookie.net/headhuntersholosuite/images/d/d8/Jesus_Christ.jpg/revision/latest/scale-to-width-down/225?cb=20171123000925",
    "https://wp.en.aleteia.org/wp-content/uploads/sites/2/2018/10/web3-christ-pantocrator-pd.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/The_Last_Supper_-_Leonardo_Da_Vinci_-_High_Resolution_32x16.jpg/1200px-The_Last_Supper_-_Leonardo_Da_Vinci_-_High_Resolution_32x16.jpg"
    ]
    print(value)
    print(jesus[value])
    await ctx.respond(jesus[value])

#BOT COMMAND FOR VERSE
@bot.command()
@lightbulb.option("verse", "type of verse shown", choices=["verse-text", "verse-image"], required=True)
@lightbulb.command("verse-of-the-day", "a random verse every day")
@lightbulb.implements(lightbulb.SlashCommand)
async def echo(ctx):
    #THIS DOESNT WORK AND I DONT KNOW WHY I HAVE BEEN BASHING MY HEAD AGAINST A WALL FOR TO LONG NOW
    payload = {'key1': 'value1', 'key2': 'value2'}
    r = requests.get('https://www.verseoftheday.com/', params=payload)
    
    if ctx.options.verse == "verse-text":
        await ctx.respond(verse_funct_text(r))
    elif ctx.options.verse == "verse-image":
        await ctx.respond(verse_funct_image(r))
    

#BOT COMMAND FOR PLAYLIST
@bot.command()
@lightbulb.option("camps", "the song playlists from different camps", choices=["futuristic-camp", "retro-camp", "general-playlist"], required=True)
@lightbulb.command("camp-playlists", "the song playlists from different camps")
@lightbulb.implements(lightbulb.SlashCommand)
async def echo(ctx):
    if ctx.options.camps == "futuristic-camp":
        await ctx.respond("futuristic-link")
    elif ctx.options.camps == "retro-camp":
        await ctx.respond(ctx.options.camps + ": https://open.spotify.com/playlist/2fhDqL3iwb2ar85FlxXE8p")
    elif ctx.options.camps == "general-playlist":
        await ctx.respond(ctx.options.camps + ": https://open.spotify.com/playlist/1bOpQMbSqb1lWmAsqyGcQX")

#bot command bug report
@bot.command
@lightbulb.option("bug", "a place to type any bugs you find")
@lightbulb.command("bug-report", "if you find any bugs or issues write about it here")
@lightbulb.implements(lightbulb.SlashCommand)
async def add(ctx):
    
    await ctx.respond("thankyou for issuing a bug report \nthe bug has now been recorded for the willow developers :)")
    date = str(today)
    print(ctx.options.bug + " : " + date)
    f = open("bugs.txt", "a")
    f.write("{} : {} : {} \n" .format(ctx.author.username, ctx.options.bug ,str(date)) )
    f.close()

#VIDEOS COMMAND
@bot.command()
@lightbulb.option("camps", "the videos from different camps", choices=["retro-camp", "futuristic-camp", "olympic-camp", "aquatic-camp"], required=True)
@lightbulb.command("camp-videos", "the videos from different camps")
@lightbulb.implements(lightbulb.SlashCommand)
async def echo(ctx):
    if ctx.options.camps == "futuristic-camp":
        await ctx.respond("futuristic camp video: https://youtu.be/aN5QyQjnYfc")
    elif ctx.options.camps == "retro-camp":
        await ctx.respond("retro camp video: https://youtu.be/Opnf18B1Kh8")
    elif ctx.options.camps == "olympic-camp":
        await ctx.respond("olympic camp video: https://www.youtube.com/watch?v=I47Ig4-lhZI&ab_channel=Videos%3A%29")
    elif ctx.options.camps == "aquatic-camp":
        await ctx.respond("aquatic camp video: https://youtu.be/StextHDOZw8/")

#PHOTOS COMMAND
@bot.command()
@lightbulb.option("camps", "the photos from different camps (contact Ethan to add photos)", choices=["retro-camp", "futuristic-camp-N/A", "olympic-camp-N/A", "aquatic-camp-N/A"], required=True)
@lightbulb.command("camp-photos", "the photos from different camps (contact Ethan to add photos)")
@lightbulb.implements(lightbulb.SlashCommand)
async def echo(ctx):
    if ctx.options.camps == "futuristic-camp-N/A":
        await ctx.respond("futuristic camp photos: https://photos.app.goo.gl/mk8hxmbD56VraC2H6")
    elif ctx.options.camps == "retro-camp":
        await ctx.respond("retro camp photos: https://photos.app.goo.gl/Y6AJQGjoeTibqiib7")
    elif ctx.options.camps == "olympic-camp-N/A":
        await ctx.respond("olympic camp photos: https://photos.app.goo.gl/3o2s9GQsAxwrhEfz6")
    elif ctx.options.camps == "aquatic-camp-N/A":
        await ctx.respond("aquatic camp photos: https://photos.app.goo.gl/iBAq9KHLn3SfvLmC6")



bot.run()
