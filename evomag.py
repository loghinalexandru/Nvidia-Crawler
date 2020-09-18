import requests
import smtplib
from email.mime.text import MIMEText

from bs4 import BeautifulSoup

def crawl_evomag():
    receiver_email = 'loghinalexandru61@gmail.com'
    sender_email = 'noreply.gdpr9@gmail.com'

    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
    }

    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(sender_email, '')

    target = 'https://www.evomag.ro/componente-pc-gaming-placi-video/asus-placa-video-asus-geforce-rtx-3080-tuf-gaming-10gb-gddr6x-320-bit-3798493.html'

    result = requests.get(target, headers=headers)

    if(result.status_code == requests.codes.ok):         
        html =  BeautifulSoup(result.text, 'html.parser')
        product_availability = html.body.find('span', attrs={'id': 'stockWidgetView'})
        if("stock_stocepuizat" not in str(product_availability)):
            msg = MIMEText(target)
            msg['Subject'] = "Out of stock trigger"
            msg['To'] = receiver_email
            msg['From'] = sender_email
            smtp.sendmail(sender_email, receiver_email, str(msg))
    else:
        msg = MIMEText(target)
        msg['Subject'] = "Site failure"
        msg['To'] = receiver_email
        msg['From'] = sender_email
        smtp.sendmail(sender_email, receiver_email, str(msg))