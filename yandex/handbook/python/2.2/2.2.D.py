petya = int(input())
vasya = int(input())
tolya = int(input())
place1 = max(petya, vasya, tolya)
place3 = min(petya, vasya, tolya)
if place1 == petya and place3 == tolya:
    print('1. Петя\n2. Вася\n3. Толя')
elif place1 == vasya and place3 == tolya:
    print('1. Вася\n2. Петя\n3. Толя')
elif place1 == tolya and place3 == petya: 
    print('1. Толя\n2. Вася\n3. Петя')
elif place1 == petya and place3 == vasya:
    print('1. Петя\n2. Толя\n3. Вася')
elif place1 == tolya and place3 == vasya:
    print('1. Толя\n2. Петя\n3. Вася')
elif place1 == vasya and place3 == petya:
    print('1. Вася\n2. Толя\n3. Петя')
