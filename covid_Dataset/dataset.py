import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# 3shan yshof el file 
def read_data(file_name):
    return pd.read_csv(file_name)

#  to handle missing values in specified columns of a dataframe
def handle_missing_values(df, columns, fill_value=''):
    for column in columns:
        df[column] = df[column].fillna(fill_value)
    return df

#  to change the date format in specified columns of a dataframe
def change_date_format(df, columns, date_format="%Y-%m-%d"):
    for column in columns:
        df[column] = pd.to_datetime(df[column], format=date_format)
    return df

# Read data from various CSV files into dataframes
df_covid = read_data("covid_19_clean_complete.csv")
df_country = read_data("country_wise_latest.csv")
df_fgroup = read_data("full_grouped.csv")
df_world = read_data("worldometer_data.csv")  # Add missing dataframe
df_day = read_data("day_wise.csv")

# Handle missing values in specific columns of the dataframes
df_covid = handle_missing_values(df_covid, ['Province/State'])
df_world = handle_missing_values(df_world, ['WHO Region'])

# Change date format in specific columns of the dataframes
df_fgroup = change_date_format(df_fgroup, ["Date"])
df_day = change_date_format(df_day, ["Date"])

# Merge 'df_covid' and 'df_country' dataframes on multiple columns
merged_covcountry = pd.merge(df_covid, df_country, on=['Country/Region', 'Confirmed', 'Deaths', 'Recovered', 'Active'], how='inner')

# Plotting boxplot for 'Confirmed', 'Deaths', 'Recovered', 'Active' columns of the merged dataframe
fig, ax = plt.subplots(figsize=(12, 6))
merged_covcountry[['Confirmed', 'Deaths', 'Recovered', 'Active']].boxplot(ax=ax)

# Plotting area chart for 'Confirmed', 'Recovered', 'Deaths', 'Active' cases over time
fig = px.area(df_fgroup.melt(id_vars="Date", value_vars=['Confirmed', 'Recovered', 'Deaths', 'Active'], var_name='Case', value_name='Count'), 
              x="Date", y="Count", color='Case', height=600, width=700, title='Cases over time')
fig.update_layout(xaxis_rangeslider_visible=True)

# Plotting pie chart for top 10 countries with highest confirmed cases
country_totals = merged_covcountry.groupby('Country/Region')['Confirmed'].sum().nlargest(10)  # Define country_totals
plt.figure(figsize=(10,10))
plt.pie(country_totals, labels=country_totals.index, autopct='%1.1f%%', startangle=140)

# you must Close the window that is open to show all the data

plt.figure(figsize=(10,10))
plt.pie(country_totals, labels=country_totals.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title('Top 10 Countries with Highest Confirmed Cases (Modified)')
plt.show()
# Plotting stacked bar chart for 'Confirmed','Recovered', 'Deaths', 'Active' cases in US
us_cases = merged_covcountry[merged_covcountry['Country/Region'] == 'US'].groupby('Country/Region')[['Confirmed','Recovered', 'Deaths', 'Active']].sum().reset_index()  # Define us_cases
us_cases[['Confirmed','Recovered', 'Deaths', 'Active']].plot(kind='bar', stacked=True, figsize=(10, 6))

# Plotting bar chart for top 20 countries with highest confirmed cases worldwide
fig = px.bar(df_country.groupby('Country/Region')['Confirmed'].sum().nlargest(20).reset_index(), 
             x='Confirmed', y='Country/Region', title='Confirmed Cases Worldwide', 
             color='Confirmed', text='Confirmed', height=900, orientation='h')
fig.show()

# Plotting line chart for 'Confirmed', 'Deaths', 'Recovered', 'Active' cases over time globally
fig = px.line(df_fgroup, x="Date", y=["Confirmed", "Deaths", "Recovered", "Active"], 
              title='Analysis of Corona spread over time globally (Modified)', 
              color_discrete_sequence=px.colors.qualitative.Pastel)
fig.show()

# Plotting bar chart for 'Confirmed', 'Deaths', 'Recovered', 'Active' cases by WHO Region
who = df_country.groupby('WHO Region')[['Confirmed', 'Deaths', 'Recovered', 'Active']].sum().reset_index()
fig = px.bar(who.sort_values('Confirmed'), x='Confirmed', y="WHO Region", color='WHO Region', 
             text='Confirmed', orientation='h', width=700, color_discrete_sequence=px.colors.sequential.Plasma)
fig.update_layout(title='Confirmed Cases by WHO Region (Modified)', xaxis_title="", yaxis_title="", yaxis_categoryorder='total ascending')
fig.show()