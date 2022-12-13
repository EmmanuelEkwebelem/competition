import pandas 
import numpy 
import urllib.request
import ssl
import pgeocode
ssl._create_default_https_context = ssl._create_unverified_context





### Cleaning ###


# Removing "non-essential" columns
NoShowData = pandas.read_csv('data/output_noshow1_balanced_2022-11-16.csv')
NoShowData.drop(['id', 'patient_id_2', 'appointment_id', 'appointment_status', 'appointment_yosi_noshow2', 
                 'custom_client','custom_client_site', 'client_site', 'data_collect', 'appointment_date_qt', 'appointment_date_month',
                 'appointment_date_year', 'appointment_start_time_hour', 'zipcode', 'geocode_zip', 'geocode_latitude', 'geocode_longitude', 'patient_age_groupper'], axis=1, inplace=True)
# Assessing NoShowData without missing rows cells
NoShowData1 = NoShowData
NoShowData1.replace('', numpy.nan, inplace=True)
NoShowData1 = NoShowData1.dropna(axis = 0)
print(NoShowData1.shape)
# Assessing NoShowData without missing columns cells, with a threshold for missingness
NoShowData2 = NoShowData
NoShowData2.replace('', numpy.nan, inplace=True)
thresh = len(NoShowData2) * .2
NoShowData2.dropna(thresh = thresh, axis = 1, inplace = True)
print(NoShowData2.shape)

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
# Removing non-essential columns from Enhanced Dataset
DistanceEnhancement.drop([ 'patient_dob','patient_age', 'patient_gender', 'appointment_start_time_groupper', 
 'appointment_scheduled_date', 'appointment_last_modified_date', 'appintmentWithin3DayHoliday', 'appointment_type','appointment_date_time', 'appointment_duration', 'appointment_date', 'appointment_start_time', 'appintmentWithin5DayHoliday', 'appintmentWithin7DayHoliday',], axis=1, inplace=True)
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
DistanceEnhancement['patient_distance_from_practice (miles)'].replace('', numpy.nan, inplace=True)
DistanceEnhancement.dropna(subset=['patient_distance_from_practice (miles)'], inplace=True)
DistanceEnhancement['patient_distance_from_practice (miles)'] = DistanceEnhancement['patient_distance_from_practice (miles)'].round(2)
# Exporting dataset
DistanceEnhancement.to_csv('data/master/DistanceEnhancement.csv', index = False)


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
# Removing non-essential columns from Enhanced Dataset
AgeEnhancement.drop(['appointment_type','appointment_date_time', 'appointment_date', 'appointment_duration', 'appointment_start_time',
       'appointment_start_time_groupper', 'patient_gender', 'appointment_scheduled_date', 'appointment_last_modified_date', 'patient_zipcode_x',
       'appintmentWithin3DayHoliday', 'practice_id', 'appintmentWithin5DayHoliday', 'patient_zipcode_x', 'appintmentWithin7DayHoliday'], axis=1, inplace=True)
# Reordering dataset columns
NewAgeEnhancementColumnOrder = ['patient_id', 'patient_dob',
       'patient_age', 'patient_age_group', 'appointment_yosi_noshow1']
AgeEnhancement = AgeEnhancement.reindex(columns = NewAgeEnhancementColumnOrder)
# Exporting dataset
AgeEnhancement.to_csv('data/master/AgeEnhancement.csv', index = False)


## Weather Enhancement ##

# Reallocating data 
WeatherEnhancement = NoShowData2.copy()
print(WeatherEnhancement.columns)
