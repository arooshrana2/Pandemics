#!/usr/bin/env python
import pandas as pd
import numpy as np
from datetime import datetime
import os

url = "https://www.mohfw.gov.in/"

def get_data():
	df_list = pd.read_html(url)
	return df_list[0]

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

	file_path = directory + '/' + file_name
	print("Saving file: ", file_path)
	df.to_csv(file_path)

if __name__ == '__main__':
	df = get_data()
	save_file(df, './')
