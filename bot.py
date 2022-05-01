
#installs all nessisary pips
try:
    import lightbulb
    import hikari
    from dotenv import load_dotenv
    import requests 
except ImportError:
    os.system('pip install -r requirements.txt')

#imports pips
from ctypes import Union

import lightbulb
import hikari
import datetime
import os
from dotenv import load_dotenv
import requests 

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

#generating files


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


#authing discord bot
bot = lightbulb.BotApp(
    token=TOKEN,
    default_enabled_guilds=(733440457618620417, 952065165988339722, 794686304810041345)
)


#check for the discord bot starting
@bot.listen(hikari.StartedEvent)
async def on_start(event):
    print("dish bot Esh workin")


#sayying the ammount of days when called
@bot.command
@lightbulb.command("time-until-camp", "tells you the ammount of days until the next camp")
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond("It is {} days until camp!" .format(days_until))

@bot.command
@lightbulb.command("website", "the bot github website!")
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond("https://github.com/Ethaisa123/Willow-discord-bot")


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
    f.write(ctx.author.username + " : " + ctx.options.bug + " : " + str(date) + "\n")
    f.close()


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

@bot.command()
@lightbulb.option("camps", "the photos from different camps", choices=["retro-camp", "futuristic-camp-N/A", "olympic-camp-N/A", "aquatic-camp-N/A"], required=True)
@lightbulb.command("camp-photos", "the photos from different camps")
@lightbulb.implements(lightbulb.SlashCommand)
async def echo(ctx):
    if ctx.options.camps == "futuristic-camp":
        await ctx.respond("futuristic camp photos: N/A")
    elif ctx.options.camps == "retro-camp":
        await ctx.respond("retro camp photos: https://photos.app.goo.gl/Y6AJQGjoeTibqiib7")
    elif ctx.options.camps == "olympic-camp":
        await ctx.respond("olympic camp photos: N/A")
    elif ctx.options.camps == "aquatic-camp":
        await ctx.respond("aquatic camp photos: N/A")




"""
https://photos.app.goo.gl/Y6AJQGjoeTibqiib7
"""

bot.run()
