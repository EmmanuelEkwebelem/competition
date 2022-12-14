import pandas 
import streamlit 

DistanceEnhancement = pandas.read_csv('data/master/DistanceEnhancement.csv')
AgeEnhancement = pandas.read_csv('data/master/AgeEnhancement.csv')
WeatherEnhancement = pandas.read_csv('data/master/WeatherEnhancement.csv')

AgeEnhancement_Y = (AgeEnhancement[AgeEnhancement["appointment_yosi_noshow1"] == 'Y'])
AgeEnhancement_N = (AgeEnhancement[AgeEnhancement["appointment_yosi_noshow1"] == 'N'])
DistanceEnhancement_Y = (DistanceEnhancement[DistanceEnhancement["appointment_yosi_noshow1"] == 'Y'])
DistanceEnhancement_N = (DistanceEnhancement[DistanceEnhancement["appointment_yosi_noshow1"] == 'N'])
WeatherEnhancement_Y = (WeatherEnhancement[WeatherEnhancement["appointment_yosi_noshow1"] == 'Y'])
WeatherEnhancement_N = (WeatherEnhancement[WeatherEnhancement["appointment_yosi_noshow1"] == 'N'])


# Header
streamlit.header('AHI Competition Visualalization')

### DistanceEnhancement Dataset ###
# Dropdown Checkbox to View Data
if streamlit.checkbox('Distanced Enhanced No Show Dataset'):
    streamlit.dataframe(DistanceEnhancement)
                        
### AgeEnhancement Dataset ###
# Dropdown Checkbox to View Data
if streamlit.checkbox('Age Enhanced No Show Dataset'):
    streamlit.dataframe(AgeEnhancement)    

### WeatherEnhancement Dataset ###
# Dropdown Checkbox to View Data
if streamlit.checkbox('Weather Enhanced No Show Dataset'):
    streamlit.dataframe(WeatherEnhancement)    

