def main():
    current = input("Start Time in 24-hour HH:MM: ").strip()
    print(*format_time(get_times(current)), sep="\n")


def format_time(times):
    i = 4
    tm = []
    for time in times:
        if i != 0:
            tm.append(
                f"Your Break Starts at {time['break']} and ends at {time['restart']}"
            )
            i -= 1
        else:
            tm.append(
                f"Your Long Break starts at {time['break']} and ends at {time['restart']}"
            )
    return tm


def get_times(current: str) -> list:
    work = int(input("Work For: "))
    srt_break = int(input("Short Break: "))
    lng_break = int(input("Long Break: "))
    print(type(current))
    hour, min = current.strip().split(":")
    min = int(min)
    hour = int(hour)
    brktme = []
    restarttm = []
    for i in range(4):
        if (work + min) >= 60:
            min = (work + min) - 60
            hour += 1
            if hour == 24:
                hour = 00
            brktme.append(f"{hour:02}:{min:02}")
        else:
            min = work + min
            brktme.append(f"{hour:02}:{min:02}")

        if (min + srt_break) >= 60:
            min = (min + srt_break) - 60
            hour += 1
            if hour == 24:
                hour = 0
            restarttm.append(f"{hour:02}:{min:02}")
        else:
            min = min + srt_break
            restarttm.append(f"{hour:02}:{min:02}")

    if (work + min) >= 60:
        min = (work + min) - 60
        hour += 1
        if hour == 24:
            hour = 00
        brktme.append(f"{hour:02}:{min:02}")
    else:
        min = work + min
        brktme.append(f"{hour:02}:{min:02}")

    if (min + lng_break) >= 60:
        min = (min + lng_break) - 60
        hour += 1
        if hour == 24:
            hour = 0
        restarttm.append(f"{hour:02}:{min:02}")
    else:
        min = min + lng_break
        restarttm.append(f"{hour:02}:{min:02}")
    times = [{"break": brktme[i], "restart": restarttm[i]} for i in range(len(brktme))]

    return times


main()
