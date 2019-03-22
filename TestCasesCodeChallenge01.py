from formatTime import formatTime

# Test01: When number 1 is used as input return text "1 second"
assert formatTime(1) == "1 second"
print(formatTime(1))

# Test02: When 0 is used as input then it should return the test "none"
assert formatTime(0) == "none"
print(formatTime(0))

# Test03: When 2 is used as input then it should return the test "2 seconds"
assert formatTime(2) == "2 seconds"
print(formatTime(2))

# Test04: When 60 is used as input then it should return the test "1 minute"
assert formatTime(60) == "1 minute"
print(formatTime(60))

# Test05: When 61 is provided as input then the test should return "1 minute and 1 second"
assert formatTime(61) == "1 minute and 1 second"
print(formatTime(61))

# Test06: Test that a value of seconds that provides 1 minute but several seconds returns "1 minute and X seconds"
print(formatTime(80))
assert formatTime(80) == "1 minute and 20 seconds"

# Test07: Test a multiple number of minutes and multiple number of seconds produces a text "X minutes and Y seconds"
print(formatTime(350))
assert formatTime(350) == "5 minutes and 50 seconds"

# Test08: Check that when 3600 is used as input it returns 1 hour
print(formatTime(3600))
assert formatTime(3600) == "1 hour"

# Test 09: Test that a number of multiple number of hours shows the text hours in plural
print(formatTime(3600*7))
assert formatTime(3600*7) == "7 hours"

# Test 10: Test that a number of multiple number of hours and 1 minute shows a text like "10 hours and 1 minute"
print(formatTime(3600*10+60))
assert formatTime(3600*10+60) == "10 hours and 1 minute"

# Test 11: Test that a number of multiple number of hours and seconds shows a text like "x hours and y seconds"
print(formatTime(3600*10+15))
assert formatTime(3600*10+15) == "10 hours and 15 seconds"

# Test 12: Test that a number of multiple number of hours,minutes and seconds
# shows a text like "x hours, z minutes and y seconds"
print(formatTime(3600*23+60*57+45))
assert formatTime(3600*23+60*57+45) == "23 hours, 57 minutes and 45 seconds"

# Test13: Test that 24 hours are represented as a day returning "1 day" when the number of seconds in a day is the input
print(formatTime(60*60*24))
assert formatTime(60*60*24) == "1 day"

# Test14: Test that several days returns a text referring to the number of days in plural like "X days"
print(formatTime(60*60*24*70))
assert formatTime(60*60*24*70) == "70 days"

# Test15: Test that only days and seconds is shown when a number of seconds translates into Days and seconds only
print(formatTime(60*60*24*6+23))
assert formatTime(60*60*24*6+23) == "6 days and 23 seconds"

# Test16: Test that only days and minutes are shown when a number of seconds translates into days and minutes only
print(formatTime(60*60*24*90+40*60))
assert formatTime(60*60*24*90+40*60) == "90 days and 40 minutes"

# Test17: Test that days, minutes and seconds are shown when a number of seconds
# translates into days, minutes and seconds
print(formatTime(60*60*24*230+14*60+1))
assert formatTime(60*60*24*230+14*60+1) == "230 days, 14 minutes and 1 second"

# Test18: Test that the number of seconds for 365 days is input it returns "1 year"
print(formatTime(60*60*24*365))
assert formatTime(60*60*24*365) == "1 year"

# Test 19: Test that when the number of seconds represent more than one year the text returns "X years"
print(formatTime(60*60*24*365*20))
assert formatTime(60*60*24*365*20) == "20 years"

# Test 20: When a number of seconds that represents several years, days, minutes and seconds, should return all
# time slices
print(formatTime(60*60*24*365*3+60*60*24*8+60*60*3+60*12+56))
assert formatTime(60*60*24*365*3+60*60*24*8+60*60*3+60*12+56) == "3 years, 8 days, 3 hours, 12 minutes and 56 seconds"

# Test 20: When singular units of time are provided the text should reflect the time in singular
print(formatTime(60*60*24*365+60*60*24+60*60+60+1))
assert formatTime(60*60*24*365+60*60*24+60*60+60+1) == "1 year, 1 day, 1 hour, 1 minute and 1 second"
