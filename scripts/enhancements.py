import pandas 
import numpy 
import urllib.request
import ssl
import pgeocode
from datetime import datetime
ssl._create_default_https_context = ssl._create_unverified_context



### Assessing Dataset ###


NoShowData = pandas.read_csv('data/output_noshow.csv')
# Assessing NoShowData without missing rows cells
NoShowData1 = NoShowData
NoShowData1.replace('', numpy.nan, inplace=True)
NoShowData1 = NoShowData1.dropna(axis = 0)
# Assessing NoShowData without missing columns cells, with a threshold for missingness
NoShowData2 = NoShowData
NoShowData2.replace('', numpy.nan, inplace=True)
thresh = len(NoShowData2) * .2
NoShowData2.dropna(thresh = thresh, axis = 1, inplace = True)



###  Enhancement ###


## Distance Enhancement ## 

# Loading enhancing datset and removing rows with empty cells
practiceLocation = pandas.read_csv('data/practiceLocations.csv')
practiceLocation = practiceLocation.dropna(axis = 0)
# Merging enhancing dataset with NoShowData2 and removing rows with empty cells
DistanceEnhancement = pandas.merge(NoShowData2, practiceLocation, on = 'practice_id', how = 'inner')
DistanceEnhancement = DistanceEnhancement.dropna(axis = 0)
# Reformatting dataset Zip-Code to 5 digits only
DistanceEnhancement['patient_zipcode_x'] = DistanceEnhancement['patient_zipcode_x'].astype(str)
DistanceEnhancement['patient_zipcode_x'] = DistanceEnhancement['patient_zipcode_x'].apply(lambda x: x.zfill(5))
DistanceEnhancement['patient_zipcode_x'] = DistanceEnhancement['patient_zipcode_x'].str[:5]
# Calculating distance (miles) between Patient and Practice Zipcode using 'pgeocode' API
def get_distance(x, y):
    usa_zipcodes = pgeocode.GeoDistance('us')
    distance_in_kms = usa_zipcodes.query_postal_code(x.values, y.values)
    return distance_in_kms
DistanceEnhancement['patient_distance_from_practice (miles)'] = get_distance(DistanceEnhancement['patient_zipcode_x'], DistanceEnhancement['practice_zipcode'])
DistanceEnhancement['patient_distance_from_practice (miles)'] = DistanceEnhancement['patient_distance_from_practice (miles)'] * 0.621371
DistanceEnhancement['patient_distance_from_practice (miles)'] = DistanceEnhancement['patient_distance_from_practice (miles)'].round(2)
# Removing rows with empty values in patient_distance_from_practice (miles) column
DistanceEnhancement['patient_distance_from_practice (miles)'].replace('', numpy.nan, inplace = True)
DistanceEnhancement.dropna(subset=['patient_distance_from_practice (miles)'], inplace = True)
# Grouping distance ranges within dataset into a new oclumn 
DistanceEnhancement.loc[DistanceEnhancement['patient_distance_from_practice (miles)']<5.01, 'patient_distance_from_practice_group'] = 'nearby'
DistanceEnhancement.loc[DistanceEnhancement['patient_distance_from_practice (miles)'].between(5.01,10), 'patient_distance_from_practice_group'] = 'close'
DistanceEnhancement.loc[DistanceEnhancement['patient_distance_from_practice (miles)'].between(10.01,30), 'patient_distance_from_practice_group'] = 'far'
DistanceEnhancement.loc[DistanceEnhancement['patient_distance_from_practice (miles)'].between(30.01,50.01), 'patient_distance_from_practice_group'] = 'very far'
DistanceEnhancement.loc[DistanceEnhancement['patient_distance_from_practice (miles)']>50.01, 'patient_distance_from_practice_group'] = 'unreasonable distance'
# Reordering dataset columns
NewDistanceEnhancementColumnOrder = ['practice_id', 'practice_zipcode', 'patient_id',
'patient_zipcode_x', 'patient_distance_from_practice (miles)', 'appointment_yosi_noshow1', 'patient_distance_from_practice_group']
DistanceEnhancement = DistanceEnhancement.reindex(columns = NewDistanceEnhancementColumnOrder)
# Exporting dataset
DistanceEnhancement.to_csv('data/EnhancedDatasets/DistanceEnhancement.csv', index = False)


## Age Enhancement ##

# Reallocating data and removing rows with empty cells
AgeEnhancement = NoShowData2.copy()
# Grouping age ranges within dataset into a new oclumn 
AgeEnhancement.loc[AgeEnhancement['patient_age']<8, 'patient_age_group'] = 'child'
AgeEnhancement.loc[AgeEnhancement['patient_age'].between(8,12), 'patient_age_group'] = 'adolescent'
AgeEnhancement.loc[AgeEnhancement['patient_age'].between(13,17), 'patient_age_group'] = 'teen'
AgeEnhancement.loc[AgeEnhancement['patient_age'].between(18,23), 'patient_age_group'] = 'young adult'
AgeEnhancement.loc[AgeEnhancement['patient_age'].between(24,30), 'patient_age_group'] = 'mature adult'
AgeEnhancement.loc[AgeEnhancement['patient_age'].between(31,49), 'patient_age_group'] = 'adult'
AgeEnhancement.loc[AgeEnhancement['patient_age'].between(50,65), 'patient_age_group'] = 'senior'
AgeEnhancement.loc[AgeEnhancement['patient_age']>65, 'patient_age_group'] = 'elderly'
# Reordering dataset columns
NewAgeEnhancementColumnOrder = ['patient_id', 'patient_age', 'appointment_yosi_noshow1', 'patient_age_group']
AgeEnhancement = AgeEnhancement.reindex(columns = NewAgeEnhancementColumnOrder)
# Removing rows within the dataset with empty cells
AgeEnhancement = AgeEnhancement.dropna(axis = 0)
# Exporting dataset
AgeEnhancement.to_csv('data/EnhancedDatasets/AgeEnhancement.csv', index = False)


## Weather Enhancement ##

# Loading both NoShowData1 & NoShowData2, and combining it with practiceLocation to obtain pratice_zipcodes
WeatherData1 = pandas.merge(NoShowData1, practiceLocation, on = 'practice_id', how = 'inner')
WeatherData1 = WeatherData1.dropna(axis = 0)
WeatherData2 = pandas.merge(NoShowData2, practiceLocation, on = 'practice_id', how = 'inner')
WeatherData2 = WeatherData2.dropna(axis = 0)
# Loading Weather Enhancements Datatset for 19128 Zipcode between 10-29-2019 & 12-1-2021
# Used 19128 Zipcode because it was the most frequent zipcode in WeatherData2 Dataset (11883 Rows)
WeatherData_19128 = pandas.read_csv('data/weatherconditions.csv')
# Renaming columns names to align with previous datasets
WeatherData_19128.rename(columns = {'zipcode':'practice_zipcode'}, inplace = True)
WeatherData_19128.rename(columns = {'datetime':'appointment_date'}, inplace = True)
WeatherData_19128.rename(columns = {'icon':'weather_icon'}, inplace = True)
# Reformatting column datatypes befor merging
WeatherData_19128['practice_zipcode'] = WeatherData_19128['practice_zipcode'].astype(str)
WeatherData_19128['appointment_date'] = pandas.to_datetime(WeatherData_19128['appointment_date'])
WeatherData2['appointment_date'] = pandas.to_datetime(WeatherData2['appointment_date'])
# Merging/Enhancing NoShowData2 with WeatherData2 
EnhancingWeatherData = pandas.merge(WeatherData2, WeatherData_19128, on = ['practice_zipcode', 'appointment_date'], how = 'inner')
# Combining EnhancingWeatherData with WeatherData1
WeatherEnhancement = pandas.concat([EnhancingWeatherData, WeatherData1], ignore_index=True, sort=False)
# Reordering WeatherEnhancement dataset columns
NewWeatherEnhancementColumnOrder = ['practice_id', 'patient_id', 'appointment_date', 
'appointment_yosi_noshow1', 'weather_icon']
WeatherEnhancement = WeatherEnhancement.reindex(columns = NewWeatherEnhancementColumnOrder)
# Exporting dataset
WeatherEnhancement.to_csv('data/EnhancedDatasets/WeatherEnhancement.csv', index = False)

# Process for WeatherEnhancement: WeatherData1 already has a "Weather Condition Column" So I chose to enhance WeatherData2 and then combine WeatherData1 & WeatherData2 
# and assess the combined WeatherEnhancement Dataset

### Merging Each "_Enhancment.csv" into a master.csv file
master = pandas.concat([DistanceEnhancement, AgeEnhancement, WeatherEnhancement], ignore_index=True, sort=False)
master.drop_duplicates(subset=['patient_id'], keep=False)
master.to_csv('data/master.csv', index = False)

