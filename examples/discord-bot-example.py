import discord, asyncio
from madlibspy import Madlibs as ml
commands = discord.ext.commands

class Madlibs(commands.Cog):
  def __init__(self, bot)
    self.bot = bot
    self.ongoing = []

  @commands.command()
  async def madlibs(self, ctx):
    if ctx.author in self.ongoing: return
    self.ongoing.append(ctx.author)
    msg = await ctx.send("Fetching data from the API...")
    data = ml.get()
    answers = []
    def check(message):
      return message.author == ctx.author and message.channel == ctx.channel and len(message.content) != 0
    for i in data["variables"]:
      try:
        await msg.edit(content=f"Enter a **{i}**")
        answer = await self.bot.wait_for('message', check=check, timeout=120)
        answers.append(answer.content)
        await answer.delete()
      except asyncio.TimeoutError:
        self.ongoing.remove(ctx.author)
        return await ctx.send("Madlibs timed out!")
    self.ongoing.remove(ctx.author)
    return await ctx.send(embed=discord.Embed(
      title=data['title'],
      description=ml.convert(answers, data['questions'], data['text']),
      color=discord.Color.green()
    )
    .set_footer(text="Made using MadLibsPy"))

def setup(bot):
  bot.add_cog(Madlibs(bot))