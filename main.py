from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://ekb.cian.ru/snyat-kvartiru-1-komn-ili-2-komn/'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

name = soup.findAll('span',
                    class_='_93444fe79c--color_primary_100--mNATk _93444fe79c--lineHeight_28px--whmWV _93444fe79c--fontWeight_bold--ePDnv _93444fe79c--fontSize_22px--viEqA _93444fe79c--display_block--pDAEx _93444fe79c--text--g9xAG _93444fe79c--text_letterSpacing__normal--xbqP6')
link = soup.findAll('a',
                    class_='_93444fe79c--link--eoxce',
                    href=True
                    )
price = soup.findAll('span',
                     class_='_93444fe79c--color_black_100--kPHhJ _93444fe79c--lineHeight_28px--whmWV _93444fe79c--fontWeight_bold--ePDnv _93444fe79c--fontSize_22px--viEqA _93444fe79c--display_block--pDAEx _93444fe79c--text--g9xAG _93444fe79c--text_letterSpacing__normal--xbqP6')
address = soup.findAll('div',
                       class_='_93444fe79c--labels--L8WyJ')
description = soup.findAll('p',
                           class_='_93444fe79c--color_gray60_100--MlpSF _93444fe79c--lineHeight_20px--tUURJ _93444fe79c--fontWeight_normal--P9Ylg _93444fe79c--fontSize_14px--TCfeJ _93444fe79c--display_block--pDAEx _93444fe79c--text--g9xAG _93444fe79c--text_letterSpacing__normal--xbqP6')
links = [data['href'] for data in link]
names = [data.text for data in name]
prices = [data.text for data in price]
addresses = [data.text for data in address]
descriptions = [data.text for data in description]


a = {'Name': names,
     'Price': prices,
     'Address': addresses,
     'Description': descriptions,
     'Link': links
     }

df = pd.DataFrame.from_dict(a, orient='index')
df = df.transpose()

df.to_excel('./data.xlsx', sheet_name='Apartments', index=False)
