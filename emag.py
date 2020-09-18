import requests
import smtplib
from email.mime.text import MIMEText

from bs4 import BeautifulSoup

def crawl_emag():

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

    target = 'https://www.emag.ro/placa-video-asus-tuf-gaming-geforce-rtxtm-3080-10gb-gddr6x-320-bit-tuf-rtx3080-10g-gaming/pd/DHQ322MBM/?X-Search-Id=329d1c01df55124b86bd&X-Product-Id=7081231&X-Search-Page=1&X-Search-Position=2&X-Section=search&X-MB=0&X-Search-Action=view'

    result = requests.get(target, headers=headers)
    
    if(result.status_code == requests.codes.ok):         
        html =  BeautifulSoup(result.text, 'html.parser')
        product_availability = html.body.find('span', attrs={'class': 'label'})
        if("label-out_of_stock" not in str(product_availability)):
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