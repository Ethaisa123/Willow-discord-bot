import lightbulb
import hikari
import datetime

#calculating days until next camp
today = datetime.date.today()
future = datetime.date(2022,7,17)
diff = future - today
days_until = str(diff.days)


#authing discord bot
bot = lightbulb.BotApp(
    token="OTY5MzI3NzUxNzc1NTMxMDQ4.Ymry0Q.AVfQBwp7EySxpq1BljrYBdslOuE",
    default_enabled_guilds=(733440457618620417)
)

#check for the discord bot starting
@bot.listen(hikari.StartedEvent)
async def on_start(event):
    print("dees bot Esh workin")



#sayying the ammount of days when called
@bot.command
@lightbulb.command("time-until-camp", "tells you the ammount of days until the next camp")
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond("It is {} days until camp!" .format(days_until))

@bot.command
@lightbulb.command("website", "the bot github website!")

"""
@bot.command
@lightbulb.command("group", "testing groups")
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def my_group(ctx):
    pass

@my_group.child
@lightbulb.command("subcommand", "subcommand this is")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def subcommand(ctx):
    await ctx.respond("subcommand")

@bot.command
@lightbulb.option("num1", "first number", type=int)
@lightbulb.option("num2", "secound number", type=int)
@lightbulb.command("add", "adds numbers")
@lightbulb.implements(lightbulb.SlashCommand)
async def add(ctx):
    await ctx.respond(ctx.options.num1 + ctx.options.num2)
"""
bot.run()