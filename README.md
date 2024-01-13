# Extreme-Weather-Impact-Energy-Generation

## The Great Freeze - Texas Energy Prices Across Sectors:
- There are defining moments in time, and the State of Texas had an extreme weather outlier during February, 2021. This inspired JARDO Analytics, Inc. to determine how such extreme weather conditions impact energy consumption and prices in Texas.
- We used the [Energy Information Administration](<https://www.eia.gov/opendata/>) API to request Texas energy data between January 2020 and January 2023. The EIA “collects, analyzes, and disseminates independent and impartial energy information to promote sound policymaking, efficient markets, and public understanding of energy and its interaction with the economy and the environment.” <https://www.eia.gov/opendata/>

- Our process:
  1. Make Initial calls to the EIA API
  2. Analyze, transform, and export JSON results
  3. Create charts using cleaned data
  4. Create a PSQL database to store the data
  5. Develop a Flask API to connect to the database and power the interactive webpage
  6. Design interactive webpage
 
- Two of the notable conclusions we made are:
  - The City Gate Price was greater during the freeze than the Residential Consumers Price, which is an anomaly since the City Gate Price is a component for calculating the Residential Consumers Price. The extreme weather conditions caused the transportation of fuel to be significantly more expensive, even if the fuel was not transferred to the residents.
  - The Petroleum sector showed spikes in petroleum consumption during the last two freezes in Texas, skipping over Winter 2021, in which there was no extreme freeze.

![Natural Gas Prices](https://github.com/DataScience-Skills/Project-3-Visualizing-Data/raw/main/images/ng_prices.png)

![Petroleum Consumption](https://github.com/DataScience-Skills/Project-3-Visualizing-Data/raw/main/images/petroleum_consumption.png)


