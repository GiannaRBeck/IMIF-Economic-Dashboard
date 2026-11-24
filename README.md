# Important Macroeconomic Indicators (IMIF)

**CIT 261: Intro to Coding Using Python**

**Team Members:** Gianna Beck and Jaida Marcus

## Project Description

The purpose of this project was to create an interactive application that allows users to view important macroeconomic indicators without having to collect and calculate the data themselves. We developed the application using Python and Streamlit. The program retrieves data from the Federal Reserve Economic Data (FRED) database, calculates the selected indicator, and displays the results in an interactive graph. The application focuses on three main areas of the economy: inflation, the labor market, and output.

## How to Run the Program

We used GitHub and Streamlit Community Cloud to make our application available online.

To run the program, open the following link in a web browser:

https://imif-economic-dashboard.streamlit.app/

Users do not need to install Python or any additional libraries to use the online application.

## How to Use the Program

1. Open the application using the link above.
2. Select a section: Inflation, Labor Market, or Output.
3. Select an economic indicator from the dropdown menu.
4. If an inflation indicator is selected, choose either the 3-month or 6-month annualized calculation.
5. View the graph and hover over the line to see the indicator's value for a specific date.
6. Use the **Check a Specific Date** feature to find the value of an indicator for a selected month or quarter.
7. View the **Description** and **Calculation** sections to learn more about the indicator and how it was calculated.
8. Download the data as a CSV file or the graph as a PNG image.

## Libraries Used

- **Streamlit:** Used to create the graphical user interface (GUI), including the dropdown menus, buttons, and other interactive features.
- **Pandas:** Used to organize, calculate, and manipulate the economic data.
- **pandas_datareader:** Used to retrieve economic data directly from FRED.
- **Altair:** Used to create the interactive graphs displayed on the application.

## Team Contributions

### Gianna Beck

- Created the main structure of the Python program.
- Developed the dropdown menus using lists, dictionaries, and conditional statements.
- Created the functions used to retrieve data from FRED, calculate the indicators, and display the graphs.
- Developed the feature that allows users to check a specific date.
- Implemented exception handling to account for potential errors.
- Worked on the formatting and appearance of the application.
- Made the application available online using GitHub and Streamlit Community Cloud.

### Jaida Marcus

- Worked on the dictionary containing the descriptions of each economic indicator.
- Created the expandable sections that display the descriptions and calculations.
- Worked on displaying the links to the FRED data sources using a for loop.
- Developed the feature that allows users to download the data as a CSV file.
- Tested the different features of the application and documented the results.
- Assisted with the project documentation.

Both team members contributed to the planning of the project and the development of the final presentation.

## Data Sources

All economic data used in this application are retrieved from the Federal Reserve Economic Data (FRED) database.

https://fred.stlouisfed.org/

The data are originally collected by the Bureau of Economic Analysis (BEA), Bureau of Labor Statistics (BLS), and U.S. Census Bureau. Links to the specific data series used for each indicator are provided within the application.

## Limitations

- An internet connection is required to retrieve data from FRED.
- The availability of data depends on when new economic data are released.
- If data cannot be retrieved or are not available for a selected date, the program displays an error message.
