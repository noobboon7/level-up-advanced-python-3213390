# Source of data: https://www.arrs.run/
# This dataset has race times for women 10k runners from the Association of Road Racing Statisticians

import re
import datetime

def get_data():
    """Return content from the 10k_racetimes.txt file"""
    with open('10k_racetimes.txt', 'rt') as file:
        content = file.read()
    return content

def get_rhines_times():
    """Return a list of Jennifer Rhines' race times"""
    races = get_data()
    racetimes = []
    for line in races.splitlines():
        if "Jennifer Rhines".lower() in line.lower():
            time = re.findall(r'\d{2}:\S+', line)[0]
            racetimes.append(time)
    return racetimes
def get_average():
    """Return Jennifer Rhines' average race time in the format:
       mm:ss:M where :
       m corresponds to a minutes digit
       s corresponds to a seconds digit
       M corresponds to a milliseconds digit (no rounding, just the single digit)"""
    racetimes = get_rhines_times()
    total_seconds  = datetime.timedelta()

    for time_str in racetimes:
        try:
            mins, secs, milly = re.split(r'[:.]', time_str)
            total_seconds += datetime.timedelta(minutes=int(mins), seconds=int(secs), milliseconds=int(milly))
        except ValueError:
            mins, secs = re.split(r'[:.]', time_str)
            total_seconds += datetime.timedelta(minutes=int(mins), seconds=int(secs))
    average_race_time = total_seconds // len(racetimes)
    
    return f'{average_race_time}'[2:9]