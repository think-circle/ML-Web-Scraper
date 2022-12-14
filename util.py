from math import sin, cos, sqrt, atan2, radians
import pandas as pd
import numpy as np
import os
from datetime import date, timedelta


############################################################################################################
# Reporting
############################################################################################################
def progress_bar(progress,total):
    percent = int(100 * (progress/total))
    bar = '%' * percent + '-' * (100-percent)
    print(percent,"% Completed")
    print(f"{progress} out of {total} URLs COMPLETED")
    print(f"\r|{bar}| {percent:.2f}%", end="\r")


def update_progress(city,url):
    filename = city+'_latest_url.txt'
    if not os.path.exists(f"progress/"):
        os.mkdir("progress/")
    with open(f"progress/{city}_latest_url.txt", 'w+') as f:
        f.write(url)


############################################################################################################
# Stateful continuation of web scraping
############################################################################################################
def start_from_last_run(city,urls):
    filename = city+'_latest_url.txt'
    try:
        with open(f"progress/{city}_latest_url.txt", 'r') as file:
            url = file.read().rstrip()
            return urls[urls.index(url)+1:]
    except:
        return urls



############################################################################################################
# Date Related Functions
############################################################################################################

# Tells you what the date of upcoming saturday
def next_saturday(input_date):
  # Create a date object from the input date
  d = date.fromisoformat(input_date)

  # Add enough days to reach the next Saturday
  if d.weekday() == 6:
    days_to_add = 6
  else:
    days_to_add = 5 - d.weekday()
  
  next_sat = d + timedelta(days=days_to_add)

  return next_sat.isoformat()


# Returns the date of the the last time the Auction web scraping was run
# by reading from a file which records that last date that was scraped.
def get_date_last_run():
  filename = 'last_date_run.txt'
  try:
    with open('last_date_run.txt', 'r') as file:
          return file.read().rstrip().fromisoformat('2011-11-04')
  except:
        print('ISSUE OPENING LAST DATE RUN FILE!!!!')
        return date.today()


# Populates a list of dates for URL population
def populate_dates(first_run):
  if first_run:
    first_date = date(2018,4, 7)
  else:
    first_date = get_date_last_run()
  
  current_date = date.today()
  dates = []
  date = first_date

  # Loop through the dates and add them to the list
  while date <= current_date:
    dates.append(date.isoformat())
    date += timedelta(weeks=1)

  return dates


################################################

############################################################################################################
# TBA
############################################################################################################




















# def calc_distance(la1,lo1):
#     # approximate radius of earth in km
#     R = 6373.0

#     lat1 = radians(la1)
#     lon1 = radians(lo1)
#     lat2 = radians(-37.81007503047575)
#     lon2 = radians(144.96273301151334)

#     dlon = lon2 - lon1
#     dlat = lat2 - lat1

#     a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
#     c = 2 * atan2(sqrt(a), sqrt(1 - a))

#     distance = R * c
#     return distance
   



#print(f"DISTANCE: {calc_distance(-37.9822122,145.0389098,-37.81007503047575, 144.96273301151334)}")
#df7['distance']  = df.apply(lambda x: cal_distance(x['lat'], x['long']), axis=1)
# vec_cal_distance = np.vectorize(calc_distance)
# df7['distance']  = vec_cal_distance(df7.lat, df7.long)
# df7.head(20)