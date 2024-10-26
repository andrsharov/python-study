text = input()
if 'хорош' in text and 'плох' not in text:
    print('Положительная эмоциональная окраска')
elif 'плох' in text and 'хорош' not in text:
    print('Отрицательная эмоциональная окраска')
else:
    print('Нейтральная или смешанная эмоциональная окраска')