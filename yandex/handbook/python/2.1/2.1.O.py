n = int(input())
m = int(input())
t = int(input())

t_start = n * 60 + m

if t > 1440:
    result_days = t // 1440
    t = t - 1440 * result_days

if t_start + t > 1440:
    t_end = t_start + t - 1440
elif t_start + t == 1440:
    t_end = 0
else:
    t_end = t_start + t

result_hour = t_end // 60
result_minute = t_end - result_hour * 60

print(f"{result_hour:0>2}:{result_minute:0>2}")