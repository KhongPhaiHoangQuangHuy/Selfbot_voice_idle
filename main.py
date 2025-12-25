import os
import sys
import shyurer
import json
import time
import requests
from websocket import create_connection
from dotenv import load_dotenv

load_dotenv()

status = os.getenv("STATUS")
custom_status = os.getenv("CUSTOM_STATUS")

GUILD_ID = int(os.getenv("GUILD_ID"))
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))
SELF_MUTE = os.getenv("SELF_MUTE", "false").lower() == "true"
SELF_DEAF = os.getenv("SELF_DEAF", "false").lower() == "true"

usertoken = os.getenv("DISCORD_TOKEN")
if not usertoken:
  print("[ERROR] Please add a token inside Secrets.")
  sys.exit()

headers = {"Authorization": usertoken, "Content-Type": "application/json"}

validate = requests.get('https://canary.discordapp.com/api/v9/users/@me', headers=headers)
if validate.status_code != 200:
  print("[ERROR] Your token might be invalid. Please check it again.")
  sys.exit()

userinfo = requests.get('https://canary.discordapp.com/api/v9/users/@me', headers=headers).json()
username = userinfo["username"]
discriminator = userinfo["discriminator"]
userid = userinfo["id"]

def joiner(token, status, custom_status=""):
    ws = create_connection('wss://gateway.discord.gg/?v=9&encoding=json')
    start = json.loads(ws.recv())
    heartbeat = start['d']['heartbeat_interval']
    
    presence = {
        "status": status,
        "afk": False
    }
    
    if custom_status:
        presence["activities"] = [
            {
                "type": 4,
                "name": "Custom Status",
                "state": custom_status,
                "created_at": int(time.time() * 1000)
            }
        ]
    
    auth = {"op": 2,"d": {"token": token,"properties": {"$os": "Windows 10","$browser": "Google Chrome","$device": "Windows"},"presence": presence},"s": None,"t": None}
    vc = {"op": 4,"d": {"guild_id": GUILD_ID,"channel_id": CHANNEL_ID,"self_mute": SELF_MUTE,"self_deaf": SELF_DEAF}}
    ws.send(json.dumps(auth))
    ws.send(json.dumps(vc))
    time.sleep(heartbeat / 1000)
    ws.send(json.dumps({"op": 1,"d": None}))

def run_joiner():
  guild_resp = requests.get(f'https://canary.discordapp.com/api/v9/guilds/{GUILD_ID}', headers=headers)
  guild_name = guild_resp.json().get("name", "Unknown Guild") if guild_resp.status_code == 200 else "Unknown Guild"
  
  channel_resp = requests.get(f'https://canary.discordapp.com/api/v9/channels/{CHANNEL_ID}', headers=headers)
  channel_name = channel_resp.json().get("name", "Unknown Channel") if channel_resp.status_code == 200 else "Unknown Channel"
  
  print(f"Logged in as {username}#{discriminator} ({userid}).")
  print(f"Server: {guild_name} | Channel: {channel_name}")
  print(f"Custom status: {custom_status}")
  try:
    while True:
      joiner(usertoken, status, custom_status)
      time.sleep(30)
  except KeyboardInterrupt:
    print("\nProgram stopped.")
    sys.exit()

run_joiner()
