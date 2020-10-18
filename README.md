# HypixelBot
A Hypixel Discord Bot made purely for displaying Hypixel statistics.

To run this bot, change `<TOKEN>` in botconfig.ini to your Discord Bot Token, which can be retrieved from your Discord Developer Portal, and change `<API KEY>`, also in botconfig.ini to your Hypixel API Key, which can be created by connecting to mc.hypixel.net and running the `/api new` command.

This bot retrieves statistics from the official public [Hypixel API](https://api.hypixel.net). Documentation for the API can be found at [https://github.com/HypixelDev/PublicAPI/tree/master/Documentation](https://github.com/HypixelDev/PublicAPI/tree/master/Documentation)

Thanks to [@DimBis](https://github.com/DimBis) for helping me with this project.

## Requirements
mojang - `python -m pip install mojang`

requests - `pip install requests`

discord.py - `py -3 -m pip install -U discord.py`

## Commands
`h!help` - A list of commands.

`h!player <playername>` - Info on a specified player.

`h!bedwars <playername>` - Bedwars Stats for a specified player.

`h!skywars <playername>` - Skywars Stats for a specified player.

`h!guild <guild>` - Information on a specified guild.

## Invite
To add this bot to your server, click [here](https://discord.com/api/oauth2/authorize?client_id=764677833820995605&permissions=0&scope=bot).
