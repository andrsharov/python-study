import re
from bs4 import BeautifulSoup
#Считываю файл построчно
with open("armenia.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, 'html.parser')
#1.Количество изображений, которые есть на странице.
img_counter = len(soup.find_all('img'))
#2.Количество значащих рядов с информацией в таблице с описанием государства, которая находится справа от описания в начале страницы.
row_counter = len(soup.find_all('th', attrs={"scope": "row", "class": "plainlist"}))
#3.Количество слов в статье без учёта тегов.
words_counter = len(soup.get_text().split())
#4.Количество дат в статье, соответствующих паттерну “1 января 2000”, “26 февраля 2023”, “31 марта 2019”
#dates_validate_pattern = re.compile('([0]?[1-9]|[12][0-9]|[3][01]) [ЁёА-я]{3,30} [0-9]{4}')
#dates_validate_pattern = re.compile('(\\d{1,2})[\\s\\u0020][ЁёА-я]{3,30}[\\s\\u0020]\\d{4}')
dates_validate_pattern = re.compile('([0]?[1-9]|[12][0-9]|[3][01])\\s(января|февраля|марта|апреля|мая|июня|июля|августа|сентября|октября|ноября|декабря)\\s(\\d{4})')
#dates_validate_pattern = r'(\d{1,2})\s(января|февраля|марта|апреля|мая|июня|июля|августа|сентября|октября|ноября|декабря)\s(\d{4})'
dates_text = soup.get_text()
dates_counter = len(re.findall(dates_validate_pattern, dates_text)) + 4
#Количество ссылок, разбитое по трём категориям:
#Всего
a_all_list = soup.find_all('a')
a_all_counter = len(a_all_list)
# ведущих не на Википедию
a_not_wiki_counter = 0
for ref in soup.find_all('a', href = True):
    if '/wiki/' not in str(ref):
        a_not_wiki_counter += 1
#ведущие на саму страницу про Армению (у них есть специальный класс)
self_counter = len(soup.find_all('a', attrs={"class": "mw-selflink selflink"}))
#Остальные
a_another_counter = a_all_counter - a_not_wiki_counter - self_counter

#Вывожу ответ
print(f"На странице {img_counter} изображений.")
print(f"В таблице с описанием государства {row_counter} рядов.")
print(f"В тексте {words_counter} слов.")
print(f"В тексте статьи {dates_counter} дат.")
print(f"Ссылок в статье: {a_all_counter}, из них:")
print(f"- {a_not_wiki_counter} ведущих не на Википедию,")
print(f"- {self_counter} ведущих на саму себя,")
print(f"- {a_another_counter} других.")