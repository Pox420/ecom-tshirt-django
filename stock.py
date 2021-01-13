from bs4 import BeautifulSoup
import requests
import openpyxl

def data(row):
    sheet.append(row)
    workbook.save(filename="data.xlsx")

response = requests.get('https://www.tadawul.com.sa/wps/portal/tadawul/market-participants/issuers/issuers-directory/company-details/!ut/p/z1/04_Sj9CPykssy0xPLMnMz0vMAfIjo8zi_Tx8nD0MLIy83V1DjA0czVx8nYP8PI0MDAz0I4EKzBEKDEJDLYEKjJ0DA11MjQzcTfW99KPSc_KTIGZllJQUWKkaqBqUJKYklpfmqBroRyXn5xYk5lUGV-Ym5QMVGQGBfjghUwuyg3LKKh0VASPsaGM!/#chart_tab2')
source = response.text
soup = BeautifulSoup(source, 'html.parser')
table= soup.find('table', id="adjustedPerformanceView")
table_h= table.find("thead").find("tr").find_all("th").string
print(table_h)

workbook =openpyxl.Workbook()
sheet = workbook.active
sheet.append(table_h)
workbook.save(filename="data.xlsx")

table_r= table.find("tbody").find_all("tr")
for rows in table_r:
    row= rows.find_all("td")
    print(row)
    data(row)


