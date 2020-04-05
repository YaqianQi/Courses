days_party_num = [int(x) for x in input().split()]
days = days_party_num[0]
party_num = days_party_num[1]
res = set()
day_off = set(i for i in range(6,days+1,7))
day_off.update( i for i in range(0,days+1,7))
for x in range(party_num):
    c = [int(x) for x in input().split()]
    start_date = c[0]
    step = c[1]

    strike_dates = {i for i in range(start_date, days+1,step)}
    strike_dates.difference_update(day_off)
    #print(*sorted(strike_dates))
    res.update(strike_dates)
print(len(res))

###  reference 
n_days, n_parties = [int(x) for x in input().split()]
strike_days_set = set()

for _ in range(n_parties):
    start_day, step = [int(x) for x in input().split()]
    strike_days_set |= set(range(start_day, n_days + 1, step))

strike_days_set -= set(range(6, n_days + 1, 7))
strike_days_set -= set(range(7, n_days + 1, 7))
print(len(strike_days_set))