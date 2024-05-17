
# Discord Truth or Dare Bl Tounsi Bot
<img src='https://play-lh.googleusercontent.com/uT1an7CUDZZhYHoxjTHUCfdyQwshjWzwW_Q9YyZmHiJWFSxidozf1vkvGP9UYhZn7Ag' align='right' width="20%">
<br>
A simple Discord bot that generates random Truth or Dare questions in tunisian for you and your friends to enjoy action/verite bil tounsi!
Radom Truth or Dare questions in tunisian

## Features

- **[Generates random Truth or Dare questions](#usage)**
- **[Customizable questions](#truth-and-dare-questions)**
- **[Error handling](#error-handling)**
- **[Installation](#installation)**
- **[Install the required packages](#required-packages)**
- **[Discord Side](#discord-side)**
- **[Set up Heruko](#finale)**

---

## Usage

- The command [prefix](#initialize-the-bot-with-intents) is **"~"**
>
> [!TIP]
>* To start a game, type **[~help](#bot-events-and-commands)** in a channel<br>
>    Type **[~truth](#truths)** to receive a Truth question<br>
>    Type **[~dare](#dares)** to receive a Dare question<br>

- Customization
    You can customize the Truth and Dare questions by modifying the truths and dares lists in the code.

### Initialize the bot with intents
```python
intents = discord.Intents.default() intents.message_content = True bot = commands.Bot(command_prefix='~', intents=intents)
```

### Truth and Dare questions
##### truths
<p align='left'>
[
"Chkoun foulena?",
"Chkoun akther wa7da ta7ki m3aha?",
"Chloun 9alsounik?",
"Taw inti rajil?",
"Chkoun il crush mte3ik?",
]
</p>

##### dares
<p align='left'>
[
"Do 10 pushups.",
"9oum 3ayit mich yo9tlouni",
"8ani 8neya fi vocal ou ib3athha le5ir we7id 7kit m3ah 3la discord",
"Do 30 pushups",
"Hbat story fiha inti 7ra9t",
]
</p>

### Bot events and commands
<img src='https://i.postimg.cc/rwWCPsxq/8d7be7cd-7a75-4063-aa3a-789153640a67.jpg' width='30%' align='right'>

```python
@bot.event async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')

@bot.command(name='truth') async def truth(ctx):
    truth_question = random.choice(truths)
        await ctx.send({user},' ',truth_question)

@bot.command(name='dare') async def dare(ctx):
    dare_question = random.choice(dares)
        await ctx.send({user},' ',dare_question)

@bot.command(name='help')
    async def truth_or_dare(ctx):
        await ctx.send("{user} Type 'truth' or 'dare' to receive a challenge!") def check(m):
            return m.author == ctx.author and m.channel == ctx.channel and m.content.lower() in ['truth', 'dare']
            try: msg = await bot.wait_for('message', check=check, timeout=30) if msg.content.lower() == 'truth':
                await truth(ctx)
            elif msg.content.lower() == 'dare':
                await dare(ctx) 
            except asyncio.TimeoutError: # type: ignore
                await ctx.send("{user} You took too long to respond! Please try again 😇.")
```

### Error handling
The bot includes basic error handling for common errors such as invalid commands and timeouts.
```Python
@bot.event async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Invalid command. Please try again.")
    else:
        await ctx.send("An error occurred. Please try again later.") print(error)
```
### Installation
> [!IMPORTANT]
> Install [Python](https://www.python.org)

### Required Packages
>
> [!WARNING]
> #### Without the necessary packages and libraries nothing will work
> Python libraries [pip/npm/etc]

> [!CAUTION]
> In your Teminal/Console
> ```pip install discord.py```<br>
> ```pip install asyncio ```

### Discord side

#### The necessary :
1. Create a new bot on the [Discord Developer Portal](https://discord.com/login?redirect_to=%2Fdevelopers%2Fapplications)
2. Copy the bot token and replace `YOUR_BOT_TOKEN` in the code with it
<img src="https://www.online-tech-tips.com/wp-content/uploads/2022/01/image-143.png" width="50%" align="center">
3. Invite the bot to your server using the generated invite link

### Run the bot with the token
```Python
bot.run('YOUR_BOT_TOKEN') import discord from discord.ext
import commands import random
```

### Finale

#### Install the Heroku CLI

<img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSeXGnBOk0xEoebyUTMjv-IGKGffCQ5xJ2tMA&s' align='right'>

Go to the Heroku [CLI installation page](https://devcenter.heroku.com/articles/heroku-cli).
Download the installer for your Device.
#### Log in to Heroku:
```bash
heroku login
```
This will open a browser window asking you to log in to your Heroku account.
#### Heroku Remote:
In your project directory, set the Heroku remote repository:

heroku git:remote -a YOU-APP-NAME
#### Stage Your Changes:

git add .
#### Commit Your Changes:

git commit -m "Initial commit"
#### Push to Heroku:

git push heroku master
Set Environment Variables on Heroku

#### Set Your Bot Token:
heroku config:set DISCORD_TOKEN=your-bot-token

**Code**:

```bash
    git init
    heroku git:remote -a your-heroku-app-name
    git add .
    git commit -m "Initial commit"
    git push heroku master
```

---
##### Do you want me to make it in js next time ?

License
This project is licensed under the MIT License - see the LICENSE.md file for details.
