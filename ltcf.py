import requests, re, json, os, sys, time, random
from bs4 import BeautifulSoup
from time import sleep

def config():
  if not os.path.exists(".cfg"):
     os.makedirs(".cfg")
  if not os.path.exists(".cfg/ltc_cfg.json"):
     f = open(".cfg/ltc_cfg.json", "w+")
     f.write("file_ready")
     f.close()
  pilihan = input("\n\033[1;35mScript ini untuk nuyul \033[1;36mlitecoin-free.com\nGanti config [y/n] : ")
  if pilihan == 'y':
    user=input("\n\n\033[1;32mmasukkan username : \033[1;0m")
    pw=input("\033[1;32mmasukkan passwordnya : \033[1;0m")
    f = open(".cfg/ltc_cfg.json", "w+")
    f.write('{\n  "username": "'+user+'",\n  "password": "'+pw+'"\n}')
    f.close()
  elif pilihan == 'n':
    sleep(1)
  else:
    print("\n\033[1;31mmasukkan input yg benar")
    sys.exit()

config()
with open('.cfg/ltc_cfg.json', 'r') as (fh):
  json_str = fh.read()
  json_value = json.loads(json_str)
  nama = json_value['username']
  pwd = json_value['password']
  
def tunggu(x):
    sys.stdout.write("\r")
    sys.stdout.write("                                                               ")
    for remaining in range(x, 0, -1):
       sys.stdout.write("\r")
       sys.stdout.write("\033[1;32m» Claim after \033[1;0m{:2d} \033[1;32mseconds".format(remaining))
       sys.stdout.flush()
       sleep(1)
       
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)
        
c = requests.Session()

url_login = "http://litecoin-free.com/login"
url_claim = "http://litecoin-free.com/earn/money-1"
url_bonus = "http://litecoin-free.com/balance/balance-1.php"

ua = {
 "User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.119 Mobile Safari/537.36"
}

dta = {
  "username": nama,
  "password": pwd,
  "remember": "yes",
  "login_btn": "Sign+In"

}

banner = f"""\033[1;35m
                                              
eeeee  eeeee e    e eeee eeeee       e  eeeee 
8   8  8   8 8    8 8    "   8       8  8   8 
8eee8e 8eee8 8eeee8 8eee eeee8       8e 8e  8 
88   8 88  8   88   88   88          88 88  8 
88   8 88  8   88   88ee 88ee8       88 88ee8 
                               eeeee
\033[1;36m=============================================
\033[1;32m ~ anthesphong1998@gmail.com - t.me/rayez_id
\033[1;36m=============================================
"""
os.system('clear')
print(banner)
r = c.post(url_login,headers=ua, data=dta)
soup = BeautifulSoup(r.content, "html.parser")
x = soup.find('strong')
mengetik(f"\033[1;35mWELCOME TO BOT (V01) -\033[1;36m {x.text}\n\033[1;35mSCRIPT INI UNTUK NUYUL WEB -\033[1;36m litecoin-free.com\n")
os.system('termux-open-url https://www.youtube.com/channel/UCDiHntcudIvgJUFS2XAHEpQ')

def login():
  r = c.post(url_login,headers=ua, data=dta)
  soup = BeautifulSoup(r.content, "html.parser")
  y = soup.find('div', class_="stat-text")
  z = re.findall(r'([\d.]*\d+)',y.text)[0]
  sys.stdout.write(f"\r\033[1;32m» Your balance has been updated || {z} LTC\n")
  sleep(1)

def claim():
  r = c.post(url_claim,headers=ua, data=dta)
  soup = BeautifulSoup(r.content, "html.parser")
  x = soup.find_all('script', type="text/javascript")[19]
  y = re.findall(r'var time_advertisement = ([\d.]*\d+)',x.text)
  tunggu (int(float(y[0])))
  sleep(5)

def bonus():
  r = c.post(url_bonus,headers=ua, data=dta)
  soup = BeautifulSoup(r.content, "html.parser")
  sys.stdout.write(f"\r\033[1;32m» Bonus berhasil di claim\n")
  sleep(1)

for i in range(999):
  login()
  claim()
  try:
   bonus()
  except Exception:
   tunggu(300)
