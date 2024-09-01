import gspread
from google.oauth2.service_account import Credentials
from data import columns, row
import html
import os 
from dotenv import load_dotenv


load_dotenv()
def decode_html_entities(data):
    # puede ser causado por cómo se están codificando o interpretando los caracteres especiales cuando se suben a la hoja de cálculo.
    return [html.unescape(item) for item in data]

scopes = [
  "https://www.googleapis.com/auth/spreadsheets"
]

creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
client = gspread.authorize(creds)

sheet_id = os.environ.get('SHEET_ID')
workbook = client.open_by_key(sheet_id)

worksheet_list = map(lambda x: x.title, workbook.worksheets())
new_worksheet_name = "Questions"

if new_worksheet_name in worksheet_list:
  sheet = workbook.worksheet(new_worksheet_name)
else:
  sheet = workbook.add_worksheet(new_worksheet_name, rows=20, cols=20)

sheet.clear()
sheet.update(range_name='A1', values=columns)

for col_index, data in enumerate(row, start=1):
    decoded_data = decode_html_entities(data)
    cell_range = f'{chr(64 + col_index)}2'#carácter ASCII.
    sheet.update(range_name=cell_range, values=[[item] for item in decoded_data])