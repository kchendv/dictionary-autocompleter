import requests
import gspread
from bs4 import BeautifulSoup
from oauth2client.service_account import ServiceAccountCredentials

pro_col = 0
up_to = 1000
until = 0

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sre you use the right name here.
sheet = client.open("Japanese Bank").sheet1

# Extract and print all of the values
if until == 0:
    search_terms = sheet.col_values(pro_col)[up_to:]
else:
    search_terms = sheet.col_values(pro_col)[up_to:until]


for c in range(len(search_terms)):
    que = search_terms[c]
    que = que.replace(" ", "")
    try:
        page = requests.get("https://jisho.org/search/" + que)
        text = page.text.split("concept_light clearfix")
        soup = BeautifulSoup(text[1], 'html.parser')
        results = soup.find("span", attrs={"class": "text"})
        defs = soup.find_all("span", attrs={"class": "meaning-meaning"})
        try:
            q = results.text.strip()
            sheet.update_cell(c + up_to + 1, pro_col - 1, q)
        except:
            pass
            print(que, "cant add word for some reason")
        try:
            qr = " "
            for dif in defs:
                if not dif.find("span", attrs={"class": "break-unit"}):
                    qr += "; " + dif.text.strip()
            sheet.update_cell(c + up_to + 1, pro_col + 1, qr[3:])
        except:
            pass
            print(que, "def not found?")
    except:
        print(que, " cannot be found")
