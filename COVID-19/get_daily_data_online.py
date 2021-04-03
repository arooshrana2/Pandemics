#!/usr/bin/env python
import pandas as pd
import numpy as np
from datetime import datetime
import os

url = "https://www.mygov.in/covid-19"

def get_data():
        from selenium import webdriver
        from bs4 import BeautifulSoup
	"""
	Link to download chromedriver:
		https://sites.google.com/a/chromium.org/chromedriver/downloads
	Link with setting up of chromedriver:
		https://sites.google.com/a/chromium.org/chromedriver/getting-started
	"""
	
	# opens a web browser for testing
        browser = webdriver.Chrome()  # needs chromedriver file in PATHS or specify it as arg
        browser.get(url)  # fetches the data from url on the browser
        
	html_source = browser.page_source
        browser.quit()
        soup = BeautifulSoup(html_source, 'lxml')
        data = soup.find('table', {'class':'ind-mp_tbl sortable'})  # finding the table tag with class ind-mp_tbl and sortable
    
        span_data = data.find_all('span')
        [d.extract() for d in span_data]  # removing the span tag data as it contains the surge from last day
    
        try:
                data = data.encode('utf-8')  # encoding the data to utf-8 to store in data frame
        except:
                pass
    
        return pd.read_html(data)[0]


def save_file(df, directory, file_name=None):
	directory = os.path.abspath(directory) + '/daily_data'
	if file_name == None:
		file_name = datetime.strftime(datetime.now(), '%Y%m%d')
	else:
		file_name = file_name + datetime.strftime(datetime.today(), '%Y%m%d')
	if datetime.now().hour < 12:
		file_name = file_name + '_morning.csv'
	elif datetime.now().hour < 15:
		file_name = file_name + '_afternoon.csv'
	else:
		file_name = file_name + '_evening.csv'

	file_path = os.path.join(directory, file_name)
	print("Saving file: ", file_path)
	df.to_csv(file_path, index=False)

if __name__ == '__main__':
	df = get_data()
	save_file(df, './')
