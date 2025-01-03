v_p = int(input())
v_v = int(input())
v_t = int(input())

v_max = max(v_p, v_v, v_t)
v_min = min(v_p, v_v, v_t)

if v_p == v_max:
    p1 = "Петя"
elif v_p == v_min:
    p3 = "Петя"
else:
    p2 = "Петя"

if v_v == v_max:
    p1 = "Вася"
elif v_v == v_min:
    p3 = "Вася"
else:
    p2 = "Вася"

if v_t == v_max:
    p1 = "Толя"
elif v_t == v_min:
    p3 = "Толя"
else:
    p2 = "Толя"

print(f'{"": ^8}{p1: ^8}{"": ^8}')
print(f'{p2: ^8}{"": ^8}{"": ^8}')
print(f'{"": ^8}{"": ^8}{p3: ^8}')
print(f'{"II": ^8}{"I": ^8}{"III": ^8}')