# Bikeshare
> Created on 27 September 2019

**Bikeshare** is a python project which analyze US Bikeshare Data for three major cities in the United States—Chicago, New York City, and Washington.
First, It imports US Bikeshare data from csv files, asks several questions to the user to determine the city and timeframe on which we'll do data analysis.
Then after filtering the dataset, it displays the following information:

1. Popular times of travel (i.e., occurs most often in the start time)
   * most common month
   * most common day of week
   * most common hour of day

2. Popular stations and trip
   * most common start station
   * most common end station
   * most common trip from start to end (i.e., most frequent combination of start station and end station)

3. Trip duration
   * total travel time
   * average travel time

4. User info
   * counts of each user type
   * counts of each gender (only available for NYC and Chicago)
   * earliest, most recent, most common year of birth (only available for NYC and Chicago)

## Files used
* chicago.csv
* new_york_city.csv
* washington.csv

## Credits
The following links helped us a lot during the development:
* [Stack Overflow](https://stackoverflow.com/questions/47136436/python-pandas-convert-value-counts-output-to-dataframe)
* [Python Data Analysis Library API](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_json.html#pandas.DataFrame.to_json)