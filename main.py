import discord, os, keep_alive, asyncio, datetime, pytz


from discord.ext import tasks, commands

client = commands.Bot(
  command_prefix=':',
  self_bot=True
)



@client.event
async def on_connect():
  await client.change_presence(activity = discord.Streaming(name = "24/7 Online ┊ 7:00 - 23:00 Online ┊ Fast Respond ┊ Mager Bjir. ┊ 3 Minggu Puasa Ges.", url = "https://www.twitch.tv/tukang_turu"))


keep_alive.keep_alive()
client.run(os.getenv("TOKEN"), bot=False)
