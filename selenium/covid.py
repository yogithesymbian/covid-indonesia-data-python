#Importing packages
from selenium import webdriver
# import pandas as pd
from bs4 import BeautifulSoup as bsoup
import graph as grcov
# import storing as cstore
from firebase import firebase
import time

# driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver = webdriver.Chrome("/opt/homebrew/bin/chromedriver")
driver.get("https://coronavirus.thebaselab.com/")
# review = driver.find_elements_by_class_name("text-left")
bs_obj = bsoup(driver.page_source, 'html.parser')
rows = bs_obj.find_all('table', class_='table-bordered')[0].find('tbody').find_all('tr')

state_label = 0
arr_rows_data = []
arr_rows_data_store = []
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
            arr_rows_data_store.append(post_td_row.text)

        print(
            "\n\tCases              : ", arr_rows_data[0],
            "\n\tDeaths             : ", arr_rows_data[1],
            "\n\tNew Cases          : ", arr_rows_data[2],
            "\n\tNew Deaths         : ", arr_rows_data[3],
            "\n\tActive Cases       : ", arr_rows_data[4],
            "\n\tRecovered          : ", arr_rows_data[5],
            "\n\tMortality Rate     : ", arr_rows_data[6],
            "\n\tRecovery Rate      : ", arr_rows_data[7],
            "\n\tCases per 1M Pop.  : ", arr_rows_data[8],
            "\n\tTests per 1M Pop.  : ", arr_rows_data[9],
        )
        print(
            "\n\t========================================",
            "\n\t (c) 2020 scodeid - Yogi Arif Widodo",
            "\n\t========================================"
        )
        # cstore.store_data(
        #     arr_rows_data_store[0],
        #     arr_rows_data_store[1],
        #     arr_rows_data_store[2],
        #     arr_rows_data_store[3],
        #     arr_rows_data_store[4],
        #     arr_rows_data_store[5]
        # )
        time_hhmmss = time.strftime('%H:%M:%S')
        date_mmddyyyy = time.strftime('%d/%m/%Y')

        data = {
            "cases": arr_rows_data_store[0],
            "deaths": arr_rows_data_store[1],
            "new_cases": arr_rows_data_store[2],
            "new_deaths": arr_rows_data_store[3],
            "active_cases": arr_rows_data_store[4],
            "recovered": arr_rows_data_store[5],
            "mortality_rate": arr_rows_data_store[6],
            "recovery_rate": arr_rows_data_store[7],
            "cases_per_1_m_pop": arr_rows_data_store[8],
            "tests_per_1_m_pop": arr_rows_data_store[9],
            'date': date_mmddyyyy,
            'time': time_hhmmss,

        }
        firebase = firebase.FirebaseApplication('yourserver')
        result = firebase.post('/covid/indonesia', data)
        print(result)

        grcov.graph(
            arr_rows_data[0],
            arr_rows_data[1],
            arr_rows_data[2],
            arr_rows_data[3]
        )

print("debug.point")