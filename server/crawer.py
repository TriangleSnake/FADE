import urllib
import numpy as np
import cv2
import re
from bs4 import BeautifulSoup as bs
import instaloader
import os
import time
import configparser

os.chdir(os.path.dirname(__file__))

config = configparser.ConfigParser()

config.read('config.ini')

USERNAME = config['INSTAGRAM']['USERNAME']
PASSWORD = config['INSTAGRAM']['PASSWORD']




def compare_image(image1, image2):

    image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    resize = 500
    image1 = cv2.resize(image1, (resize,resize))
    image2 = cv2.resize(image2, (resize,resize))
    for i in range(resize):
        for j in range(resize):
            cv2.waitKey(500)
            
            if image1[i][j] != image2[i][j]:
                cv2.imshow("image1", cv2.rectangle(image1, (i, j), (i+1, j+1), (0, 255, 0), 1))
                cv2.imshow("image2", cv2.rectangle(image2, (i, j), (i+1, j+1), (0, 255, 0), 1))
                #return True
            else :
                cv2.imshow("image1", cv2.rectangle(image1, (i, j), (i+1, j+1), (0, 0, 255), 1))
                cv2.imshow("image2", cv2.rectangle(image2, (i, j), (i+1, j+1), (0, 0, 255), 1))
    return False

def check_username(username):
    if len(username)>30:
        return False
    pattern = r'^[A-Za-z0-9_.]+$'
    if re.match(pattern, username):
        return True
    else:
        return False

def get_img(image_url):
    response = urllib.request.urlopen(image_url)
    image_array = np.asarray(bytearray(response.read()), dtype=np.uint8)
    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
    return image

def get_account_info(username) -> dict:

    L = instaloader.Instaloader()
    L.login(user=USERNAME,passwd=PASSWORD)
    
    profile = instaloader.Profile.from_username(L.context,username)
    
    ret_dict = dict()
    '''
    session = requests.Session()
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"}
    ret_dict = dict()
    if not check_username(username):
        raise ValueError("Invalid username")
    url = "https://www.instagram.com/" + username
    r = session.get(url, headers=headers)
    soup = bs(r.text, "html.parser")
    with open("test.html", "w") as f:
        f.write(r.text)
    username = soup.title.string.split("•")[0]
    for i in "() ":
        username = username.replace(i, "")
    
    fullname = username.split("@")[0]
    username = username.split("@")[1]
    description = soup.find("div")
    
    if description:
        description = description.string
    else:
        description = ""
    '''
    ret_dict['fullname'] = profile.full_name
    ret_dict['username'] = username
    ret_dict['followers'] = profile.followers
    ret_dict['following'] = profile.followees
    ret_dict['private'] = profile.is_private
    
    pic_url = profile.profile_pic_url
    pic = get_img(pic_url)
    pic_default = cv2.imread("./asserts/default.jpg")

    ret_dict['profile_pic'] = compare_image(pic, pic_default)
    ret_dict['description'] = profile.biography
    ret_dict['external_url'] = True if profile.external_url else False
    return ret_dict

print(get_account_info("nba"))