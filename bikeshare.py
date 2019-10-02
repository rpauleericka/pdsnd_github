import time
import pandas as pd
import numpy as np

# here are the data files that will be imported
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }
# First Question to be asked to filter the datasets by City
cityQuestion = 'Would you like to see data for Chicago, New York, or Washington?\n'
cities = ['chicago', 'new york','washington']
# Second Question to be asked to determine timeframe on which we 'll do data analysis: month, day, both or none
dateFilterQuestion = 'Would you like to filter the data by month, day, both or not at all? Type "none" for no time filter\n'
dateFilters = ['month','day','both','none']
# If the User chose month, we will ask the month
monthFilterQuestion = 'Which month? January, February, March, April, May, or June?\n'
months = ['january','february','march','april','may','june']
# If the User chose day, we will ask the day as an integer 1 = Sunday,2 = Monday,3 = Tuesday,4 = Wednesday,5 = Thursday,6 = Friday,7 = Saturday
dayFilterQuestion = 'Which day? Please type your response as an integer (e.g., 1 = Sunday,2 = Monday,3 = Tuesday,4 = Wednesday,5 = Thursday,6 = Friday,7 = Saturday)\n'
days = np.arange(1,8) # array of weekdays from 1 to 7

def toFind(question,answersArray,errormsg="Not a valid input! Please try again",typeMustBe="str"):
    """
    Asks user input which have a certain type.

    Returns:
        (str) question - question to ask the user
        (array) answersArray - array that contains the different answer to the question
        (str) errormsg - error message to print if the use enter an invalid input 
        (type) typeMustBe - type of the input that we expect from  the user by default string
    """
    answer = ""
    inputAnswer = ""
    while True:
        try:
            if type(typeMustBe) is str:
                inputAnswer =  str(input(question)).lower()
            elif type(typeMustBe) is int:
                inputAnswer =  int(input(question))
        except:
            print(errormsg) 
        else:
            if inputAnswer in answersArray:
                answer = inputAnswer
                break
            else:
                print(errormsg) 
    return answer

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    city = ""
    month = "all"
    day = "all"
    strConfirm = 'We will make sure to filter by '

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = toFind(cityQuestion,cities)
    print('Looks like you want to hear about {}! If this is not true, restart the program now!\n'.format(city))

    #get user input for date filter: month, day, both,none
    dateFilter = toFind(dateFilterQuestion,dateFilters)
    print(strConfirm+dateFilter+'\n')

    # print(dateFilter)
    if dateFilter == 'month':
        # get user input for month (all, january, february, ... , june)
        month = toFind(monthFilterQuestion,months)
    elif dateFilter == 'day':
        # get user input for day of week (all, monday, tuesday, ... sunday)
        day = toFind(question=dayFilterQuestion,answersArray=days,typeMustBe=7)
    elif dateFilter == 'both':
        # get user input for month (all, january, february, ... , june)
        month = toFind(monthFilterQuestion,months) 
        # get user input for day of week (all, monday, tuesday, ... sunday)
        day = toFind(question=dayFilterQuestion,answersArray=days,typeMustBe=7)
    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file for the given 'city' into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # create new column for start station and end station trip
    df['trip'] = df['Start Station'] + '-' +df['End Station']

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        #df = df[df['day_of_week'] == day.title()]
        
        # use the index of the days of the week list to get the corresponding dow name
        days_of_weeks = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
        day = days_of_weeks[day-1]
        # print(day)
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('Most common month...: {}, Count: {}'.format(months[int(df['month'].mode()[0])-1],len(df[df['month']==df['month'].mode()[0]])))

    # display the most common day of week
    print('Most common day of week...: {}, Count: {}'.format(df['day_of_week'].mode()[0],len(df[df['day_of_week']==df['day_of_week'].mode()[0]])))

    # display the most common start hour
    print('Most common start hour...: {},Count: {}'.format(df['hour'].mode()[0],len(df[df['hour']==df['hour'].mode()[0]])))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('Most common start station...: {},Count: {}'.format(df['Start Station'].mode()[0],len(df[df['Start Station']==df['Start Station'].mode()[0]])))

    # display most commonly used end station
    print('Most common end station...: {},Count: {}'.format(df['End Station'].mode()[0],len(df[df['End Station']==df['End Station'].mode()[0]])))

    # display most frequent combination of start station and end station trip
    # print(df[['Start Station','End Station','trip']])
    print('Most common start station and end station trip...: {}, Count:{}'.format(df['trip'].mode()[0],len(df[df['trip']==df['trip'].mode()[0]])))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('Total travel time...: {}'.format(df['Trip Duration'].sum()))

    # display mean travel time
    print('Mean travel time...: {}'.format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    if 'User Type' in df.columns:
        # Display counts of user types
        print('Counts of each user types...:\n {}'.format(df['User Type'].value_counts().to_frame('Counts')))
    elif 'User Type' not in df.columns:
        print('\nNo User Type data to share\n')

    if 'Gender' in df.columns:
        # Display counts of gender
        print('\nCounts of each gender...:\n {}'.format(df['Gender'].value_counts().to_frame('Counts')))
    elif 'Gender' not in df.columns:
        print('\nNo gender data to share\n')

    # Display earliest, most recent, and most common year of birth
    # print(df[['Birth Year']])
    if 'Birth Year' in df.columns:
        print('\nBirth Year:\n Earliest: {}\n Most recent: {}\n Most common year of birth: {}\n'.format(df['Birth Year'].min(),df['Birth Year'].max(),df['Birth Year'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    first = 0
    end = 5
    while True:
        city, month, day = get_filters()
        print('Just one moment... loading the data')
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        while True:
            inputRaw = input('\nWould you like to view individual trip data? Type yes or no.\n')
            if inputRaw.lower() == 'yes':
                # print next 5 rows of data from index first to end into json format
                print(df.iloc[first:end].to_json(orient='records',lines=True))
                first = end
                end +=5
            elif inputRaw.lower() == 'no':
                break
            else:
                print('Not a valid input! Please try again')
                continue
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()