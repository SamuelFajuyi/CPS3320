import arrow

utc = arrow.utcnow()

now = arrow.now()
print("The time now is: ", now)
print ("The time in Universal Coordinated time is: ", utc)

seconds = utc.timestamp
print("Time coverted into seconds:", seconds)

date = arrow.Arrow.fromtimestamp(seconds)
print("Time coverted into today's date: ", date)

print("Time right now in US/Pacific time:", utc.to('US/Pacific').format('HH:mm:ss'))
print("Time right now in London:", utc.to('Europe/London').format('HH:mm:ss'))

print("What is the time 10 hours from now:", now.shift(hours=10).time())