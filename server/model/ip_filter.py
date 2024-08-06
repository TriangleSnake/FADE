import requests
from tqdm import tqdm
import random
with open ("server/model/proxy.txt", "r") as f:
    proxies = f.read().splitlines()

url = "https://www.instagram.com/api/v1/users/web_profile_info/?username=nasa"

headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 105.0.0.11.118 (iPhone11,8; iOS 12_3_1; en_US; en-US; scale=2.00; 828x1792; 165586599)'
}
counter = 0
while True:
    proxy = random.choice(proxies)
    try:
        r = requests.get(url,headers=headers,proxies={"https": proxy},timeout=3)
        print("getting user info via",proxy,"status code:",r.status_code)
        if r.status_code == 200:
            counter += 1
            print(counter)
            with open("server/model/new_proxy.txt", "a") as f:
                f.write(proxy + "\n")
            proxies.remove(proxy)
            if counter == 20:
                break
    except Exception as e:
        print("getting user info via",proxy,"falied:",e)
        proxies.remove(proxy)