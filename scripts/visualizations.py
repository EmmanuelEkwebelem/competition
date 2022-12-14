import pandas 
import streamlit 

DistanceEnhancement = pandas.read_csv('data\EnhancedDatasets\DistanceEnhancement.csv')
AgeEnhancement = pandas.read_csv('data\EnhancedDatasets\AgeEnhancement.csv')
WeatherEnhancement = pandas.read_csv('data\EnhancedDatasets\WeatherEnhancement.csv')

AgeEnhancement_Y = (AgeEnhancement[AgeEnhancement["appointment_yosi_noshow1"] == 'Y'])
AgeEnhancement_N = (AgeEnhancement[AgeEnhancement["appointment_yosi_noshow1"] == 'N'])
DistanceEnhancement_Y = (DistanceEnhancement[DistanceEnhancement["appointment_yosi_noshow1"] == 'Y'])
DistanceEnhancement_N = (DistanceEnhancement[DistanceEnhancement["appointment_yosi_noshow1"] == 'N'])
WeatherEnhancement_Y = (WeatherEnhancement[WeatherEnhancement["appointment_yosi_noshow1"] == 'Y'])
WeatherEnhancement_N = (WeatherEnhancement[WeatherEnhancement["appointment_yosi_noshow1"] == 'N'])


# Header
streamlit.header('AHI Competition Visualalization')

### DistanceEnhancement Dataset ###
streamlit.subheader('Distance Enhanced Dataset')
# Dropdown Checkbox to View Data
if streamlit.checkbox('Distanced Enhanced No Show Dataset'):
    streamlit.dataframe(DistanceEnhancement)
streamlit.caption('Checkbox Dropdown for Distance Enhancement Dataset')
DistanceEnhancementVisual = DistanceEnhancement.groupby('patient_distance_from_practice_group')['appointment_yosi_noshow1'].value_counts().unstack()
streamlit.line_chart(DistanceEnhancementVisual)
streamlit.caption('This Figure Illustrates the Number of Show (N) vs No Show (Y) per Distance Group')

### AgeEnhancement Dataset ###
streamlit.subheader('Age Enhanced Dataset')
# Dropdown Checkbox to View Data
if streamlit.checkbox('Age Enhanced No Show Dataset'):
    streamlit.dataframe(AgeEnhancement) 
streamlit.caption('Checkbox Dropdown for Age Enhancement Dataset')   
AgeEnhancementVisual = AgeEnhancement.groupby('patient_age_group')['appointment_yosi_noshow1'].value_counts().unstack()
streamlit.line_chart(AgeEnhancementVisual)
streamlit.caption('This Figure Illustrates the Number of Show (N) vs No Show (Y) per Age Group')

### WeatherEnhancement Dataset ###
streamlit.subheader('Weather Enhanced Dataset')
# Dropdown Checkbox to View Data
if streamlit.checkbox('Weather Enhanced No Show Dataset'):
    streamlit.dataframe(WeatherEnhancement)    
streamlit.caption('Checkbox Dropdown for Weather Enhancement Dataset')
WeatherEnhancementVisual = WeatherEnhancement.groupby('weather_icon')['appointment_yosi_noshow1'].value_counts().unstack()
streamlit.line_chart(WeatherEnhancementVisual)
streamlit.caption('This Figure Illustrates the Number of Show (N) vs No Show (Y) per Daily Weather Condition')
