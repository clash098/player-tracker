from colorama import Fore, init
import requests
import random
import time

TrackerName = ""

Cosmetics = [
    {
    "CosmeticName":"Stick",
    "CosmeticId":"LBAAK." 
    },
    {
    "CosmeticName":"Admin Badge",
    "CosmeticId":"LBAAD." 
    },
    {
    "CosmeticName":"Illustrator Badge",
    "CosmeticId":"LBAGS." 
    },
    {
    "CosmeticName":"Finger Painter",
    "CosmeticId":"LBADE." 
    },
    {
    "CosmeticName":"Unreleased Sweater",
    "CosmeticId":"LBACP." 
    },
]

Colors = [
    { 
    "ColorName": "Red",
    "ColorHex": 0xff0000,
    "Activated": True,
    },
    { 
    "ColorName": "Green",
    "ColorHex": 0x00ff00,
    "Activated": True,
    },
    { 
    "ColorName": "Blue",
    "ColorHex": 0x0000ff,
    "Activated": True,
    },
    { 
    "ColorName": "Black",
    "ColorHex": 0x000000,
    "Activated": True,
    },
    { 
    "ColorName": "White",
    "ColorHex": 0xffffff,
    "Activated": True,
    },
    { 
    "ColorName": "Grey",
    "ColorHex": 0x818181,
    "Activated": True,
    },
    
]

SessionTickets = [
    "",
]

WebhookURL = ""
StatusWebhookURL = ""

Codes = [
    "MINIGAMES",
]


def Webhook(item, code, region, player_count, board_position, actor, rawconcat):
    if len(rawconcat) >= 1000:
        concat = "Concat is too long to display in the embed..."
    else:
        concat = rawconcat

    for ColorData in Colors:
        if ColorData['Activated'] is True:
            Color = ColorData['ColorHex']
    
    if not Color:
        Color = 0x000000
        
    content = f"<@&1292686258937659482>"
    embeds = [{
        "title":
        f"🐵 {TrackerName} Tracker 🐵",
        "description":
        "",
        "color":
        Color,
        "fields": [
            {"name": "Found","value": f"```{item}```","inline": False},
            {"name": "Code","value": f"```{code}```","inline": False},
            {"name": "Region","value": f"```{region}```","inline": False},
            {"name": "Player Count","value": f"```{player_count}```","inline": False},
            {"name": "Leaderboard Pos","value": f"```{board_position}```","inline": False},
            {"name": "Actor Number","value": f"```{actor}```","inline": False},
            {"name": "Concat","value": f"```{concat}```","inline": False},
        ],   "footer": {"text": f"{TrackerName} | Src By Clash"
        }
    }]

    data = {"content": content, "embeds": embeds}
    headers = {"Content-Type": "application/json"}

    response = requests.post(WebhookURL, json=data, headers=headers)
    response.raise_for_status()

def StartWebhook():
    for ColorData in Colors:
        if ColorData['Activated'] is True:
            Color = ColorData['ColorHex']
    
    if not Color:
        Color = 0x000000
        
    content = f"<@&1292686258937659482>"
    embeds = [{
        "title":
        f"🐵 {TrackerName} Started 🐵",
        "description":
        "",
        "color":
        Color,
        "fields": [
            {"name": "Person Running","value": f"```Pulse```","inline": False},
            {"name": "Codes","value": f"```{len(Codes)}```","inline": False},
            {"name": "Tickets","value": f"```{len(SessionTickets)}```","inline": False},
        ],   "footer": {"text": "Pulse Tracker | Src By Clash | gg/lucid-tracker"
        }
    }]

    data = {"content": content, "embeds": embeds}
    headers = {"Content-Type": "application/json"}

    response = requests.post(StatusWebhookURL, json=data, headers=headers)
    response.raise_for_status()

def CheckCode():
    for code in Codes:
        SessionTicket = random.choice(SessionTickets)
        for region in ['EU', 'US', 'USW']:
            headers = {"X-Authorization": SessionTicket}
            json = {"SharedGroupId": code + region}

            request = requests.post(url="https://63FDD.playfabapi.com/Client/GetSharedGroupData",headers=headers,json=json)
            requestjson = request.json()

            if requestjson['code'] == 200:

                room_data = requestjson['data']['Data']
                player_count = len(room_data)
                board_position = 0

                for key, value in room_data.items():
                    board_position += 1
                    concat = value['Value']
                    
                    for CosmeticData in Cosmetics:
                        if CosmeticData['CosmeticId'] in value['Value']:
                            Webhook(CosmeticData['CosmeticName'], code, region, player_count, board_position, key, concat)
                            
                            print(Fore.GREEN + f"Found {CosmeticData['CosmeticName']} in code: {code}")
                        
                print(Fore.LIGHTBLACK_EX + f"Checked Room {code}{region} with {player_count} players.")

            elif requestjson['code'] == 429:
                throttle_time = requestjson['retryAfterSeconds']
                print(Fore.RED + f"Ratelimited - Now sleeping for {throttle_time}")
                time.sleep(throttle_time)

def main():
    StartWebhook()
    while True:
        CheckCode()

main()
