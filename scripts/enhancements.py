import pandas 
import numpy 

NoShowData = pandas.read_csv('data/output_noshow1_balanced_2022-11-16.csv')
practiceLocation = pandas.read_csv('data/practiceLocations.csv')

print(NoShowData.isnull().any(axis=1).sum())
# Shortens dataset from 10000 to 3301 Rows, by removing rows with empty cells is several columns 
NoShowData.replace('', numpy.nan, inplace=True)
NoShowData.dropna(subset=['geocode_zip',
       'geocode_city', 'geocode_county', 'geocode_state', 'geocode_stusab',
       'geocode_latitude', 'geocode_longitude', 'geocode_lengthlife',
       'geocode_healthybehaviors', 'geocode_clinicalcare',
       'geocode_socioeconomic', 'geocode_physicalenv'], how='all', inplace=True)
print(NoShowData.isnull().any(axis=1).sum())

NoShowData.drop(['id', 'patient_id_2', 'appointment_id', 'appointment_status', 'appointment_date_time', 'appointment_yosi_noshow2', 
                 'custom_client','custom_client_site', 'client_site', 'data_collect', 'appointment_date_qt', 'appointment_date_month',
                 'appointment_date_year', 'appointment_start_time_hour', 'zipcode', 'geocode_zip'], axis=1, inplace=True)

NoShowData['appointment_duration'] = NoShowData['appointment_duration'] * 60
NoShowData.rename(columns={'appointment_duration':'appointment_duration (s)'}, inplace=True)

NoShowData['patient_zipcode_x'] = NoShowData['patient_zipcode_x'].str[:5]

NoShowData.to_csv('data/test.csv')
# UpdatedNoShowData = pandas.merge(NoShowData, practiceLocation, on = 'practice_id', how = 'left')


# 'patient_zipcode_x', remove last 5 characters, 
# 'patient_age_groupper', with own paramters

