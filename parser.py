import requests
from bs4 import BeautifulSoup
import datetime
import schedule


problems_url_list = []

for i in range(0, 87):
    url = f'https://codeforces.com/problemset/page/{i}?order=BY_SOLVED_DESC'

    q = requests.get(url)
    result = q.content

    soup = BeautifulSoup(result, 'lxml')
    problems = soup.find_all('a')

    for problem in problems:
        problem_url = 'https://codeforces.com' + problem.get('href')
        problems_url_list.append(problem_url)

with open('problems_url_list.txt', 'a') as file:
    for line in problems_url_list:
        file.write(f'{line}\n')

#Искомый номер
num = "/problemset/problem"

#Читаем файл
with open("problems_url_list.txt", mode='r', encoding='utf_8') as f:
    lst = f.readlines()

#Ищем данные
for i in lst: # перебор всех элементов
    if num in i: # Проверка на наличие номера
        with open('problems_list.txt', 'a') as file:
            file.write(i)

i = 1

def check():
    global i
    print(f"Запустился {i} раз")
    i += 1
    print(datetime.datetime.now())


schedule.every(5).seconds.do(check)

while True:
    schedule.run_pending()

