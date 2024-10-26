print('Любите ли вы котиков?')
answer1 = input()
print('Умеете ли вы программировать?')
answer2 = input()
if answer1 == 'да' and answer2 == 'да':
    print('Да вы просто идеал!')
elif answer1 == 'да' and answer2 == 'нет':
    print('Вы обладаете редкостной добротой.')
elif answer1 == 'нет' and answer2 == 'да':
    print('Вы обладаете незаурядным умом.')
elif answer1 == 'нет' and answer2 == 'нет':
    print('У вас большие перспективы.')
else:
    print('Ошибка: ожидались ответы да/нет')