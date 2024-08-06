import requests
import re
import hashlib
import random

with open ("server/model/new_proxy.txt", "r") as f:
    proxies = f.read().splitlines()

def profile_pic(url:str):
    sha1 = hashlib.sha1()
    sha1.update(requests.get(url).content)
    if sha1.hexdigest() == "f205a4666738dc766a820307348d9f8926ee8305":
        return 0
    else :
        return 1

def numDivLen(username:str):
    if username == "":
        return 0
    return len(re.findall(r'\d',username)) / len(username)

def get_user_info(username:str) -> list:
    
    url = "https://www.instagram.com/api/v1/users/web_profile_info/?username=" + username
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 105.0.0.11.118 (iPhone11,8; iOS 12_3_1; en_US; en-US; scale=2.00; 828x1792; 165586599)'
    }

    '''    
    for _ in range(5):
        proxy = random.choice(proxies)
        try:
            r = requests.get(url,headers=headers,proxies={"https":proxy},timeout=5)
            #print("getting user info via",proxy,"status code:",r.status_code)
            if r.status_code == 200:
                break
        except Exception as e:
            print(e)
    else:
        return []  
    '''
    r = requests.get(url,headers=headers)
    if r.status_code != 200:
        return []
    print(r.text)
    #'''
    
    
    r = r.json()
    r = r['data']['user']
    return [
        profile_pic(r['profile_pic_url']), # has profile picture
        numDivLen(r['username']), # number of digits in username
        r['full_name'].count(' ') + 1, # number of words in full name
        numDivLen(r['full_name']), # number of digits in full name
        1 if r['username'] == r['full_name'] else 0, # username == full name
        len(r['biography']), #description length
        0 if r['external_url'] else 1, # has external url
        1 if r['is_private'] else 0, # is private
        r["edge_owner_to_timeline_media"]['count'], # number of posts
        r['edge_followed_by']['count'],
        r['edge_follow']['count']
    ]

if __name__ == "__main__":
    res = get_user_info("learningsteak")

    print(res)