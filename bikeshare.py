import time
import pandas as pd
import numpy as np
# chicago = pd.read_csv('chicago.csv')
# new_york_city = pd.read_csv('new_york_city.csv')
# washington = pd.read_csv('washington.csv')
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities = ['chicago','new york city','washington']
months = ['all','january','february','march','april','may','june','july','august','september','october','november','december']
days = ['all','saturday','sunday','monday','tuesday','wednesday','thursday','friday']

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
    city = input('please select the name of the city you need to search for (chicago, new york city, washington)').lower()
    while city not in cities:
        print('invalid city name')
        city = input('please select the name of the city you need to search for (chicago, new york city, washington)').lower()
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('please select the name of the month you need to search for or type all to search for all months(all, january, february, ... , june)').lower()
    while month not in months:
        print('invalid month name')
        month = input('please select the name of the month you need to search for or type all to search for all months(all, january, february, ... , june)').lower()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('please select the name of the day you need to search for or type all to search for all week days(all, monday, tuesday, ... sunday)').lower()
    while day not in days:
        print('invalid day name')
        day = input('please select the name of the day you need to search for or type all to search for all week days(all, monday, tuesday, ... sunday)').lower()
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

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january','february','march','april','may','june','july','august','september','october','november','december']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month'] = pd.DatetimeIndex(df['Start Time']).month
    popular_month = df['month'].mode()[0]
    month_index = months[popular_month]
    print('Most Popular month:', month_index,'.')


    # TO DO: display the most common day of week
    df['day of week'] = pd.DatetimeIndex(df['Start Time']).day_name()
    popular_day = df['day of week'].mode()[0]
    print('Most Popular day of week:', popular_day,'.')


    # TO DO: display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour,'.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Popular Start Station:', popular_start_station,'.')

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Popular End Station:', popular_end_station,'.')


    # TO DO: display most frequent combination of start station and end station trip
    #concat
    most_frequent = df.groupby(['Start Station','End Station']).size().idxmax()
    print('Most Frequent Combination of Start Station and End Station trip:',most_frequent,'.')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    #sum
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time:',total_travel_time,'seconds.')
    # TO DO: display mean travel time
    #.mean()
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time:',mean_travel_time,'seconds.')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    #.count
    counts_user_types = df['User Type'].value_counts()
    print('Counts of User Type:',counts_user_types,'.')
    # TO DO: Display counts of gender
    counts_gender = df['Gender'].value_counts()
    print('Counts of Gender:',counts_gender,'.')

    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_year_of_birth = df['Birth Year'].min()
    print('The Earliest Year of Birth:',earliest_year_of_birth,'.')
    most_recent_year_of_birth = df['Birth Year'].max()
    print('The Most Recent Year of Birth:',most_recent_year_of_birth,'.')
    most_common_year_of_birth = df['Birth Year'].mode()
    print('The Most Common Year of Birth:',most_common_year_of_birth,'.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        if city != 'washington':
            user_stats(df)
        else:
            print('There is no user type or gender data to display for Washington City.')
        
        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
        start_loc = 0
        while view_data == 'yes':
            print(df.iloc[start_loc:(start_loc+5)])
            start_loc += 5
            view_data = input("Do you wish to continue?: ").lower()
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()