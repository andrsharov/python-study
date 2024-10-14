dict_domains = {
    '.uk': 'Великобритания',
    '.de': 'Германия',
    '.il': 'Израиль',
    '.in': 'Индия',
    '.kz': 'Казахстан',
    '.mm': 'Мьянма',
    '.om': 'Оман',
    '.ru': 'Россия',
    '.uz': 'Узбекистан',
    '.et': 'Эфиопия',
    '.com': 'Международный',
    '.org': 'Международный',
    '.net': 'Международный'
}

input_domain = str(input())

keys = list(dict_domains.keys())

for i in range(len(keys)):
    if keys[i] in input_domain:
        print(dict_domains[keys[i]])