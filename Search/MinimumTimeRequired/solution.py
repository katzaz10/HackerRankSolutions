def minTime(machines, goal):
    days = [0]
    for machine in list(set(machines)):
        days = days * machine
    days += [0]
    for day in machines:
        cur_day = day
        while cur_day < len(days):
            days[cur_day] += 1
            curday += day
    tot_days = 0
    tot_made = 0
    cur_day = 0
    while tot_made < goal:
        cur_day += 1
        if cur_day > len(days):
            cur_day = 1
        tot_days += 1
        tot_made += days[cur_day]
    return tot_days

print minTime([2,3], 5)