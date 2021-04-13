#!/usr/bin/python3

import re, sys

# cron syntax "5 5 5 5 5 /command/test"

cron = sys.argv[1]
splitCron = cron.split()

# # Define the function used to parse each cron argument
def test(value, field):
    start = 0
    step = 1
    params = []
    if field == 'hours':
        end = 25
    elif field == 'minutes':
        end = 60
    elif field == 'dayofmonth':
        end = 31
    elif field == 'months':
        end = 13
    elif field == 'daysofweek':
        end = 7
    if "/" in value:
        step = int(value.split("/")[1]) 
    elif "-" in value:
        step = 1
        start = int(value.split("-")[0])
        endCustom = int(value.split("-")[1])    
        if endCustom <= end:
            end = endCustom
        else:
            print("Max value ", end, " exceeded!")
            return 0
    elif "*" in value and "/" not in value:
        step = 1
        start = 1
    elif "," in value:
        x = value.split(',')
        print(field, *x)
        return 0
    else:
        endCustom = int(value)
        if endCustom > end:
            print('błąd')
            return 0           
        print(field, value)
        return 0
    for i in range(start, end, step):
        params.append(i)
    print(field, "\t\t", *params)

test(splitCron[0],'minutes')
test(splitCron[1],'hours')
test(splitCron[2],'dayofmonth')
test(splitCron[3],'months')
test(splitCron[4],'daysofweek')
print('command', splitCron[5])