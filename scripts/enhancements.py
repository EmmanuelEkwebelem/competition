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

### Assessment Results ###
# There are more rows with missing data than there are columns with missing data.
# It would be more beneficial to enhance the NoShowData2 (100000 Rows) vs NoShowData1 (3265 Rows). Despite the fact that NoShowData1 has more columns (30) than NoShowData2 (19)
# Goal: Assess relationship between No Shows and [Age], [Distance], [Weather].





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
# Reordering dataset columns
NewDistanceEnhancementColumnOrder = ['practice_id', 'practice_name', 'practice_address1', 'practice_zipcode', 'patient_id','patient_zipcode_x', 'appointment_yosi_noshow1']
# Calculating distance between patient zipcode and practice zipcode in miles
DistanceEnhancement = DistanceEnhancement.reindex(columns = NewDistanceEnhancementColumnOrder)
def get_distance(x, y):
    usa_zipcodes = pgeocode.GeoDistance('us')
    distance_in_kms = usa_zipcodes.query_postal_code(x.values, y.values)
    return distance_in_kms
DistanceEnhancement['patient_distance_from_practice (miles)'] = get_distance(DistanceEnhancement['patient_zipcode_x'], DistanceEnhancement['practice_zipcode'])
DistanceEnhancement['patient_distance_from_practice (miles)'] = DistanceEnhancement['patient_distance_from_practice (miles)'] * 0.621371
# Removing rows with empty values in patient_distance_from_practice (miles) column
DistanceEnhancement['patient_distance_from_practice (miles)'].replace('', numpy.nan, inplace = True)
DistanceEnhancement.dropna(subset=['patient_distance_from_practice (miles)'], inplace = True)
DistanceEnhancement['patient_distance_from_practice (miles)'] = DistanceEnhancement['patient_distance_from_practice (miles)'].round(2)
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
NewAgeEnhancementColumnOrder = ['patient_id', 'patient_dob',
       'patient_age', 'patient_age_group', 'appointment_yosi_noshow1']
AgeEnhancement = AgeEnhancement.reindex(columns = NewAgeEnhancementColumnOrder)
# Exporting dataset
AgeEnhancement.to_csv('data/EnhancedDatasets/AgeEnhancement.csv', index = False)


## Weather Enhancement ##

# Loading both NoShowData1 & NoShowData2, and combining it with practiceLocation to obtain pratice_zipcodes
WeatherData1 = pandas.merge(NoShowData1, practiceLocation, on = 'practice_id', how = 'inner')
WeatherData1 = WeatherData1.dropna(axis = 0)
WeatherData2 = pandas.merge(NoShowData2, practiceLocation, on = 'practice_id', how = 'inner')
WeatherData2 = WeatherData2.dropna(axis = 0)
# Re-ordering dataset columns
NewWeatherData1ColumnOrder =  ['practice_id', 'practice_zipcode', 'patient_id', 
'appointment_start_time_groupper','appointment_date', 'weather_icon', 'appointment_yosi_noshow1']
WeatherData1 = WeatherData1.reindex(columns = NewWeatherData1ColumnOrder)
NewWeatherData2ColumnOrder = ['practice_id', 'practice_zipcode', 'patient_id', 
'appointment_start_time_groupper','appointment_date', 'appointment_yosi_noshow1']
WeatherData2 = WeatherData2.reindex(columns = NewWeatherData2ColumnOrder)
# Loading Weather Enhancements Datatset for 19128 Zipcode between 10-29-2019 & 12-1-2021
# Used 19128 Zipcode because it was the most frequent zipcode is WeatherData2 Dataset (11883 Rows)
WeatherData_19128 = pandas.read_csv('data/weatherconditions.csv')
# Renaming columns names to align with previous datasets
WeatherData_19128.rename(columns = {'zipcode':'practice_zipcode'}, inplace = True)
WeatherData_19128.rename(columns = {'datetime':'appointment_date'}, inplace = True)
WeatherData_19128.rename(columns = {'icon':'weather_icon'}, inplace = True)
# Reformatting column datatypes for merger
WeatherData_19128['practice_zipcode'] = WeatherData_19128['practice_zipcode'].astype(str)
WeatherData_19128['appointment_date'] = pandas.to_datetime(WeatherData_19128['appointment_date'])
WeatherData2['appointment_date'] = pandas.to_datetime(WeatherData2['appointment_date'])
# Merging/Enhancing NoShowData2 with WeatherData2 
EnhancingWeatherData = pandas.merge(WeatherData2, WeatherData_19128, on = ['practice_zipcode', 'appointment_date'], how = 'inner')
# Combining EnhancingWeatherData with WeatherData1
WeatherEnhancement = pandas.concat([EnhancingWeatherData, WeatherData1], ignore_index=True, sort=False)
# Exporting dataset
WeatherEnhancement.to_csv('data/EnhancedDatasets/WeatherEnhancement.csv', index = False)

# Process Explained: WeatherData1 already has a "Weather Condition Column" So I chose to enhance WeatherData2 and then combine WeatherData1 & WeatherData2 and assess the combined WeatherEnhancement Dataset

### I initially seperated Each "_Enhancment.csv" as it made it easier for me to analyze/understand
### I combined all 3 Enhancement files into a master csv in this script

master = pandas.concat([DistanceEnhancement, AgeEnhancement, WeatherEnhancement], ignore_index=True, sort=False)
master.drop_duplicates(subset=['patient_id'], keep=False)

master.to_csv('data/master.csv', index = False)
print()
