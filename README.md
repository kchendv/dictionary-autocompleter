# dictionary-autocompleter
## Summary
This is a tool that takes Japanese words and auto-fills the definition, spelling and difficulty on Google Sheets. The tool obtains information from www.jisho.org.

## Requirements
* Python 3.6 or higher
* Packages:
    * oauth2client
    * bs4
    * gspread
    * requests
## Setup
1. Enable Google API interaction on a GSuite account
2. Download client_secret.json and place it in the project directory

## Usage
1. Fill the spreadsheet on col 3 with **romaji** of the words that you wish to be autofilled
2. Specify the column range (e.g. start = 0, end = 100) that you want to fill
3. Run the following files for different purposes:
    * _bankfill.py_: fills the kanji spelling and definition of the word (first result on jisho.org)
    * _banktag.py_: fills the JLPT rating of the word, and whether or not it has the **common word** tag
    * _bankdupe.py_: removes duplicated entries in your dictionary
    