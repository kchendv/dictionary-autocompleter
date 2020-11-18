import requests
import gspread
from bs4 import BeautifulSoup
from oauth2client.service_account import ServiceAccountCredentials

def_col = 0
up_to = 1000
until = 0

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("Japanese Bank").sheet1

# Extract and print all of the values
if until == 0:
    search_terms = sheet.col_values(def_col)[up_to:]
else:
    search_terms = sheet.col_values(def_col)[up_to:until]


for c in range(len(search_terms)):
    try:
        page = requests.get("https://jisho.org/search/" + search_terms[c])
        text = page.text.split("concept_light clearfix")
        soup = BeautifulSoup(text[1], 'html.parser')
        results = soup.find("span", attrs={"class": "concept_light-tag label"})
        common = soup.find("span", attrs={"class": "concept_light-tag concept_light-common success label"})
        if common:
            sheet.update_cell(c + up_to + 1, 1, "O")
        try:
            q = results.text.strip()
            if q[0] == 'J':
                sheet.update_cell(c + up_to + 1, 2, q[-2:])
        except:
            pass
    except:
        pass
