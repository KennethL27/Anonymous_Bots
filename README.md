# Anonymous Bots

<table>
<tr>
<td>
  These Anonymous Bots are created specifically for University of Calfornia, Santa Barbara Physics Discord. The intent of these Bots are meant to create a welcoming enviornment and a platform for anyone to ask a question or to respond with anonymity. These Anonymous Bots are made by using <a href="https://discordpy.readthedocs.io/en/latest/">Discord's Python API</a>. As the UCSB Physics Discord Community continues to grow, these Anonymous Bots will become more user friendly.
</td>
</tr>
</table>

___

## Main Anonymous (Alpha)
*Version 1.2.0*

### Features

* Provides Users (with the proper role) with the ability to post messages anonymously with a command. *Semi Anonymous to the community*
* Allows Users (with the proper role) to Direct Message (DM) the bot and have the message be sent directly to the channel. (ie. Rant Anonymous Bot will take DMs and post them anonymously to the Rant Channel.) *Completely Anonymous to the community*
* Provides the individual that runs this code the anonymous messages and their corresponding author's username. This feature is intented to not be looked at, only in serious cases where a user breaks a rule with the Anonymous Bot.
* Provides the amount of time the Bot has been running for. 

___

## Anonymous (Beta)
*Version 2.0.0*

### Features
* All Alpha fetures are provided in the Beta

___

## AMA Anonymous 
*Version 1.0.0*

### Features
* All Alpha features are provided in this Anonymous Bot
* Generates a random 4 digit number and assignes it to a user. This allows other users to understand if the same anonymous user is continuing to message. 

___

## Installation 
*Meant for the Beta Version*

### Discord Bots

In order to run Discord Bots you must first create a [Developer Portal](https://discord.com/login?redirect_to=%2Fdevelopers%2Fapplications) and create one. 

___

## Usage
Prerequisites: Python 3.7, Discord.py 1.5.1

For the most basic Discord Bot the following is the base code:

```python
import discord

client = discord.Bot(command_prefix = "!")

@client.event
async def on_ready():
	print('Bot is online')

client.run('Token')
```

Once this simple code has been working correcly with your own bot setup, you may now use functions from Broida(beta).py

___

## Contribution

All of the contribution made so far have been done by Kenneth Lara. Input to form different systems are a collaborative effor made by the staff of UCSB Physics Discord and by the community itself.

## Message from the Founder of UCSB Physics Discord and Broida

I would like to thank all of those who have encouraged me to continuly purseue this avenue. I am more than thankful for all the support and suggestions that the Physics Community has given to me at UCSB. Thank you Thank you Thank you!
