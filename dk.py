import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city = input('Which City do you want to explore?').lower()
        if city not in ('chicago', 'new york city', 'washington'):
            print("We either have no data for this city or you must have misspelled it.")
        else:
            print(city)
            break

    # get user input for month (all, january, february, ... , june)

    while True:
        month = input('Which month do you want to explore?').lower()
        if month not in ('all', 'january', 'february', 'march','april', 'may', 'june'):
            print("We either have no data for this month or you must have misspelled it.")
        else:
            print(month)
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Which day do you want to explore?').lower()
        if day not in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
            print("You must have misspelled the day, please try again.")
        else:
            print(day)
            break

    ### 

    print('-' * 40)
    return city, month, day


def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])

    return df
    # df_by_month = df['']
    # Missing values (Nan) beruecksichtigen!

    # Columns: + Beispielwerte
    # Unnamed: 0  : 1423854                 dtype: int
    # Start Time: 2017-06-23 15:09:32       dtype: object
    # End Time: 2017-06-23 15:14:53         dtype: object
    # Trip Duration: 321                    dtype: int
    # Start Station: Wood St & Hubbard St   dtype: object
    # End Station: Damen Ave & Chicago Ave  dtype: object
    # User Type: Subscriber                 dtype: object
    # Gender: Male/Female/ Nan              dtype: object
    # Birth Year: 1992.0                    dtype: float

    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # add new columns


    # df['Start Time'] = pd.to_datetime(df['Start Time'])
    # df['hour'] = df['Start Time'].dt.hour


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()  # variable to show how long the function takes

    # display the most common month

    df['Start Time'] = pd.to_datetime(df['Start Time'])  # changes values of column 'Start Time' into datetime-format
    # change of format is needed to pandas methods dt.month etc.
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]

    print('Most popular month:', popular_month)

    # display the most common day of week

    df['day'] = df['Start Time'].dt.day
    popular_day = df['day'].mode()[0]

    print('Most popular day:', popular_day)

    # display the most common start hour

    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]

    print('Most popular hour:', popular_hour)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most popular start station:', popular_start_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most popular end station:', popular_end_station)

    # display most frequent combination of start station and end station trip

    popular_start_end_station = df[['Start Station', 'End Station']].mode()

    popular_start_end_station_start = popular_start_end_station['Start Station'][0]

    popular_start_end_station_end = popular_start_end_station['End Station'][0]

    print('Most popular start end station combination: ', popular_start_end_station_start,
          popular_start_end_station_end)


'''
df['station combination'] = pd.concat([df['Start Station'].dropna(), df['End Station'].dropna()])#.reindex_like(df)
popular_combination_of_stations = df ['station combination'].mode()[0]
print ('Most popular station combination:', popular_combination_of_stations)
'''

# dataframe["period"] = dataframe["Year"].map(str) + dataframe["quarter"]
start_time = time.time()
print("\nThis took %s seconds." % (time.time() - start_time))
print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    t_d_e=pd.to_datetime(df['End Time'])
    t_d_s=pd.to_datetime(df['Start Time'])
    t_d=t_d_e -t_d_s


    print('Duration time estimates:', t_d)
    print('Total time:', t_d.sum())  
    print('Mean:', t_d.mean())
    print('Median:', t_d.median())
    print('\nCalculating Trip Duration...\n')




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    U_T= df ['User Type'].value_counts()
    print(U_T)


    # Display counts of gender
    G_D= df ['Gender'].value_counts()
    print (G_D)
  


    # Display earliest, most recent, and most common year of birth

    BY= df ['Birth Year']

    BY1= df ['Birth Year'].mode()[0]

    print ('Oldest:', BY.min())

    print ('Youngest:', BY.max())

    print('Most common:', BY1)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        print(df.head(10))
        print(df.dtypes)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()

