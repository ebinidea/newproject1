import discord
from discord.ext import commands

from util.plugins.common import *

def selfbotspammer():
    token = input("[>>>] Token: ")
    validateToken(token)
    print("\nWrite '!spam (message) (Number)' in one of your DMs to delete your messages")

    intents = discord.Intents.all()

    bot = commands.Bot(command_prefix="!", self_bot=True, intents=intents)
    bot.remove_command("help")

    @bot.event
    async def on_ready():
        print("Bot is ready")

    @bot.command()
    async def clear(ctx, limit: int = None):
        passed = 0
        failed = 0
        async for msg in ctx.message.channel.history(limit=limit):
            if msg.author.id == ctx.bot.user.id:
                try:
                    await msg.delete()
                    passed += 1
                except:
                    failed += 1
        print(f"\nRemoved {passed} messages with {failed} fails")
        input("\nPress ENTER to exit")

    @bot.command()
    async def spam(ctx, text: str, times: int):
        await ctx.message.delete()  # Delete the invoking message
        for _ in range(times):
            try:
                await ctx.send(text)
            except discord.HTTPException:
                print("Rate limited.")
                pass

    bot.run(token, bot=False)