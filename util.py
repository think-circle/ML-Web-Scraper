from math import sin, cos, sqrt, atan2, radians
import pandas as pd
import numpy as np
df7 = pd.read_csv('../data/melb_data_latlong.csv')

def calc_distance(la1,lo1):
    # approximate radius of earth in km
    R = 6373.0

    lat1 = radians(la1)
    lon1 = radians(lo1)
    lat2 = radians(-37.81007503047575)
    lon2 = radians(144.96273301151334)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance
   



#print(f"DISTANCE: {calc_distance(-37.9822122,145.0389098,-37.81007503047575, 144.96273301151334)}")
#df7['distance']  = df.apply(lambda x: cal_distance(x['lat'], x['long']), axis=1)
vec_cal_distance = np.vectorize(calc_distance)
df7['distance']  = vec_cal_distance(df7.lat, df7.long)
df7.head(20)