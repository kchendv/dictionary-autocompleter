import requests
import gspread
from bs4 import BeautifulSoup
from oauth2client.service_account import ServiceAccountCredentials

pro_col = 3

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("Japanese Bank").sheet1

# Extract and print all of the values
search_terms = sheet.col_values(pro_col)


for c in range(len(search_terms) - 1):
    if search_terms[c] == search_terms[c + 1]:
        sheet.update_cell(c + 1, pro_col, "AAAAAAA" + search_terms[c])
