import discord
import os
from dotenv import load_dotenv
from Discord.Coin.keep_alive import keep_alive
import Discord.Coin.rpc as rpc
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

load_dotenv()


RPCUSER = os.getenv('RPCUSER')
RPCPASSWORD = os.getenv('RPCPASSWORD')
RPCPORT = os.getenv('RPCPORT')


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
# client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print("Bot is now ready to use!!!")
    print("--------------------------")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content
    rpc_connection = AuthServiceProxy(f"http://{RPCUSER}:{RPCPASSWORD}@127.0.0.1:{RPCPORT}")
    if msg.startswith('$qoute'):
        await message.channel.send("Hiii!!!!!!!")

client.run(os.getenv('TOKEN'))