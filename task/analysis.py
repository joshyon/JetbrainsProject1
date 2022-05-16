# write your code here
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', 14)
#reading in data
general = pd.read_csv('/Users/joshuahyon/PycharmProjects/Data Analysis for Hospitals/Data Analysis for Hospitals/task/test/general.csv')
prenatal = pd.read_csv('/Users/joshuahyon/PycharmProjects/Data Analysis for Hospitals/Data Analysis for Hospitals/task/test/prenatal.csv')
sports = pd.read_csv('/Users/joshuahyon/PycharmProjects/Data Analysis for Hospitals/Data Analysis for Hospitals/task/test/sports.csv')
#rename columns to match each other
prenatal.rename(columns={'HOSPITAL': 'hospital', 'Sex': 'gender'}, inplace=True)
sports.rename(columns={'Hospital': 'hospital', 'Male/female': 'gender'}, inplace=True)
#combine dataframes in specific order
merged_df = pd.concat([general, prenatal], ignore_index=True)
merged_df = pd.concat([merged_df, sports], ignore_index=True)
#remove unnamed column
merged_df.drop(columns='Unnamed: 0', inplace=True)
#pick specific rows to change value
merged_df.loc[merged_df['hospital'] == 'prenatal', ['gender']] = 'f'
#change any values to another
merged_df.replace(to_replace='woman', value='f', inplace=True)
merged_df.replace(to_replace='man', value='m', inplace=True)
merged_df.replace(to_replace='female', value='f', inplace=True)
merged_df.replace(to_replace='male', value='m', inplace=True)
#remove empty rows
merged_df.dropna(axis=0, how='all', inplace=True)
#fill in empty values with 0 for specific columns
tests = {'bmi': 0, 'diagnosis' : 0, 'blood_test': 0, 'ecg': 0, 'ultrasound': 0, 'mri': 0, 'xray':0, 'children':0, 'months':0}
merged_df.fillna(tests, inplace=True)
#print shape of dataframe
#print(merged_df.shape)
#print random 20 rows
#print(merged_df.sample(n=20, random_state=30))
#get the number of entries grouped by hospital
#print(merged_df.groupby(['hospital']).count())
#print(merged_df.(10))
#pandas loc with multiple conditions
#print(merged_df.loc[(merged_df['hospital'] == 'general') & (merged_df['diagnosis'] == 'stomach')].count())
#print(merged_df.loc[(merged_df['hospital'] == 'sports') & (merged_df['diagnosis'] == 'dislocation')].count())
#general_stomach_share = round(150/461, 3)
#sports_dislocation_share = round(61/214, 3)
#median_age_general = merged_df.loc[(merged_df['hospital'] == 'general'), 'age'].median()
#median_age_sports = merged_df.loc[(merged_df['hospital'] == 'sports'), 'age'].median()
#difference = median_age_general - median_age_sports
#print(merged_df.loc[(merged_df['hospital'] == 'general') & (merged_df['blood_test'] == 't')].count())
#print(merged_df.loc[(merged_df['hospital'] == 'prenatal') & (merged_df['blood_test'] == 't')].count())
#print(merged_df.loc[(merged_df['hospital'] == 'sports') & (merged_df['blood_test'] == 't')].count())
#print('The answer to the 1st question is general')
#print(f'The answer to the 2nd question is {general_stomach_share}')
#print(f'The answer to the 3rd question is {sports_dislocation_share}')
#print(f'The answer to the 4th questions is {difference}')
#print('The answer to the 5th question is prenatal, 325 blood tests')

plt.hist(merged_df['age'], bins=[0, 15, 35, 55, 70, 80])
plt.show()
#print(merged_df.diagnosis.unique())
merged_df.groupby('diagnosis').size().plot(kind='pie', autopct='%.1f%%')
plt.show()
hospital_height = merged_df[['hospital', 'height']]
general_hospital_height = hospital_height.loc[hospital_height['hospital'] == 'general']
general_height = general_hospital_height[['height']]
sports_hospital_height = hospital_height.loc[hospital_height['hospital'] == 'sports']
sports_height = sports_hospital_height[['height']]
prenatal_hospital_height = hospital_height.loc[hospital_height['hospital'] == 'prenatal']
prenatal_height = prenatal_hospital_height[['height']]
plt.violinplot(general_height)
plt.violinplot(sports_height)
plt.violinplot(prenatal_height)

plt.show()
print('The answer to the 1st question: 15-35')
print('The answer to the 2nd question: pregnancy')
print("The answer to the 3rd question: It's because the sports hospital patients are very tall." )

