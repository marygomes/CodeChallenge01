def formatTime(num_seconds):
    num_seconds_in_a_minute = 60
    num_seconds_in_an_hour = 3600
    num_seconds_in_a_day = 3600*24
    num_seconds_in_a_year = 3600*24*365
    period_text_singular = ['year', 'day', 'hour', 'minute', 'second']
    period_text_plural = ['years', 'days', 'hours', 'minutes', 'seconds']
    time_calculation_index = 0
    time_slice_calculated = []
    time_slice_text = []
    for time_slice in (num_seconds_in_a_year, num_seconds_in_a_day, num_seconds_in_an_hour, num_seconds_in_a_minute, 1):
        quotient, remainder = divmod(num_seconds, time_slice)
        if quotient >= 1:
            time_slice_calculated.append(quotient)
            time_slice_text.append(period_text_singular[time_calculation_index] if quotient == 1 else period_text_plural[time_calculation_index])
            num_seconds = remainder
        time_calculation_index += 1
    output_string = ''
    k = 0
    for time_element in time_slice_calculated:
        output_string += ("{} {}{}".format(str(time_element), time_slice_text[k], ', ' if len(time_slice_calculated)-k >2 else ' and ' if len(time_slice_calculated)-k == 2 else ''))
        k += 1
    return output_string if output_string else 'none'
