import nasdaqdatalink
import pandas as pd
import pygal

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 12)
pd.set_option('display.width', 400)

nasdaqdatalink.ApiConfig.api_key = 'Qt8xgJoYVWeVzv5sQ6JK'
TVTVR_data = nasdaqdatalink.get_table('QDL/BCHAIN', code='TVTVR')


TVTVR_list = []
dates = []
value = []

for index,row in TVTVR_data.iterrows():
  #Convert the timestamp to the date format as %Y-%m-%d
  date=row[1].strftime('%Y-%m-%d')
  # append to the list
  TVTVR_list.insert(0,(date,row[2]))
  #Extract seperate lists for date and value
  dates,value = zip(*TVTVR_list)

  #Create a line chart using pygal
chart = pygal.Line(x_label_rotation=45)
chart.title = 'Bitcoin Trade Volume vs Transaction Volume Ratio' 
chart.x_labels = dates
chart.add('Values',value)

chart.render_to_file('btv_tr.svg')


#TOTBC
TOTBC_data = nasdaqdatalink.get_table('QDL/BCHAIN', code='TOTBC')


TOTBC_list = []
dates = []
value = []

for index,row in TOTBC_data.iterrows():
  #Convert the timestamp to the date format as %Y-%m-%d
  date=row[1].strftime('%Y-%m-%d')
  # append to the list
  TOTBC_list.insert(0,(date,row[2]))
  #Extract seperate lists for date and value
  dates,value = zip(*TOTBC_list)

  #Create a line chart using pygal
chart = pygal.Line(x_label_rotation=45)
chart.title = 'Bitcoin Price Over Time' 
chart.x_labels = dates
chart.add('Values',value)

chart.render_to_file('bpot.svg')


