# Important Macroeconomic Indicators (IMIF)

## Project Description
IMIF is an interactive economic dashboard developed in Python using Streamlit. The application retrieves economic data from the Federal Reserve Economic Data (FRED) database and allows users to visualize important macroeconomic indicators, including inflation, labor market conditions, and output.

## How to Run the Program
The application is deployed online through Streamlit Community Cloud.

To access the program, open the following link in a web browser:

https://imif-economic-dashboard.streamlit.app/

No installation or additional software is required to use the online application.

## How to Use the Program
1. Open the application using the link above.
2. Select a section: Inflation, Labor Market, or Output.
3. Choose an economic indicator from the available dropdown menus.
4. For inflation indicators, select either the 3-month or 6-month annualized calculation.
5. View the interactive graph, which automatically updates based on your selections.
6. Use **Check a Specific Date** to retrieve an indicator's value for a selected month or quarter.
7. Expand the **Description** and **Calculation** sections for additional information.
8. Download the calculated data as a CSV file using the download button.

## Libraries Used
- **Streamlit:** Creates the interactive web application.
- **Pandas:** Organizes and calculates economic data.
- **pandas_datareader:** Retrieves data from FRED.
- **Altair:** Creates interactive graphs.

## Notes
- An internet connection is required to retrieve economic data from FRED.
- The availability of observations depends on FRED's data release schedule.
- The application includes error handling for unavailable data and invalid FRED series codes.
