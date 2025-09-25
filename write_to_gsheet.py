import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
from dotenv import load_dotenv
from datetime import datetime
from scrapper_stolnik import all_prices

load_dotenv()

GOOGLE_CREDENTIALS = os.getenv("GOOGLE_CREDENTIALS")
SPREADSHEET_ID = os.getenv("SPREADSHEET_ID")
WORKSHEET_ID = int(os.getenv("WORKSHEET_ID"))

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

today = datetime.today().strftime('%d.%m.%Y %H:%M')
worksheet.update(range_name='F3', values=[[today]])


