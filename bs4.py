import sys
from bs4 import BeautifulSoup
import time
import requests
import smtplib


URL = "https://www.flipkart.com/apple-iphone-6s-gold-64-gb/p/itmebysgqertms7g?pid=MOBEBY3V6HYJHTUB&lid=LSTMOBEBY3V6HYJHTUBPZUQFL&marketplace=FLIPKART&sattr[]=color&sattr[]=storage&st=color&otracker=search"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36 OPR/63.0.3368.107'}

def check_title():

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find("span", class_="_35KyD6").get_text()
    price = soup.find("div", class_="_1vC4OE _3qQ9m1").get_text()
    price_list = price[1:7]
    

    if str(price_list) <= '25,000':
        print(title)
        print(price_list)
        sent_mail()
    else:     
        print(price_list)
        print("Price is Same!!!!")

    sys.exit()    
    
       

def sent_mail():
   
    sender =str(input("Enter Sender e-mail"))
    reciver = str(input("Enter receiver e-mail")) 
    msg='Check out the URL \n {}'.format(URL) # whatever msessage you wnt to give to reciver
    passw = str(input("Enter sender password")) 

    secure = smtplib.SMTP('smtp.gmail.com', 587)
    secure.ehlo()
    secure.starttls()
    secure.ehlo()
    secure.login(sender, passw)
    secure.sendmail(sender,reciver , msg)
    print('Send')
    secure.quit()


check_title()

"""while True:  # script run every hour to check!!!
    check_title()
    time.sleep()
    """
