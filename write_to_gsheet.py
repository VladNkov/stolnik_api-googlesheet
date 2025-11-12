import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
from dotenv import load_dotenv
from datetime import datetime
from scrapper_stolnik import get_all_prices

load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
GOOGLE_CREDENTIALS = os.path.join(BASE_DIR, "innate-vigil-413910-fba5430aca0d.json")
# GOOGLE_CREDENTIALS = os.getenv("GOOGLE_CREDENTIALS")
# GOOGLE_CREDENTIALS = "/opt/airflow/projects/stolnik_api-googlesheet/innate-vigil-413910-fba5430aca0d.json"
SPREADSHEET_ID = os.getenv("SPREADSHEET_ID")
WORKSHEET_ID = int(os.getenv("WORKSHEET_ID"))

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(GOOGLE_CREDENTIALS, scope)
client = gspread.authorize(creds)

spreadsheet = client.open_by_key(SPREADSHEET_ID)
worksheet = spreadsheet.get_worksheet_by_id(WORKSHEET_ID)
all_prices = get_all_prices()

updates = [
    ('E8:F8', 'sheet_1mm_1000_2000'),
    ('E9:F9', 'sheet_2mm_1000_2000'),
    ('E6:F6', 'sheet_2mm_1250_2500'),
    ('E7:F7', 'sheet_8mm_m2'),
    ('E10:F10', 'sheet_10mm_m2'),
    ('E11:F11', 'sheet_perf_2mm_1000_2000'),
    ('E5:F5', 'sheet_corrug_3mm_1000_4000'),
    ('E12:F12', 'sheet_expand_3mm_1000_2000'),
    ('E14:F14', 'pipe_20_20_2'),
    ('E15:F15', 'pipe_30_30_3'),
    ('E16:F16', 'pipe_40_20_3'),
    ('E17:F17', 'pipe_40_40_3'),
    ('E18:F18', 'pipe_50_30_3'),
    ('E19:F19', 'pipe_50_50_3'),
    ('E20:F20', 'pipe_100_50_3'),
    ('E21:F21', 'corner_20_20_3'),
    ('E22:F22', 'corner_30_30_3'),
    ('E23:F23', 'corner_50_50_3'),
    ('E25:F25', 'armature_8mm'),
    ('E26:F26', 'stripe_20_4'),
    ('E27:F27', 'rod_m10'),
    ('E28:F28', 'screw_m10'),
    ('E29:F29', 'navis_16'),
]

# value = all_prices['sheet_1mm_1000_2000']
# worksheet.update(range_name='E8:F8', values=[[value['name'], value['price']]])
#
# value = all_prices['sheet_2mm_1000_2000']
# worksheet.update(range_name='E9:F9', values=[[value['name'], value['price']]])
#
# value = all_prices['sheet_2mm_1250_2500']
# worksheet.update(range_name='E6:F6', values=[[value['name'], value['price']]])
#
# value = all_prices['sheet_8mm_m2']
# worksheet.update(range_name='E7:F7', values=[[value['name'], value['price']]])
#
# value = all_prices['sheet_10mm_m2']
# worksheet.update(range_name='E10:F10', values=[[value['name'], value['price']]])
#
# value = all_prices['sheet_perf_2mm_1000_2000']
# worksheet.update(range_name='E11:F11', values=[[value['name'], value['price']]])
#
# value = all_prices['sheet_corrug_3mm_1000_4000']
# worksheet.update(range_name='E5:F5', values=[[value['name'], value['price']]])
#
# value = all_prices['sheet_expand_3mm_1000_2000']
# worksheet.update(range_name='E12:F12', values=[[value['name'], value['price']]])
#
# value = all_prices['pipe_20_20_2']
# worksheet.update(range_name='E14:F14', values=[[value['name'], value['price']]])
#
# value = all_prices['pipe_30_30_3']
# worksheet.update(range_name='E15:F15', values=[[value['name'], value['price']]])
#
# value = all_prices['pipe_40_20_3']
# worksheet.update(range_name='E16:F16', values=[[value['name'], value['price']]])
#
# value = all_prices['pipe_40_40_3']
# worksheet.update(range_name='E17:F17', values=[[value['name'], value['price']]])
#
# value = all_prices['pipe_50_30_3']
# worksheet.update(range_name='E18:F18', values=[[value['name'], value['price']]])
#
# value = all_prices['pipe_50_50_3']
# worksheet.update(range_name='E19:F19', values=[[value['name'], value['price']]])
#
# value = all_prices['pipe_100_50_3']
# worksheet.update(range_name='E20:F20', values=[[value['name'], value['price']]])
#
# value = all_prices['corner_20_20_3']
# worksheet.update(range_name='E21:F21', values=[[value['name'], value['price']]])
#
# value = all_prices['corner_30_30_3']
# worksheet.update(range_name='E22:F22', values=[[value['name'], value['price']]])
#
# value = all_prices['corner_50_50_3']
# worksheet.update(range_name='E23:F23', values=[[value['name'], value['price']]])
#
# value = all_prices['armature_8mm']
# worksheet.update(range_name='E25:F25', values=[[value['name'], value['price']]])
#
# value = all_prices['stripe_20_4']
# worksheet.update(range_name='E26:F26', values=[[value['name'], value['price']]])
#
# value = all_prices['rod_m10']
# worksheet.update(range_name='E27:F27', values=[[value['name'], value['price']]])
#
# value = all_prices['screw_m10']
# worksheet.update(range_name='E28:F28', values=[[value['name'], value['price']]])
#
# value = all_prices['navis_16']
# worksheet.update(range_name='E29:F29', values=[[value['name'], value['price']]])
#
# today = datetime.today().strftime('%d.%m.%Y %H:%M')
# worksheet.update(range_name='F3', values=[[today]])

batch_data = []
for cell_range, key in updates:
    value = all_prices.get(key)
    if value:
        batch_data.append({
            'range': cell_range,
            'values': [[value['name'], value['price']]]
        })


today = datetime.today().strftime('%d.%m.%Y %H:%M')
batch_data.append({
    'range': 'F3',
    'values': [[today]]
})


worksheet.batch_update(batch_data)
print("Данные обновлены в Google Sheets")