import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = [ 'all' , 'january', 'february', 'march', 'april', 'may', 'june']
days = [ 'all' , 'saturday' , 'sunday' , 'monday' , 'tuesday' , 'wednesday' , 'thursday' , 'friday'  ]

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
    cities = [ 'chicago' , 'new york city' , 'washington'  ]
    while True :
        city = input("enter name of the city to analyze: ").lower()
        if city in cities : 
            break
        else :
            print('please enter valid city ')
           

    # TO DO: get user input for month (all, january, february, ... , june)
    while True : 
        month = input("enter name of the month to filter by, or 'all' to apply no month filter: ").lower()
        if month in months :
            break
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True : 
        day = input("enter name of the day of week to filter by, or 'all' to apply no day filte: ").lower()
        if day in days : 
            break 
        else :
            print('please enter valid day ')    

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
    df['day_of_week'] = df['Start Time'].dt.weekday_name 
    df['hour'] = df['Start Time'].dt.hour
    
    
    if month != "all" :
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
        df = df[df["month"]==month]
    if day != "all" :
        df = df[df["day_of_week"]==day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("the most common month is : " , months[df['month'].mode()[0]])

    # TO DO: display the most common day of week
    print("\nthe most common day is : " , str(df['day_of_week'].mode()[0]))

    # TO DO: display the most common start hour
    print("\nthe most common start hour is : " , str(df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print( 'most commonly used start station : ' , df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print( 'most commonly used end station : ' , df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    print( 'most frequent combination of start station and end station trip : ' , (df['Start Station'] +' to '+ df['End Station']).mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print( ' total travel time is : ' , total_time/60 , 'minutes'  )

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print( ' mean travel time is : ' , mean_time/60 , 'minutes' )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df , city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('counts of user type is : ' , df['User Type'].value_counts()) 

    # TO DO: Display counts of gender
    if city == 'Chicago' or city == 'New York City' :
        print('counts of gender is : ' , df['Gender'].value_counts()) 

    # TO DO: Display earliest, most recent, and most common year of birth
    if city == 'Chicago' or city == 'New York City' :
        print( ' the earliest common year of birth : ' , int(df['Birth Year'].min()))
        print( ' the most recent common year of birth : ' , int(df['Birth Year'].max()))
        print( ' the most common year of birth : ' , int(df['Birth Year'].mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def display_row_data(df) : 
    print(df.head())
    start_loc = 0
    while True :
        view_data = input("Would you like to view 5 rows of data? Enter yes or no?")
        if view_data.lower() == 'yes' :
            start_loc += 5
            print(df.iloc[start_loc:start_loc+5])
            

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df , city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
