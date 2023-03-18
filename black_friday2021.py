import csv
import requests
from bs4 import BeautifulSoup

header=['ORDER','NAME OF PRODUIT','MARK','SHINPPING(DH)','PRICE(DH)','TOTAL']

URLS=['https://www.jumia.ma/ar/vr-box-2.0-virtual-reality-3d-glasses-for-3.5-6.0-inch-smartphone-camera-ar-vr-box-mpg856232.html','https://www.jumia.ma/ar/vr-shinecon-lunettes-video-3d-de-realite-virtuelle-adaptees-aux-smartphones-de-35-a-60-pouces-avec-casque-hifi-27755973.html',
      'https://www.jumia.ma/ar/vr-box-lunettes-3d-realite-pour-tous-mobiles-android-iphone-33045899.html?seller_product=1','https://www.jumia.ma/ar/moulin-a-cafe-aussi-a-epices-new-design-large-capacite-env.-70g-homy-mpg75170.html'
      'https://www.jumia.ma/ar/f9-5-ecouteurs-sans-fil-bluetooth-avec-power-bank-led-digital-tws-mpg923721.html','https://www.jumia.ma/ar/generic-uno-r3-shield-q-starter-kit-for-arduino-beginner-stem-lcd-se-44366365.html',
      'https://www.jumia.ma/ar/autre-id-starter-kit-for-arduino-uno-r3-upgraded-version-learning-suite-with-retail-box-43955453.html','https://www.jumia.ma/ar/carte-wifi-usb-alfa-awus039nh-adaptateur-98dbi-high-gain-alfa-network-mpg19854.html']


for i in range(len(URLS)):
    page=requests.get(URLS[i]).content
    soop=BeautifulSoup(page,'html.parser')
    name=soop.find('h1',class_="-fs20 -pts -pbxs").text.split(" ")
    new_name=' '.join(name[:5])
    shipping=soop.find('div',class_="markup -ptxs").text
    new_shipping1=shipping.replace('Dhs','')
    new_shipping2=new_shipping1.replace('الشحن','')

    price   =soop.find('span',class_="-b -ltr -tal -fs24").text.replace('Dhs','')
    total=float(price)+float(new_shipping2)
    data=[i,new_name,'','',URLS[i],new_shipping2,price,total]
    with open('DATA_BLACK_FRIDAY_2021.csv','a', encoding='UTF8') as data:
        writer = csv.writer(data)
        # write the header
        # writer.writerow(header)

        # write the data
        writer.writerow(data)

