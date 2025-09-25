import requests
from bs4 import BeautifulSoup
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

GOOGLE_CREDENTIALS = os.getenv("GOOGLE_CREDENTIALS")
SPREADSHEET_ID = os.getenv("SPREADSHEET_ID")
WORKSHEET_ID = int(os.getenv("WORKSHEET_ID"))


urls = {'https://stroyryad.com.ua/cat/lyst-chornyi': [2821, 2823, 2829, 7784, 7791],
        'https://stroyryad.com.ua/cat/lyst-ryflenyi': [10515],
        'https://stroyryad.com.ua/cat/lyst-perforovanyi': [7165],
        'https://stroyryad.com.ua/cat/lyst-prosichno-vytiazhnyi': [6650],
        'https://stroyryad.com.ua/cat/truby-profilni': [2897, 3469, 13525, 16080, 3406, 3029, 3027, ],
        'https://stroyryad.com.ua/cat/kutyk-katanyi': [2975, 7458, 6216],
        'https://stroyryad.com.ua/cat/armatura': [2857],
        'https://stroyryad.com.ua/cat/smuha': [12764]}

products = {'sheet_1mm_1000_2000': {'url': 'https://stroyryad.com.ua/cat/lyst-chornyi', 'id': 2821},
            'sheet_2mm_1000_2000': {'url': 'https://stroyryad.com.ua/cat/lyst-chornyi', 'id': 2823},
            'sheet_2mm_1250_2500': {'url': 'https://stroyryad.com.ua/cat/lyst-chornyi','id': 2829},
            'sheet_8mm_m2': {'url': 'https://stroyryad.com.ua/cat/lyst-chornyi', 'id': 7784},
            'sheet_10mm_m2': {'url': 'https://stroyryad.com.ua/cat/lyst-chornyi', 'id': 7791},
            'sheet_corrug_3mm_1000_4000': {'url': 'https://stroyryad.com.ua/cat/lyst-ryflenyi', 'id': 10515},
            'sheet_perf_2mm_1000_2000': {'url': 'https://stroyryad.com.ua/cat/lyst-perforovanyi', 'id': 7165},
            'sheet_expand_3mm_1000_2000': {'url': 'https://stroyryad.com.ua/cat/lyst-prosichno-vytiazhnyi', 'id': 6650},
            'pipe_20_20_2': {'url': 'https://stroyryad.com.ua/cat/truby-profilni', 'id': 2897},
            'pipe_30_30_3': {'url': 'https://stroyryad.com.ua/cat/truby-profilni', 'id': 3469},
            'pipe_40_20_3': {'url': 'https://stroyryad.com.ua/cat/truby-profilni', 'id': 13525},
            'pipe_40_40_3': {'url': 'https://stroyryad.com.ua/cat/truby-profilni', 'id': 16080},
            'pipe_50_30_3': {'url': 'https://stroyryad.com.ua/cat/truby-profilni', 'id': 3406},
            'pipe_50_50_3': {'url': 'https://stroyryad.com.ua/cat/truby-profilni', 'id': 3029},
            'pipe_100_50_3': {'url': 'https://stroyryad.com.ua/cat/truby-profilni', 'id': 3027},
            'corner_20_20_3': {'url': 'https://stroyryad.com.ua/cat/kutyk-katanyi', 'id': 2975},
            'corner_30_30_3': {'url': 'https://stroyryad.com.ua/cat/kutyk-katanyi', 'id': 7458},
            'corner_50_50_3': {'url': 'https://stroyryad.com.ua/cat/kutyk-katanyi', 'id': 6216},
            'armature_8mm': {'url': 'https://stroyryad.com.ua/cat/armatura', 'id': 2857},
            'stripe_20_4': {'url': 'https://stroyryad.com.ua/cat/smuha', 'id': 12764}}


def get_prices_and_name(url, pid):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    a_tag = soup.find('a', href=f"/cat/{url.split('/')[-1]}/product/{pid}")
    tr = a_tag.find_parent('tr')
    tds = tr.find_all('td')
    price = (tds[2].get_text(strip=True))
    price = price.replace('грн.', '').replace('\xa0', '').strip()
    price = float(price.replace(',', '.'))
    name = a_tag.get_text(strip=True).replace('Купити', '')
    return {"name": name, "price": price}


all_prices = {}
for key, info in products.items():
    result = get_prices_and_name(info['url'], info['id'])
    all_prices[key] = result


scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(GOOGLE_CREDENTIALS, scope)
client = gspread.authorize(creds)

spreadsheet = client.open_by_key(SPREADSHEET_ID)
worksheet = spreadsheet.get_worksheet_by_id(WORKSHEET_ID)

value = all_prices['sheet_1mm_1000_2000']
worksheet.update(range_name='E8:F8', values=[[value['name'], value['price']]])

value = all_prices['sheet_2mm_1000_2000']
worksheet.update(range_name='E9:F9', values=[[value['name'], value['price']]])

value = all_prices['sheet_2mm_1250_2500']
worksheet.update(range_name='E6:F6', values=[[value['name'], value['price']]])

value = all_prices['sheet_8mm_m2']
worksheet.update(range_name='E7:F7', values=[[value['name'], value['price']]])

value = all_prices['sheet_10mm_m2']
worksheet.update(range_name='E10:F10', values=[[value['name'], value['price']]])

value = all_prices['sheet_perf_2mm_1000_2000']
worksheet.update(range_name='E11:F11', values=[[value['name'], value['price']]])

value = all_prices['sheet_corrug_3mm_1000_4000']
worksheet.update(range_name='E5:F5', values=[[value['name'], value['price']]])

value = all_prices['sheet_expand_3mm_1000_2000']
worksheet.update(range_name='E12:F12', values=[[value['name'], value['price']]])

value = all_prices['pipe_20_20_2']
worksheet.update(range_name='E14:F14', values=[[value['name'], value['price']]])

value = all_prices['pipe_30_30_3']
worksheet.update(range_name='E15:F15', values=[[value['name'], value['price']]])

value = all_prices['pipe_40_20_3']
worksheet.update(range_name='E16:F16', values=[[value['name'], value['price']]])

value = all_prices['pipe_40_40_3']
worksheet.update(range_name='E17:F17', values=[[value['name'], value['price']]])

value = all_prices['pipe_50_30_3']
worksheet.update(range_name='E18:F18', values=[[value['name'], value['price']]])

value = all_prices['pipe_50_50_3']
worksheet.update(range_name='E19:F19', values=[[value['name'], value['price']]])

value = all_prices['pipe_100_50_3']
worksheet.update(range_name='E20:F20', values=[[value['name'], value['price']]])

value = all_prices['corner_20_20_3']
worksheet.update(range_name='E21:F21', values=[[value['name'], value['price']]])

value = all_prices['corner_30_30_3']
worksheet.update(range_name='E22:F22', values=[[value['name'], value['price']]])

value = all_prices['corner_50_50_3']
worksheet.update(range_name='E23:F23', values=[[value['name'], value['price']]])

value = all_prices['armature_8mm']
worksheet.update(range_name='E25:F25', values=[[value['name'], value['price']]])

value = all_prices['stripe_20_4']
worksheet.update(range_name='E26:F26', values=[[value['name'], value['price']]])

today = datetime.today().strftime('%d.%m.%Y')
worksheet.update(range_name='F3', values=[[today]])

print("Цены загружены в Google Sheets!")


