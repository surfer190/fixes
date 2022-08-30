def get_age_in_days(age_in_years: int) -> int:
    '''
    Calculate the age in days
    '''
    return age_in_years * 365

def get_age_in_hours(age_in_years: int) -> int:
    '''
    Calculate the age in hours
    '''
    return age_in_years * 365 * 24

def get_age_in_seconds(age_in_years: int) -> int:
    '''
    Calculate the age in seconds
    '''
    return age_in_years * 365 * 24 * 60 * 60

if __name__ == "__main__":
    age = int(input('How old are you? '))
    age_expected = int(input('How old are you expected to be? '))
    
    print(get_age_in_days(age), 'days')
    print(get_age_in_hours(age), 'hours')
    print(get_age_in_seconds(age), 'seconds')
    
    years_left = age_expected - age

    print(get_age_in_days(years_left), 'days left')
    print(get_age_in_hours(years_left), 'hours left')
    print(get_age_in_seconds(years_left), 'seconds left')
