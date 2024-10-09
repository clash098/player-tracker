import requests
import aiohttp
import asyncio
import random
import time
from config import Codes, SessionTickets, PaidWebhookURLs, EarlyWebhookURLs, FreeWebhookURLs, StartWebhookURL, AccountWebhookURLs, ConcatWebhookURLs
from discord_webhook import DiscordWebhook

# Role pings
Sweater_Ping = "1282213756222443530"
PaidTracker_Ping = "1281445589401206867"
FreeTracker_Ping = "1281517062564352051"
ConcatTracker_Ping = "1286123698964926505"

# Data
Code_Num = len(Codes)
SessionTicketNum = len(SessionTickets)
RunTimeNum = 2 * SessionTicketNum

# Sends Webhook to A Channel When It Finds A Specific Person
def ConcatWebhook(Person, Region, Code, Count, Actor, BoardPos):
    ConcatWebhookURL = random.choice(ConcatWebhookURLs)
    content = f"<@&{ConcatTracker_Ping}>"
    embeds = [{
        "title": f"🌙 Lucid Tracker Concat 🌙",
        "description": "",
        "color": 0x808080,
        "fields": [
           {"name": "", "value": f"", "inline": False},
           {"name": "👀 Person 👀", "value": f"```{Person}```", "inline": False},
           {"name": "🔢 Code 🔢", "value": f"```{Code}```", "inline": True},
           {"name": "🌐 Region 🌐", "value": f"```{Region}```", "inline": True},
           {"name": "🧑‍🧑‍🧒‍🧒 Player Count 🧑‍🧑‍🧒‍🧒", "value": f"```{Count}```", "inline": False},
           {"name": "🥇 Leader Board 🥇", "value": f"```{BoardPos}```", "inline": True},
           {"name": "🎭 Actor Number 🎭", "value": f"```{Actor}```", "inline": True},
      ],
        "footer": { "text": "Lucid Tracker </> Free + Non-Skidded"}
    }]
    data = {"content": content,"embeds": embeds}
    headers = {"Content-Type": "application/json"}

    response = requests.post(ConcatWebhookURL, json=data, headers=headers)
    response.raise_for_status()
    
    print(f"Found: {Cosmetic} in code -> {Code}{Region} with -> {Count} players")

# Sends Webhook to A Channel For Early Access
def EarlyWebhook(Cosmetic, Region, Code, Count, Actor, Concat, BoardPos, NormalCosmetics, Role):
    EarlyWebhookURL = random.choice(EarlyWebhookURLs)
    ConcatLength = len(Concat)
    # Stops Webhook From Including The Value 'Concat', When Its Value Exceeds 1500 Charecters
    if ConcatLength > 1500:
        ConcatValue = "Concat Is Too Long..."
    else:
        ConcatValue = Concat
    
    # Checks To See How Many '.'s Are In The Player's Data
    for ConcatSTR in Concat:
        if "." in ConcatSTR:
            NormalCosmetics += 1
    content = f"<@&{Role}>"
    embeds = [{
      "title": f"🌙 Lucid Tracker EA 🌙",
      "description": "",
      "color": 0x808080,
      "fields": [ 
           {"name": "👀 Found 👀", "value": f"```{Cosmetic}```", "inline": False},   
           {"name": "🔢 Code 🔢", "value": f"```{Code}```", "inline": True},
           {"name": "🌐 Region 🌐", "value": f"```{Region}```", "inline": True},
           {"name": "🧑‍🧑‍🧒‍🧒 Player Count 🧑‍🧑‍🧒‍🧒", "value": f"```{Count}```", "inline": False},
           {"name": "🟫 Normal Cosmetics 🟫", "value": f"```{NormalCosmetics}```", "inline": False},
           {"name": "🥇 Leader Board 🥇", "value": f"```{BoardPos}```", "inline": True},
           {"name": "🎭 Actor Number 🎭", "value": f"```{Actor}```", "inline": True},
           {"name": "🧵 Concat 🧵", "value": f"```{ConcatValue}```", "inline": False},
      ],
      "footer": {"text": "Lucid Tracker </> Free + Non-Skidded"}
  }]
    data = {"content": content,"embeds": embeds}
    headers = {"Content-Type": "application/json"}

    response = requests.post(PaidWebhookURL, json=data, headers=headers)
    response.raise_for_status()
    
    print(f"Found: {Cosmetic} in code -> {Code}{Region} with -> {Count} players")

# Sends Webhook to A Channel For Rarer Cosmetics
def MainWebhook(Cosmetic, Region, Code, Count, Actor, Concat, BoardPos, NormalCosmetics, Role):
    PaidWebhookURL = random.choice(PaidWebhookURLs)
    ConcatLength = len(Concat)
    # Stops Webhook From Including The Value 'Concat', When Its Value Exceeds 1500 Charecters
    if ConcatLength > 1500:
        ConcatValue = "Concat Is Too Long..."
    else:
        ConcatValue = Concat
    
    # Checks To See How Many '.'s Are In The Player's Data
    for ConcatSTR in Concat:
        if "." in ConcatSTR:
            NormalCosmetics += 1
    content = f"<@&{Role}>"
    embeds = [{
      "title": f"🌙 Lucid Tracker 🌙",
      "description": "",
      "color": 0x808080,
      "fields": [ 
           {"name": "👀 Found 👀", "value": f"```{Cosmetic}```", "inline": False},   
           {"name": "🔢 Code 🔢", "value": f"```{Code}```", "inline": True},
           {"name": "🌐 Region 🌐", "value": f"```{Region}```", "inline": True},
           {"name": "🧑‍🧑‍🧒‍🧒 Player Count 🧑‍🧑‍🧒‍🧒", "value": f"```{Count}```", "inline": False},
           {"name": "🟫 Normal Cosmetics 🟫", "value": f"```{NormalCosmetics}```", "inline": False},
           {"name": "🥇 Leader Board 🥇", "value": f"```{BoardPos}```", "inline": True},
           {"name": "🎭 Actor Number 🎭", "value": f"```{Actor}```", "inline": True},
           {"name": "🧵 Concat 🧵", "value": f"```{ConcatValue}```", "inline": False},
      ],
      "footer": {"text": "Lucid Tracker </> Free + Non-Skidded"}
  }]
    data = {"content": content,"embeds": embeds}
    headers = {"Content-Type": "application/json"}

    response = requests.post(PaidWebhookURL, json=data, headers=headers)
    response.raise_for_status()
    
    print(f"Found: {Cosmetic} in code -> {Code}{Region} with -> {Count} players")

# Sends Webhook to A Channel For Basic Cosmetics
def BasicWebhook(Cosmetic, Region, Code, Count, Actor, Concat, BoardPos, NormalCosmetics):
    FreeWebhookURL = random.choice(FreeWebhookURLs)
    ConcatLength = len(Concat)
    # Stops Webhook From Including The Value 'Concat', When Its Value Exceeds 1500 Charecters
    if ConcatLength > 1500:
        ConcatValue = "Concat Is Too Long..."
    else:
        ConcatValue = Concat
    
    # Checks To See How Many '.'s Are In The Player's Data
    for ConcatSTR in Concat:
        if "." in ConcatSTR:
            NormalCosmetics += 1
    content = f"<@&{FreeTracker_Ping}>"
    embeds = [{
      "title": f"🌙 Lucid Tracker Basic 🌙",
      "description": "",
      "color": 0x808080,
      "fields": [ 
           {"name": "👀 Found 👀", "value": f"```{Cosmetic}```", "inline": False},   
           {"name": "🔢 Code 🔢", "value": f"```{Code}```", "inline": True},
           {"name": "🌐 Region 🌐", "value": f"```{Region}```", "inline": True},
           {"name": "🧑‍🧑‍🧒‍🧒 Player Count 🧑‍🧑‍🧒‍🧒", "value": f"```{Count}```", "inline": False},
           {"name": "🟫 Normal Cosmetics 🟫", "value": f"```{NormalCosmetics}```", "inline": False},
           {"name": "🥇 Leader Board 🥇", "value": f"```{BoardPos}```", "inline": True},
           {"name": "🎭 Actor Number 🎭", "value": f"```{Actor}```", "inline": True},
           {"name": "🧵 Concat 🧵", "value": f"```{ConcatValue}```", "inline": False},
      ],
      "footer": {"text": "Lucid Tracker </> Free + Non-Skidded"}
  }]
    data = {"content": content,"embeds": embeds}
    headers = {"Content-Type": "application/json"}

    response = requests.post(FreeWebhookURL, json=data, headers=headers)
    response.raise_for_status()
    
    print(f"Found: {Cosmetic} in code -> {Code}{Region} with -> {Count} players")

def StartAccountInfo():
    for SessionTicket in SessionTickets:
        AccountWebhookURL = random.choice(AccountWebhookURLs)
        
        headers = {"X-Authorization": SessionTicket}
        json = {'InfoRequestParameters': {'GetUserAccountInfo': True}}
        request = requests.post(url=f"https://63fdd.playfabapi.com/Client/GetPlayerCombinedInfo",json=json,headers=headers)
        
        requestjson = request.json()
        status_code = requestjson['code']
        if status_code == 200:
            Last_Login = requestjson['data']['InfoResultPayload']['AccountInfo']['TitleInfo']['LastLogin']
            Is_Banned = requestjson['data']['InfoResultPayload']['AccountInfo']['TitleInfo']['isBanned']
            Steam_Id = requestjson['data']['InfoResultPayload']['AccountInfo']['SteamInfo']['SteamId']
            Steam_Name = requestjson['data']['InfoResultPayload']['AccountInfo']['SteamInfo']['SteamName']
        else:
            Last_Login = "N/A"
            Is_Banned = "N/A"
            Steam_Id = "N/A"
            Steam_Name = "N/A"
     
        content = f"<@&1293078334854402048>"
        embeds = [{
        "title": f"🌙 Lucid Tracker Accounts 🌙",
        "description": "",
        "color": 0x00FF00,
        "fields": [ 
            {"name": "", "value": "", "inline": False},
            {"name": "📅 Event 📅", "value": "Tracker Has Started", "inline": False},  
            {"name": "🎟️ Session Ticket", "value": f"{SessionTicket}", "inline": False},    
            {"name": "🏷️ Steam Name🏷️", "value": f"```{Steam_Name}```", "inline": False},
            {"name": "🛑 Is Banned 🛑", "value": f"```{Steam_Id}```", "inline": False},
            {"name": "🕕 Last Login 🕕", "value": f"```{Last_Login}```", "inline": False},
        ],
        "footer": {"text": "Lucid Tracker </> Free + Non-Skidded"}
    }]
        data = {"content": content,"embeds": embeds}
        headers = {"Content-Type": "application/json"}

        response = requests.post(AccountWebhookURL, json=data, headers=headers)
        response.raise_for_status()
        
def DeadAccountInfo(SessionTicket):
    AccountWebhookURL = random.choice(AccountWebhookURLs)        
     
    content = f"<@&1293078334854402048>"
    embeds = [{
        "title": f"🌙 Lucid Tracker Accounts 🌙",
        "description": "",
        "color": 0xFF0000,
        "fields": [ 
            {"name": "", "value": "", "inline": False},
            {"name": "📅 Event 📅", "value": "An Account Has Died!", "inline": False},  
            {"name": "🎟️ Session Ticket", "value": f"'''{SessionTicket}'''", "inline": False},    
            {"name": "🏷️ Steam Name🏷️", "value": f"```N/A```", "inline": False},
            {"name": "🛑 Is Banned 🛑", "value": f"```N/A```", "inline": False},
            {"name": "🕕 Last Login 🕕", "value": f"```N/A```", "inline": False},
        ],
        "footer": {"text": "Lucid Tracker </> Free + Non-Skidded"}
    }]
    data = {"content": content,"embeds": embeds}
    headers = {"Content-Type": "application/json"}

    response = requests.post(AccountWebhookURL, json=data, headers=headers)
    response.raise_for_status()

async def fetch(session, url, headers, json):
    async with session.post(url, json=json, headers=headers) as response:
        return await response.json(), response.status

async def process_code(session, Code, Region):
    # Define json
    SessionTicket = random.choice(SessionTickets)
    headers = {"X-Authorization": SessionTicket}
    groupid = Code + Region
    json = {"SharedGroupId": groupid}
    url = "https://63FDD.playfabapi.com/Client/GetSharedGroupData"
    try:
        requestjson, status_code = await fetch(session, url, headers, json)
        # If Post Request is Approved
        if status_code == 200:
            PlayerCount = len(requestjson['data']['Data'])
            response_data = requestjson['data']['Data']
            BoardPos = 0
            NormalCosmetics = 0
            # Checks Value For Each Account
            for key, value in response_data.items():
                BoardPos += 1
                items = str(value['Value'])
                # Concats
                # Owners
                if "LBAHF.LHAAB.LBAHC.LBAGT.LHABP.LBADK.LBAGP.LBAGN.LBAGO.LHABC.LMAII.LMAIL.LBAET.LHAAM.LMAGM.LBAEA.LHAAE.LFACS.LBADS.LHAAQ.LMABP.LHAAP.LBAAB.LHAAC.LFAAN.LBACQ.LMACT.LHACZ.LHAAL." in items:
                    ConcatWebhook("Clash Quest (Owner)", Region, Code, PlayerCount, key, BoardPos)
                if "LHAAC.LMAKZ.LMAFM.LFACW.LBAFL.LBAFN.LMAIL.LBAEU.LHAFJ.LSABF.LMAHU.LBAEO.LSABE.LHAFG.LMAHJ.LBAES.LFADK.LHACW.LFABN.LMAAK.LBADK.LHAAA.LBADC.LHAAP.LSAAU.LMADL.LFAAA.LBADB.LMADE.game-purchase-bundleLMAAR.LBACT.LFAAN.LBAAB.LHAAC." in items:
                    ConcatWebhook("Eclipse (Owner)",  Region, Code, PlayerCount, key, BoardPos)
                # Sweaters
                if "LBAHF.LBAGN.LHABP.LBACP.LHABR.LFABD.LBACQ.LMACT." in items:
                    ConcatWebhook("Unity (Known) | Sweater",  Region, Code, PlayerCount, key, BoardPos)
                if "LMAKY.LBAHS.LMALQ.LFAEH.LSABR.LMALP.LBAHT.LHAGT.LBAHP.LHAGR.LBADR.LFADZ.LBAGV.LBAGX.LBABH.LMAKJ.LFAEE.LSABQ.LMALI.LHAGS.LMAKT.LBAHF.LFAEF.LFAEG.LMALD.LMALA.LMAKX.LSABP.LBAHE.LFAED.LMALH.LSABN.LHAAB.LMAKE.LBAGT.LBAGP.LBAGN.LBAGO.LBAGN.LBAGO.LBAGP.LBAGN.LBAGO.LBAGP.LMAJR.LBAGP.LBAGO.LBAGN.LBAGE.LMAJA.LSABI.LBAGD.LMAIH.LMAII.LBAFI.LHAFK.LMAIG.LSABG.LBAFL.LMAIL.LBAFN.LBAFC.LMAHD.LMAHK.LBAEP.LBAET.LBAEO.LBADB.LMAHG.LBAEO.LBADB.LBAET.LBAET.LBAEO.LBADB.LBAET.LBAEO.LBADB.LBAET.LBAEO.LBADB.LBAAF.LFADL.LMAHT.LBAEV.LHAFI.LMAHV.LMAHX.LMAHW.LMAIA.LBAET.LMAHY.LMAHU.LBAEU.LSABF.LHAFJ.LFADK.LBAEO.LMAHI.LHAFF.LBAER.LSABE.LMAHJ.LHAFG.LBAES.LFAAF.LMAHB.LBAEL.LMAHE.LBAEJ.LHAFA.LHAFC.LBAEK.LBAEH.LFADH.LMAGV.LMAGW.LFADI.LHAEX.LMAGX.LMAGY.LFADF.LBAEG.LFADG.LHAEW.LMAGS.LMAGU.LBAEI.LHAEY.LBAEF.LHAEV.LMAGR.LSABD.LFADE.LBAEB.LBAEA.LHAEQ.LMAGJ.LMAGG.LMAGH.LBACD.LHAEO.LBADZ.LHAEN.LFADB.LMAGA.LFADA.LHAEP.LMAFY.LFADD.LMAFT.LMAFX.LBADY.LBADW.LBADX.LMAGC.LFADC.LMAFZ.LMAFW.LMAFV.LMAFU.LFACW.LMAFO.LFACQ.LHAEL.LFACU.LFACS.LMAFJ.LMAFM.LHAEM.LSABC.LMAFN.LBADV.LBADS.LBADQ.LMAFE.LMAFG.LFACO.LMAER.LBADL.LHAED.LBADJ.LSABA.LFACN.LMAEO.LHADY.LMADX.LMADZ.LMAEF.LMAEA.LMAEC.LMADY.LBABD.LBABB.LMAEN.LHAEA.LBADC.LFACK.LHAAG.LMADS.LMADN.LMADM.LBADA.LFACI.LHADU.LMADR.LMADU.LMADT.LSAAX.LHADV.LBACZ.LMADO.LSAAW.LHADS.LBACY.LSAAV.LFACG.LBACX.LHADR.LFACJ.LHADT.LMADP.LFACH.LSAAY.LMADV.LBADB.LMADK.LBABG.LMADJ.LHABM.LHABN.LHABO.LBACU.LHABI.LHABH.LHADQ.LHADP.LHADO.LBACV.LBACW.LHABL.LHABJ.LFACE.LHADN.LMADG.LMADF.LHABK.LSAAT.LMADI.LFACF.LSAAU.LMADL.LMACZ.LMADA.LMADD.LMADB.LMADH.LBACT.LMADC.LMADE.LFAAO.LBACP.LBACO.LMACO.LMACV.LMACW.LBACS.LHADM.LHABR.LFABD.LMACY.LHABQ.LBAAV.LBAAX.LBAAW.LBAAY.LBACR.LMACU.LSAAS.LMACX.LMACT.LBACQ.LBACA.LBACM.LBACN.LBACL.LMACM.LMACN.LHADL.LHADK.LHADJ.LHADI.LFACD.LFACC.LFACB.LMACR.LMACS.LMACP.LMACQ.LMAAQ.LMAAV.LMACL.LHADD.LBACJ.LFABY.LHADG.LBACI.LHADF.LSAAQ.LFABZ.LHADE.LSAAP.LBACH.LFACA.LBACK.LSAAR.LHADC.LHADH.LMACG.LMACH.LMACK.LMACB.LMACC.LMACI.LMACD.LMACJ.LFABX.LHACZ.LHACV.LMABP.LHACY.LMABY.LBACE.LBACF.LMABZ.LHADA.LSAAP2.LHACR.LHACS.LHACW.LMABQ.LMABU.LBACC.LMABR.LHACU.LSAAN.LMACA.LMABV.LBACG.LMABX.LMABW.LMABT.LMABS.LBACB.LHACT.LSAAO.LHACX.LFAAV.LBAAQ.LFAAW.LBAAP.LMABM.LMABH.LHACP.LHACQ.LFABW.LMABK.LMABL.LMABG.LMABE.LMABF.LMABI.LMABJ.LMABN.LMABO.LFAAP.LHAAU.LFAAQ.LSAAC.LHAAX.LFAAT.LBAAN.LSAAB.LBAAM.LHAAW.LFAAS.LFAAR.LBAAL.LHAAV.LSAAA.LSAAD.LHAAY.LFAAU.LBAAO.LMAAZ.LHACN.LSAAM.LBABZ.LBABW.LHACL.LSAAJ.LMAAY.LSAAL.LBABY.LHACO.LFABV.LFABU.LBABX.LHACM.LSAAI.LHACJ.LHACK.LMAAT.LMAAS.LMABD.LMAAR.LMAAP.LMAAX.LMABB.LMAAW.LSAAK.LHACI.LFABT.LBABV.LMABC.LMABA.LFABS.LFABR.LFABP.LFABQ.LHACF.LBABQ.LBABR.LBABT.LBABS.LSAAF.LHACH.LHACG.LBABU.LSAAG.LMAAU.LFABL.LFABO.LHACE.LMAAN.LMAAO.LFABN.LMAAM.LBABM.LFABI.LFAAL.LHACB.LHACD.LMAAI.LMAAG.LFABH.LMAAF.LMAAD.LBABK.LHACA.LMAAC.LBABI.LHABZ.LHABV.LHABX.LMAAB.LMAAA.LBABF.LHABW.LFABG.LFABF.LHAAJ.LHAAC.LBABA.LBAAZ.LBAAU.LFABB.LBAAT.LHABF.LHAAE.LFAAY.LHABG.LHABD.LFAAX.LSAAE.LBAAR.LHABE.LFABA.LBAAS.Early Access Supporter PackLHAAZ.LHAAT." in items:
                    ConcatWebhook("Gary (Known) | Sweater", Region, Code, PlayerCount, key, BoardPos)
                # FingerPainter
                if "LFAEH.LFADC.LMAKX.LBAHF.LHAGN.LBAGY.LBABP.LBADE.LMAAS.LHAAB.LHAAF.LHACZ.LMAJA.LSABI.LBAGD.LFACK.LBAFR.LFADO.LHAAQ.LMAIL.LBAFN.LMACN.LHABK.LHABH.LHABM.LBAAT.LMACR.LHACV.LMACJ.LFADK.game-purchase-bundleLBAER.LFAAT.LBAAN.LHAAX.LSAAC.LFADF.LMAGH.LFADE.LBAEB.LMAFO.LMAFN.LSABC.LHAEM.LBADV.LBADS.LFACW.LFACS.LMAAN.LMAAM.LFACN.LBADJ.LSABA.LMAEO.LBADQ.LFABI.LMAES.LMAAA.LBADB.LBACT.LHABR.LBACQ.LMACT.LHAAJ.LHABG.LMACK.LFAAK.LHAAS.LMACD.LSAAP.LHADE.LBACH.LFABZ.LFABX.LMACI.LMABQ.LMABT.LHACY.LHACW.LBACF.LMABZ.LSAAP2.LHADA.Early Access Supporter PackLMABO.LHAAD.LFAAF.LMAAZ.LHABP.LFAAL.LHAAL.LHAAM.LHAAP.LFABN.LFAAN.LBAAB.LHAAC.LHAAE." in items:
                    ConcatWebhook("Alec Vr (Know)", Region, Code, PlayerCount, key, BoardPos)
                # Stick
                if "LBAAK." in items:
                    EarlyWebhook('🪃 Stick 🪃', Region, Code, PlayerCount, key, items, BoardPos, NormalCosmetics, PaidTracker_Ping)
                    time.sleep(15)
                    MainWebhook('🪃 Stick 🪃', Region, Code, PlayerCount, key, items, BoardPos, NormalCosmetics, PaidTracker_Ping)
                # Finger Painter
                if "LBADE." in items:
                    EarlyWebhook('🎨 Finger Painter 🎨', Region, Code, PlayerCount, key, items, BoardPos, NormalCosmetics, PaidTracker_Ping)
                    time.sleep(15)
                    MainWebhook('🎨 Finger Painter 🎨', Region, Code, PlayerCount, key, items, BoardPos, NormalCosmetics, PaidTracker_Ping)
                # Illustrator Badge
                if "LBAGS." in items:
                    EarlyWebhook('🎨 Illustrator Badge 🎨', Region, Code, PlayerCount, key, items, BoardPos, NormalCosmetics, PaidTracker_Ping)
                    time.sleep(15)
                    MainWebhook('🎨 Illustrator Badge 🎨', Region, Code, PlayerCount, key, items, BoardPos, NormalCosmetics, PaidTracker_Ping)
                # Admin Badge
                if "LBAAD." in items:
                    EarlyWebhook('👨‍💼 Admin Badge 👨‍💼', Region, Code, PlayerCount, key, items, BoardPos, NormalCosmetics, PaidTracker_Ping)
                    time.sleep(15)
                    MainWebhook('👨‍💼 Admin Badge 👨‍💼', Region, Code, PlayerCount, key, items, BoardPos, NormalCosmetics, PaidTracker_Ping)
                # Unreleased Sweater
                if "LBACP." in items:
                    MainWebhook('👕 Unreleased Sweater 👕', Region, Code, PlayerCount, key, items, BoardPos, NormalCosmetics, Sweater_Ping)
                # Monkey Plush
                if "LBADB." in items:
                    BasicWebhook('🧸 Monkey Plush 🧸', Region, Code, PlayerCount, key, items, BoardPos, NormalCosmetics)
                # Early Access
                if "LBAAE." in items:
                    BasicWebhook('🔓 Early Access 🔓', Region, Code, PlayerCount, key, items, BoardPos, NormalCosmetics)
                # GT1 Badge
                if "LBAAZ." in items:
                    BasicWebhook('1️⃣ GT1 Badge 1️⃣', Region, Code, PlayerCount, key, items, BoardPos, NormalCosmetics)
                # We Are Vr Headset
                if "LFADE." in items:
                    BasicWebhook('🥽 We Are Vr Headset 🥽', Region, Code, PlayerCount, key, items, BoardPos, NormalCosmetics)
                # We Are Vr Badge
                if "LBAEB." in items:
                    BasicWebhook('🥽 We Are Vr Badge 🥽', Region, Code, PlayerCount, key, items, BoardPos, NormalCosmetics)
                # In Game Purchase
                if "game-purchase-bundle" in items:
                    BasicWebhook('💰 Ingame Purchase 💰', Region, Code, PlayerCount, key, items, BoardPos, NormalCosmetics)
                if PlayerCount == 1:
                    BasicWebhook('👻 Alone Player 👻', Region, Code, PlayerCount, key, items, BoardPos, NormalCosmetics)
            else:
                print(f"Checked {Code} -> {Region} -> {status_code} | Empty")
        
        # Ratelimited
        elif status_code == 429:
            throttle_time = requestjson['retryAfterSeconds']
            await asyncio.sleep(throttle_time)  
        
        # Invalid Session Ticket
        elif status_code == 401:
            DeadAccountInfo(SessionTicket)
            print(f"A Session Ticket Has Been Removed, Check The Logs On The Discord!!!")   
        
        # Banned Account
        elif status_code == 403:
            DeadAccountInfo(SessionTicket)
            print(f"A Session Ticket Has Been Removed, Check The Logs On The Discord!!!")       

    # Error Proccesing Code
    except Exception as e:
        print(f"Error processing {Code} -> {Region}: {e}")

# Uses Multi Threading To Increase Speed A Lot
async def main():
    async with aiohttp.ClientSession() as session:
        while True:
            tasks = []
            for Code in Codes:
                for Region in ['EU', 'USW', 'US']:
                    tasks.append(process_code(session, Code, Region))
            await asyncio.gather(*tasks)


def Start():
    StartAccountInfo()
    content = "<@&1281445589401206867> + <@&1281517062564352051>"
    embeds = [{
    "title": f"🌙 Lucid Tracker Started 🌙",
    "description": "",
    "color": 0x808080,
    "fields": [
        {"name": "", "value": "", "inline": False},
        {"name": "🔢 Number Of Codes 🔢", "value": f"```{len(Codes)}```", "inline": False},
        {"name": "🔢 Number Of Session tickets 🔢", "value": f"```{len(SessionTickets)}```", "inline": False},
        {"name": "🧍‍♂️ Person Running 🧍‍♂️", "value": f"```PI-TRACKER (Beta)```", "inline": False},
        ],
    }]
    
    print("✨ Lucid Tracker Started... ✨")
    print("")
    print("Stats:")
    print(f"Codes: {Code_Num}")
    print(f"Session tickets: {SessionTicketNum}")
    print("")
    print(f"The script will run for {RunTimeNum} seconds then stop for 100 seconds to avoid ratelimiting.")
    print("")
    print("Starting in 3 seconds...")
    time.sleep(3)
    
    webhook = DiscordWebhook(url=StartWebhookURL, embeds=embeds)
    webhook.execute()
    
    asyncio.run(main())
Start() 
