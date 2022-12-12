import pandas 
import numpy 

NoShowData = pandas.read_csv('data/output_noshow1_balanced_2022-11-16.csv')
practiceLocation = pandas.read_csv('data/practiceLocations.csv')

### Cleaning NoShowData ###



# Removing "non-essential" coolumns
NoShowData.drop(['id', 'patient_id_2', 'appointment_id', 'appointment_status', 'appointment_yosi_noshow2', 
                 'custom_client','custom_client_site', 'client_site', 'data_collect', 'appointment_date_qt', 'appointment_date_month',
                 'appointment_date_year', 'appointment_start_time_hour', 'zipcode', 'geocode_zip', 'geocode_latitude', 'geocode_longitude', 'patient_age_groupper'], axis=1, inplace=True)
# Converting apporintment_duration from minutes to seconds, and appropriately renaiming it
NoShowData['appointment_duration'] = NoShowData['appointment_duration'] * 60
NoShowData.rename(columns={'appointment_duration':'appointment_duration (s)'}, inplace=True)
# Reformatting NoShowData Zip-Code to 5 digits only
NoShowData['patient_zipcode_x'] = NoShowData['patient_zipcode_x'].str[:5]
# Reformating NoShowData patient_age_groupper
NoShowData.loc[NoShowData['patient_age']<8, 'patient_age_group'] = 'child'
NoShowData.loc[NoShowData['patient_age'].between(8,12), 'patient_age_group'] = 'adolescent'
NoShowData.loc[NoShowData['patient_age'].between(13,17), 'patient_age_group'] = 'teen'
NoShowData.loc[NoShowData['patient_age'].between(18,23), 'patient_age_group'] = 'young adult'
NoShowData.loc[NoShowData['patient_age'].between(24,30), 'patient_age_group'] = 'mature adult'
NoShowData.loc[NoShowData['patient_age'].between(31,49), 'patient_age_group'] = 'adult'
NoShowData.loc[NoShowData['patient_age'].between(50,65), 'patient_age_group'] = 'senior'
NoShowData.loc[NoShowData['patient_age']>65, 'patient_age_group'] = 'elderly'
# Reformmating NoShowData column order 
NewColumnOrder = ['practice_id', 'patient_id', 'appointment_type', 'patient_dob', 'patient_age', 'patient_gender', 'patient_age_group', 'appointment_date_time', 'appointment_date', 'appointment_start_time',
                  'appointment_start_time_groupper', 'appointment_duration (s)', 'appointment_scheduled_date', 'appointment_last_modified_date', 'appointment_yosi_noshow1', 
                  'patient_zipcode_x',  'appintmentWithin3DayHoliday', 'appintmentWithin5DayHoliday', 'appintmentWithin7DayHoliday', 'weather_conditions', 'weather_icon', 
                  'geocode_city', 'geocode_county','geocode_state', 'geocode_stusab', 'geocode_lengthlife', 'geocode_healthybehaviors', 'geocode_clinicalcare', 'geocode_socioeconomic', 
                  'geocode_physicalenv']
NoShowData = NoShowData.reindex(columns=NewColumnOrder)
NoShowData.to_csv('data/test.csv', index = False)

### Assessing NoShowData ###



# Assessing NoShowData without missing rows cells
NoShowData1 = NoShowData
NoShowData1.replace('', numpy.nan, inplace=True)
NoShowData1 = NoShowData1.dropna(axis = 0)
print(NoShowData1.shape)
NoShowData1.to_csv('data/test1.csv', index = False)

# Assessing NoShowData without missing columns cells, with a threshold for missingness
NoShowData2 = NoShowData
NoShowData2.replace('', numpy.nan, inplace=True)
thresh = len(NoShowData2) * .2
NoShowData2.dropna(thresh = thresh, axis = 1, inplace = True)
print(NoShowData2.shape)
NoShowData2.to_csv('data/test2.csv', index = False)


### Assessment ###
# There is more rows with missing data than there are columns with missing data. 
# It would be more beneficial to enhance the NoShowData2 (10000 Rows) vs NoShowData1 (3265 Rows)


# UpdatedNoShowData = pandas.merge(NoShowData, practiceLocation, on = 'practice_id', how = 'left')
# UpdatedNoShowData.to_csv('data/testing.csv', index = False)
