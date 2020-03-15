#Importing packages
from selenium import webdriver
# import pandas as pd
from bs4 import BeautifulSoup as bsoup
import graph as grcov

driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get("https://coronavirus.thebaselab.com/")
# review = driver.find_elements_by_class_name("text-left")
bs_obj = bsoup(driver.page_source, 'html.parser')
rows = bs_obj.find_all('table', class_='table-responsive-sm')[0].find('tbody').find_all('tr')

state_label = 0
arr_rows_data = []
for post in rows:

    country = post.find('th').get_text()
    rows_data = post.find_all('td')

    if country.find("Indonesia") == -1:
        continue
    else:
        print(
            "\n\t========================================",
            "\n\t\tnegara         : ", country,
            "\n\t========================================"
        )
        for post_td_row in rows_data:
            arr_rows_data.append(post_td_row.text)

        print(
            "\n\tInfection      : ", arr_rows_data[0],
            "\n\tActive Case    : ", arr_rows_data[1],
            "\n\tDeaths         : ", arr_rows_data[2],
            "\n\tRecovered      : ", arr_rows_data[3],
            "\n\tMortality Rate : ", arr_rows_data[4],
            "\n\tRecovery Rate  : ", arr_rows_data[5],
        )
        grcov.graph(
            arr_rows_data[0],
            arr_rows_data[1],
            arr_rows_data[2],
            arr_rows_data[3]
            )

    # name = post.find('th').get_text()
    # print(name)
# for post in review:
#     if post.text.find("Indonesia") == -1:
#         continue
#     else:
#         print(post.text)


print("debug.point")