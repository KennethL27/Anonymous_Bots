# Anonymous Bots

<table>
<tr>
<td>
  These Anonymous Bots are created specifically for University of Calfornia, Santa Barbara Physics Discord. The intent of these Bots are meant to create a welcoming enviornment and a platform for anyone to ask a question or to respond with anonymity. These Anonymous Bots are made by using <a href="https://discordpy.readthedocs.io/en/latest/">Discord's Python API</a>. As the UCSB Physics Discord Community continues to grow, these Anonymous Bots will become more user friendly. Currently UCSB Physics Discord has Anonymous Hotline (Rant Channel), Anonymous Spam (Spam Channel), Anonymous Advising (Advising Channel), and Anonymous User (used for Townhall and AMA Event).
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
1. Head over to the Developer Portal and sign in with your discord account.
2. Once you successfully sign in go to the "Applications" tab and create a new Application with the "New Application" button on the top right.
3. Create a Name for this new application (or bot) and hit the "Create" button.
4. On the left side cick on "Bot" and on the right side use the "Add Bot" to create the bot. You will need to comfirm by clicking  on "Yes, do it!"
5. You have now created a Bot! Copy the token (next to the Bot's icon) and use it in your code for the bot to run. *Note: Do not give anyone your bot's token! In case the token is shared, use the "Regenerate" button to make sure you Bot is safe.*
6. Before you can actually see you go live, you must invite your bot to a server. On the left side go to "OAuth2"
7. In the "OAuth2" tab, check mark "bot" in the middle column. You will now see more options at the bottom, these options are to grant your bot's permission. For testing sake I suggest check marking "Administrator". This grants all premission to the bot, and most of these permissions can be changed within the server. 
8. With the permissons selected you can copy the link above the permission option and past it in a new tab. Select a server you want to bring the bot into, you must have the permission to manage the server in order to introduce a bot. If you dont have a server with this permission I suggest creating a personal server. 
9. Once you have the server selected, click "Authorize" and begin coding!

### Discord.py

__Windows/Linux__

`pip install discord.py`
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
