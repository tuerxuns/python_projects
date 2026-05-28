def getHoursMinutesSeconds(totalSeconds):
    seconds = totalSeconds
    minutes = 0
    hours = 0

    while seconds >= 3600:
        hours += 1
        seconds -= 3600

    while seconds >= 60:
        minutes += 1
        seconds -= 60

    hms = []
    h = str(hours) + "h"
    m = str(minutes) + "m"
    s = str(seconds) + "s"

    if hours > 0:
        hms.append(h)
    if minutes > 0:
        hms.append(m)
    if seconds > 0 or totalSeconds == 0:
        hms.append(s)

    return " ".join(hms)


assert getHoursMinutesSeconds(30) == "30s"

assert getHoursMinutesSeconds(60) == "1m"

assert getHoursMinutesSeconds(90) == "1m 30s"

assert getHoursMinutesSeconds(3600) == "1h"

assert getHoursMinutesSeconds(3601) == "1h 1s"

assert getHoursMinutesSeconds(3661) == "1h 1m 1s"

assert getHoursMinutesSeconds(90042) == "25h 42s"

assert getHoursMinutesSeconds(0) == "0s"

print("All tests passed!")
