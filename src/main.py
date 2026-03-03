from random import randint
from os import getenv

import discord
import roles
import playerList

bot = discord.Bot()

#Role IDs
gameMaster = 1432880451604709547
alive = 1432889281231323268
dead = 1432883624394362923

#Channel IDs
death_announcements = 1432858492842283089



MaxApoc = randint(0, 4)
MaxCoven = randint(2, 4)
MaxNeutral = len(playerList.playerList) - MaxApoc - MaxCoven - randint(5, len(
    playerList.playerList) - MaxCoven - MaxApoc + 5)


def addPlayerToGame(player):
    playerList.playerList.append(player)

def StartNewGame():
    Coven = roles.Coven()
    CovenCount = 0

    Apoc = roles.Apoc()
    ApocCount = 0

    Neutral = roles.Neutral()
    NeutralCount = 0

    Town = roles.Town()

    while playerList.playerList:

        playerfr = playerList.playerList[randint(0, len(playerList.playerList) - 1)]

        if CovenCount < MaxCoven:
            Coven.select_role(playerfr)
            playerList.playerList.remove(playerfr)
            CovenCount = CovenCount + 1

        elif ApocCount < MaxApoc:
            Apoc.select_role(playerfr)
            playerList.playerList.remove(playerfr)
            ApocCount = ApocCount + 1

        elif NeutralCount < MaxNeutral:
            Neutral.select_role(playerfr)
            playerList.playerList.remove(playerfr)
            NeutralCount = NeutralCount + 1

        else:
            Town.select_role(playerfr)
            playerList.playerList.remove(playerfr)


@bot.slash_command(name="join_game", description="adds you to queue for next game")
async def join_queue(ctx):
    addPlayerToGame(ctx.author.user)
    await ctx.respond("You have been added to the next game!", ephemeral=True)

@bot.slash_command(name="start-game", description="starts the Town of Salem game!")
async def start_game(ctx):
    member = ctx.guild.get_member(ctx.author.id)
    if any(role.id == gameMaster for role in member.roles):
        StartNewGame()
        await ctx.respond("Starting new game!", ephemeral=True)
    else:
        await ctx.respond("You do not have permission to start a new game!", ephemeral=True)


@bot.slash_command(name="kill-player", description="kills a player for real for real")
async def kill_player(ctx, player: discord.Option(discord.User)):
    member = ctx.guild.get_member(ctx.author.id)
    if any(role.id == gameMaster for role in member.roles):
        channel = bot.fetch_channel(death_announcements)
        channel.send(f"# {player.mention}")
        await player.remove_roles(ctx.guild.fetch_roles(alive))
        await player.add_roles(ctx.guild.fetch_roles(dead))
        await ctx.respond("Killed player!")
    else:
        ctx.respond("Yeah no buddy you dont have perms for ts :pray:")




bot.run(getenv("TOKEN"))

