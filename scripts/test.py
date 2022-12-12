import pandas 
import numpy 

NoShowData = pandas.read_csv('data/output_noshow1_balanced_2022-11-16.csv')
practiceLocation = pandas.read_csv('data/practiceLocations.csv')

print(NoShowData.isnull().any(axis=1).sum())
print(NoShowData.shape)
NoShowData.replace('', numpy.nan, inplace=True)
NoShowData = NoShowData.dropna()
print(NoShowData.isnull().any(axis=1).sum())
print(NoShowData.shape)

NoShowData.to_csv('data/test.csv')
