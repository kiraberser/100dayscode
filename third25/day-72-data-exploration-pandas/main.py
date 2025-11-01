import pandas as pd 
df = pd.read_csv('salaries_by_college_major.csv')

#print(df.head())
clean_df = df.dropna()

print(f"There are {clean_df.shape[0]} rows, and {clean_df.shape[1]} columns")

print(f"Columns names:",)
for n in df.columns: 
    print('- ',n)

#print(f"Nan values {df.isna()}")
#print(clean_df.tail())

#Accessing Columns and Individual cells in a Dataframe 

#print(f"The most amount salary that someone can reach when start their career is: {clean_df['Starting Median Salary'].max()}")

#print(f"Index of the max amount starting median salary: {clean_df['Starting Median Salary'].idxmax()} and is {clean_df['Undergraduate Major'][43]}\n")

#print(f"Information about {clean_df['Undergraduate Major'][43]}\n {clean_df.loc[43]}")

major = clean_df['Undergraduate Major']

print('What college major has the highest mid-career salary? How much do graduates with this major earn? (Mid-career is defined as having 10+ years of experience).')
mid_career = clean_df['Mid-Career Median Salary']
index_mid = mid_career.idxmax()
print(f"The most amount salary that someone can reach when is in the mid of their career is: {mid_career.max()}")
print(f"Index of the max amount mid median salary: {index_mid} and is {major[index_mid]}\n")
print(f"Information about {mid_career[index_mid]}\n {clean_df.loc[index_mid]} \n")

print('Which college major has the lowest starting salary and how much do graduates earn after university?')
start_career = clean_df['Starting Median Salary']
index_start = start_career.idxmin()
print(f"The less amount of salary that someone can reach when is in the mid of their career is: {start_career.min()}")
print(f"Index of the less amount start salary: {index_start} and is {major[index_start]}\n")
print(f"Information about {start_career[index_start]}\n {clean_df.loc[index_start]}\n")

print('Which college major has the lowest mid-career salary and how much can people expect to earn with this degree? ')
mid_career_low = clean_df['Mid-Career Median Salary']
index_mid_low = mid_career_low.idxmin()
print(f"The less amount of salary that someone can reach when is in the mid of their career is: {mid_career_low.min()}")
print(f"Index of the The less amount of salary mid median salary: {index_mid_low} and is {major[index_mid_low]}\n")
print(f"Information about {mid_career_low[index_mid_low]}\n {clean_df.loc[index_mid_low]}")

#Sorting values & Adding columns

#Lowest risk major

#low_risk = clean_df['Mid-Career 90th Percentile Salary'].subtract(clean_df['Mid-Career 10th Percentile Salary']) 
#
#clean_df.insert(1, 'Spread', low_risk)
#print(clean_df.head())
#
#low_risk = clean_df.sort_values('Spread', ascending=False)
#print(low_risk[['Undergraduate Major', 'Spread']].head())
#
#high_risk_mid_90 = clean_df.sort_values('Mid-Career 90th Percentile Salary', ascending=False)
#print(high_risk_mid_90[['Undergraduate Major', 'Mid-Career 90th Percentile Salary']].head())
#
#high_risk = clean_df.sort_values('Mid-Career Median Salary', ascending=False)
#print(high_risk[['Undergraduate Major', 'Mid-Career Median Salary']].head())


print(clean_df.groupby('Group').count())

pd.options.display.float_format = '{:,.2f}'.format

print(clean_df.groupby('Group').mean(numeric_only=True))


