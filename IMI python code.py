# streamlit run "C:\Users\giann\OneDrive\Desktop\Classes 2026-2027\CIT 261\Final Project\IMI python code.py"

#1
import streamlit as st
import pandas as pd
from pandas_datareader import data as web
import altair as alt

#2
st.set_page_config(page_title='IMIF')
st.markdown("""
<style>
.stApp {
    background-color: white;
    color: black;}
[data-testid="stAppViewContainer"] {background-color: white;}
[data-testid="stHeader"] {background-color: white;}
[data-testid="stExpander"] {background-color: white; color: black;}
[data-testid="stExpander"] summary {
    background-color: #F1F1F1; color: black;}
[data-testid="stExpander"] summary p {color: black;}
.stApp h1, .stApp h2, .stApp h3, .stApp p {color: black;}
.stButton button,
.stDownloadButton button {background-color: #252630; color: white !important;}
.stButton button p, .stDownloadButton button p {
    color: white !important;}
.stButton button:hover, .stDownloadButton button:hover {
    background-color: #40414F;
    color: white !important;}
.stButton button:hover p, .stDownloadButton button:hover p {
    color: white !important;}
</style> """, unsafe_allow_html=True)

#3
st.title('Important Macroeconomic Indicators')
section = st.selectbox('Section', ['Inflation', 'Labor Market','Output'])

if section == 'Inflation':
    category = st.selectbox('Category', ['PCE','CPI'])
    if category == 'PCE':
        choices = {'Headline PCE': 'PCEPI', 'Core PCE': 'PCEPILFE',
                   'DUMMY': 'THIS_FRED_SERIES_DOES_NOT_EXIST_987654321'}
    else:
        choices = {'Headline CPI': 'CPIAUCSL', 'Core CPI': 'CPILFESL'}
    calc = st.selectbox('Calculation', ['3-Month Annualized','6-Month Annualized'])
elif section == 'Labor Market':
    choices = {'Vacancies-to-Unemployed Ratio': 'JTSJOL'}
else:
    choices = {'Real GDP Growth (YoY)': 'GDPC1', 'Real GDP per Capita': 'GDPC1',
               'Real Wage Growth': 'CES0500000003'}
name = st.selectbox('Indicator', list(choices))
code = choices[name]

#4
def get_data(name, code, section, calc):
    if name == 'Vacancies-to-Unemployed Ratio':
        data = web.DataReader(['JTSJOL', 'UNEMPLOY'], 'fred', '2015-01-01')
        data[name] = data['JTSJOL'] / data['UNEMPLOY']
        sources = ['JTSJOL', 'UNEMPLOY']
        unit = 'Ratio'
        calculation = 'Job Openings / Unemployed Workers'

    elif name == 'Real GDP per Capita':
        data = web.DataReader('GDPC1', 'fred', '2015-01-01')
        pop = web.DataReader('POPTHM', 'fred', '2015-01-01')
        data = data.join(pop.resample('QS').mean())
        data[name] = data['GDPC1'] * 1000000 / data['POPTHM']
        sources = ['GDPC1', 'POPTHM']
        unit = 'Real Dollars per Person ($)'
        calculation = '(Real GDP * 1,000,000) / Population'

    elif name == 'Real Wage Growth':
        data = web.DataReader(['CES0500000003', 'CPIAUCSL'], 'fred', '2015-01-01')
        data['Real Wage'] = data['CES0500000003'] / data['CPIAUCSL'] * 100
        data[name] = data['Real Wage'].pct_change(12) * 100
        sources = ['CES0500000003', 'CPIAUCSL']
        unit = 'Percent (%)'
        calculation = '((Current Real Wage / Real Wage 12 Months Ago) - 1) * 100'
   
    else:
        data = web.DataReader(code, 'fred', '2015-01-01')
        sources = [code]
        unit = 'Percent (%)'
        
        if section == 'Inflation':
            if calc == '3-Month Annualized':
                data = ((data / data.shift(3)) ** 4 - 1) * 100
                calculation = '((Current Index / Index 3 Months Ago) ** 4 - 1) * 100'
            else:
                data = ((data / data.shift(6)) ** 2 - 1) * 100
                calculation = '((Current Index / Index 6 Months Ago) ** 2 - 1) * 100'
        else:
            data = data.pct_change(4) * 100
            calculation = '((Current GDP / GDP 4 Quarters Ago) - 1) * 100'
 
    if name in data.columns:
        data = data[[name]]
    else:
        data.columns = [name]
    data = data.dropna()
    return data, sources, unit, calculation

#5
descriptions = {
    'Headline PCE': 'The Personal Consumption Expenditures (PCE) Price Index is a measure of inflation produced by the Bureau of Economic Analysis (BEA). It tracks changes in the prices of goods and services consumed by households across the United States. Headline PCE includes food and energy. It is the Federal Reserve preferred inflation measure for evaluating its 2% inflation target.',
    'Core PCE': 'The Core Personal Consumption Expenditures (PCE) Price Index is a measure of underlying inflation produced by the Bureau of Economic Analysis (BEA). It measures changes in consumer prices while excluding food and energy, which tend to experience greater short-term price fluctuations. Economists use Core PCE to evaluate persistent inflationary pressures.',
    'Headline CPI': 'The Consumer Price Index (CPI) is a measure of inflation produced by the Bureau of Labor Statistics (BLS). It tracks changes in prices paid by urban consumers for a basket of goods and services, including housing, food, transportation, and medical care. Headline CPI includes food and energy and is widely used to evaluate changes in the cost of living.',
    'Core CPI': 'The Core Consumer Price Index (CPI) is a measure of underlying inflation produced by the Bureau of Labor Statistics (BLS). It measures changes in consumer prices while excluding food and energy. Removing these more volatile categories helps economists identify underlying inflation trends.',
    'Vacancies-to-Unemployed Ratio': 'The vacancies-to-unemployed ratio measures labor market tightness using data from the Bureau of Labor Statistics (BLS). It compares available job openings with the number of unemployed workers. A higher ratio indicates greater labor demand relative to available workers, while a lower ratio suggests a less tight labor market.',
    'Real GDP Growth (YoY)': 'Real Gross Domestic Product (GDP) measures inflation-adjusted economic output and is produced by the Bureau of Economic Analysis (BEA). Year-over-year growth compares output with the same quarter of the previous year. Economists use this indicator to evaluate economic growth and overall economic activity.',
    'Real GDP per Capita': 'Real GDP per capita measures inflation-adjusted economic output per person. It uses Real GDP from the Bureau of Economic Analysis (BEA) and population data from the Census Bureau. Economists use it to evaluate changes in average economic output over time.',
    'Real Wage Growth': 'Real wage growth measures changes in workers hourly earnings after adjusting for inflation. It uses average hourly earnings and CPI data from the Bureau of Labor Statistics (BLS). Positive real wage growth indicates that wages are rising faster than prices, improving purchasing power.'
}

#6
def show_graph(data, name, section, calc, unit, calculation, sources):
    if section == 'Inflation':
        title = name + ' - ' + calc
    else:
        title = name
    
    graph_data = data.reset_index()
    graph_data.columns = ['Date', 'Value']
    source_text = 'Source: FRED | ' + ', '.join(sources)
    graph = alt.Chart(graph_data).mark_line(
        color='#0072E5',
        strokeWidth=2
    ).encode(
        x=alt.X('Date:T', title='Date',
                axis=alt.Axis(grid=False, labelPadding=8, titlePadding=12)),
        y=alt.Y('Value:Q', title=unit,
                axis=alt.Axis(grid=False, labelPadding=8, titlePadding=12),
                scale=alt.Scale(zero=False)),
        tooltip=[
            alt.Tooltip('Date:T', title='Date'),
            alt.Tooltip('Value:Q', title=name, format='.3f')]
    ).properties(
        width='container',
        height=330,
        title=alt.TitleParams(text=title, anchor='start', color='white', 
            fontSize=18, offset=15))
    source = alt.Chart(
        pd.DataFrame({'text': [source_text]})
    ).mark_text(
        align='left', baseline='middle',color='white',
        fontSize=12,fontWeight='bold'
    ).encode(
        x=alt.value(0), y=alt.value(10), text='text:N'
    ).properties(
        width='container', height=20
    )
    graph = alt.vconcat(graph, source, spacing=18).configure(
        background='#0E1117',
        padding={'left': 15, 'right': 15, 'top': 35, 'bottom': 10}
    ).configure_axis(
        labelColor='white', titleColor='white', domainColor='#555555',
        tickColor='#555555', labelFontSize=11, titleFontSize=12
    ).configure_view(stroke=None)

    st.altair_chart(graph, use_container_width=True)

#7
    st.subheader('Check a Specific Date')
    selected_date = st.date_input(
        'Select a date',
        min_value=pd.Timestamp('1800-01-01').date())

    if st.button('Check Date'):
        date = pd.Timestamp(selected_date)
        if name == 'Real GDP Growth (YoY)' or name == 'Real GDP per Capita':
            # to_period('Q') identifies the selected quarter.
            period = date.to_period('Q')
            dates = data.index.to_period('Q')
        else:
            period = date.to_period('M')
            dates = data.index.to_period('M')
        if period in dates:
            value = data[name][dates == period].iloc[0]
            st.success(
                name + ' for ' + str(period) + ': ' +
                str(round(value, 3)) + ' ' + unit)
        else:
            # Displays an error if no observation exists.
            st.error('Date not available for this indicator. Please select another date.')

#8
    with st.expander('Description', expanded=True):
        st.write(descriptions[name])
    with st.expander('Calculation', expanded=True):
        st.write(calculation)
    # A for loop displays each FRED source link.
    for source in sources:
        st.markdown('Source: [FRED - ' + source + '](https://fred.stlouisfed.org/series/' + source + ')')

#9

if name not in choices:
    st.error('Please select a valid indicator.')
else:
    try:
        data, sources, unit, calculation = get_data(
            name, code, section, calc if section == 'Inflation' else ''
        )
        if data.empty:
            st.warning('No data is available for this indicator.')
        else:
            show_graph(
                data, name, section,
                calc if section == 'Inflation' else '',
                unit, calculation, sources
            )
            filename = 'IMIF_' + code + '.csv'
            csv = data.to_csv(index=True)
            st.download_button(
                label='Download Data to CSV', data=csv, 
                file_name=filename, mime='text/csv'
            )
    except Exception as e:
        st.error('FRED data could not be retrieved. Check the series code or connection.')

