import requests
import random

def read_from_file(filename):
    with open(filename, 'r') as file:
        return file.read().strip().split('\n')

def send_request_with_proxy(token, proxy, cookie, xsp, refer, messageid, guildid):
    url = "https://discord.com/api/v9/channels/" + guildid + "/messages/" + messageid + "/reactions/%E2%9C%85/%40me?location=Message&type=0"
    headers = {
    "accept": "*/*",
    "accept-language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
    "authorization": token,
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "x-debug-options": "bugReporterEnabled",
    "x-discord-locale": "de",
    "x-discord-timezone": "Europe/Berlin",
    "x-super-properties": xsp,
    "cookie": cookie,
    "Referer": refer,
    "Referrer-Policy": "strict-origin-when-cross-origin"
  }
    try:
        response = requests.get(url, headers=headers, proxies=proxy)
        print(f"Token: {token}, Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Token: {token}, Error: {e}")

def main():
    token_file = input("Token file>>>")
    proxy_file = input("Proxy file>>>")
    guildiddsc = input("GuildID>>>")
    msgiddsc = input("MessageID>>>")
    cookiedsc = input("cookie>>>")
    xspdsc = input("XSP>>>")
    referdsc = input("Referer>>>")
    tokens = read_from_file(token_file)
    proxies = read_from_file(proxy_file)

    proxy_list = [proxy.strip() for proxy in proxies]

    for token in tokens:
        proxy = random.choice(proxies)
        send_request_with_proxy(token, proxy, cookiedsc, xspdsc, referdsc, msgiddsc, guildiddsc)

if __name__ == "__main__":
    main()
