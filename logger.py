# https://www.youtube.com/watch?v=Bg9r_yLk7VY

import requests
from bs4 import BeautifulSoup
import smtplib
import sys
import datetime

my_eth = 0.04741157
buy_price = 3170.9068
buy_eur = 146.25
fee = 0.025 # 2.5% 
URL = 'https://ethereumprice.org/eth-eur/live/'
headers = {"User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}

x = datetime.datetime.now()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def check_price():
  page = requests.get(URL, headers=headers)
  soup = BeautifulSoup(page.content, 'html.parser')
  try:
    value = soup.find("span", class_="value").get_text()
    index = value.find(".")
    decimal = float(value[index+1:len(value)]) / 100
    value = value[0:index]
    converted_value = float(value.replace(",", ".")) * 1000 + decimal
    my_eur = my_eth * converted_value

    print(f"\n{bcolors.WARNING}Dátum a čas:{bcolors.ENDC}\t{(x.day):02d}.{(x.month):02d}.{(x.year):04d}\t{(x.hour):02d}:{(x.minute):02d}:{(x.second):02d}")
    print(f"{bcolors.WARNING}Aktuálny kurz:{bcolors.ENDC}\t1 ETH\t\t= {converted_value:.2f} €")
    print(f"{bcolors.WARNING}V peňaženke:{bcolors.ENDC}\t{my_eth} ETH\t= {my_eur:.4f} €")
    text_color = bcolors.FAIL if (my_eur - buy_eur) < 0.0 else bcolors.OKGREEN
    print(f"{bcolors.WARNING}Rozdiel:{text_color}\t{(my_eur - buy_eur):.4f} €")
    text_color = bcolors.FAIL if (my_eur*(1.0 - fee)) < buy_eur else bcolors.OKGREEN
    print(f"{bcolors.WARNING}Možný výber:{text_color}\t{(my_eur*(1.0 - fee)):.2f} €{bcolors.ENDC}\n")

    if '-email' in sys.argv:
      send_mail(my_eth, converted_value)
  except:
    e = sys.exc_info()[1]
    print(f"\n{bcolors.FAIL}CHYBA: {bcolors.ENDC}{e}\n")


def send_mail(my_eth, kurz):
  email_from = 'firemankoxd.python@gmail.com'
  password = 'Python55bot'
  email_to = 'kalus.filip25@gmail.com'
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.ehlo()
  server.starttls()
  server.ehlo()

  server.login(email_from, password)
  subject = f"1 ETH is worth {kurz:.2f} €"
  msg = f"Subject: {subject}\n\n" \
        f"Aktuálny kurz: 1 ETH = {kurz:.2f} €\n" \
        f"V peňaženke: {my_eth:.8f} ETH = {(my_eth*kurz):.4f} €\n" \
        f"Rozdiel: {(my_eth*kurz - 100.0):.2f} €\n" \
        f"Možný výber: {(my_eth*kurz*(1.0 - fee)):.2f} €"

  server.sendmail(email_from, email_to, msg.encode('utf-8'))
  print(f"Email bol poslany na adresu {email_to}\n")
  server.quit()

check_price()