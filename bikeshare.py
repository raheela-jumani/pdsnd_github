import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = input("Enter the city name Chicago, New York city, Washington:\n ").lower()
            if city in ['chicago', 'washington', 'new york city']:
                break
            else:
                print("\nError: An incorrect value for city has been entered. Please enter city as Chicago, Washington or New York City.\n")
        except (ValueError, TypeError):
            print("\nIncorrect Value\n")
        
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input("\nEnter the month? January, February, March, April, May or June or all:\n ").lower()
            if month in ["january", "february", "march", "april", "may", "june", "all"]:
                break
            else:
                print("\nError: An incorrect value for month has been entered. Please try January, February, March, April, May, June or type All\n")          
        except (ValueError, TypeError):
            print("\nIncorrect Value\n")
            
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input("\nEnter the day of the week? Sunday, Monday, Tuesday, Wednesday, Thursday, Friday or Saturday or All:\n ").lower()
            if day in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"]:
                break
            else:
                print("\nError: An incorrect value for day has been entered. Please try Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or type All\n")
        except (ValueError, TypeError):
            print("\nIncorrect Value\n")

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day.title()]

    return df

def time_stats(df, _city, _month, _day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    
    start_time = time.time()
    df['hour'] = df['Start Time'].dt.hour

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print("Most popular month of travel: {}, Filterred by City: {}, Month: {}, Day: {}".format(popular_month, _city.title(), _month.title(), _day.title()))
    
    # TO DO: display the most common day of week
    popular_day = df['day'].mode()[0]
    print("\nMost popular day to travel is: {}, Filterred by City: {}, Month: {}, Day: {}".format(popular_day, _city.title(), _month.title(), _day.title()))
    
    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    popular_hour_count = df.loc[df.hour == popular_hour, 'hour'].count()
    print("\nMost popular hour of travel: {}, Count: {}, Filterred by City: {}, Month: {}, Day: {}".format(popular_hour, popular_hour_count, _city.title(), _month.title(), _day.title()))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df, _city, _month, _day):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    popular_start_station_count = df.loc[df['Start Station'] == popular_start_station, 'Start Station'].count()
    print("Most popular start station: {}, Count: {}, Filterred by City: {}, Month: {}, Day: {}".format(popular_start_station, popular_start_station_count,  _city.title(), _month.title(), _day.title()))
    
    # TO DO: display most commonly used end station
    popular_end_station_count = df.loc[df['End Station'] == df['End Station'].mode()[0], 'End Station'].count()
    print("\nMost popular end station is: {}, Count: {}, Filterred by City: {}, Month: {}, Day: {}".format(popular_end_station, popular_end_station_count,  _city.title(), _month.title(), _day.title()))

    # TO DO: display most frequent combination of start station and end station trip
    df['Combination'] = df['Start Station'] + " to " + df['End Station']
    popular_combination = df['Combination'].mode()[0]
    popular_combination_count = df.loc[df['Combination'] == popular_combination, 'Combination'].count()
    print("\nMost popular start and end station destination is: {}, Count: {}, Filterred by City: {}, Month: {}, Day: {}".format(popular_combination, popular_combination_count, _city.title(), _month.title(), _day.title()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df, _city, _month, _day):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total = df['Trip Duration'].sum()
    total_count = df['Trip Duration'].count()
    print("\nTotal trip duration is: {}seconds, Count: {}, Filterred by City: {}, Month: {}, Day: {}".format(total, total_count, _city.title(), _month.title(), _day.title()))
    
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    mean_count = df['Trip Duration'].count()
    print("\nAverage trip duration: {}seconds, Count: {}, Filterred by City: {}, Month: {}, Day: {}".format(mean_travel_time, mean_count, _city.title(), _month.title(), _day.title()))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df, _city, _month, _day):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("\nUser Types:\n {} \nFilterred by City: {}, Month: {}, Day: {}".format(user_types, _city.title(), _month.title(), _day.title()))
    
    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print("\nGender Breakdown:\n {}\nFilterred by City: {}, Month: {}, Day: {}".format(gender_counts, _city.title(), _month.title(), _day.title()))
    else:
        print("\n{} city does not have information on Gender".format(_city.title()))
              
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
              earliest_datofbirth = int(df['Birth Year'].min())
              most_recent_dateofbirth = int(df['Birth Year'].max())
              most_common_birthyear = int(df['Birth Year'].mode()[0])
              print("\nEarliest Year of Birth: {}, Most Recent Year of Birth: {}, Most Common Year of Birth: {}, Filterred by City: {}, Month: {}, Day: {}".format( earliest_datofbirth, most_recent_dateofbirth, most_common_birthyear, _city.title(), _month.title(), _day.title()))
    else:
              print("\n{} city does not have information on Birth Year".format(_city.title()))
            
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def view_data(df, _city, _month, _day):
    """Display the rows of data"""
    n = 0
    while True:
        try:
            check_data = input("\nWould you like to view individual trip data? Type 'Yes' or 'No'?\n ").lower()
            if check_data == "yes":
                display = df.iloc[n:n+5,:-4].to_dict('index')
                for x in display:
                    print(x)
                    for y in display[x]:
                        print(y,":",display[x][y])
                    print("\n")
                n = n + 5
            elif check_data == "no":
                print("\nRequest for no data display")
                break
            else:
                print("\nIncorrect value has been entered\n")
        except (ValueError, TypeError):
            print("\nIncorrect Value\n")
  
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, city, month, day)
        station_stats(df, city, month, day)
        trip_duration_stats(df, city, month, day)
        user_stats(df, city, month, day)
        view_data(df, city, month, day)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
            
if __name__ == "__main__":
	main()