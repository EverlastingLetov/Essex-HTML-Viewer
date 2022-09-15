import requests
import html2text

print("Приветствуем в Essex! С помощью данной программы Вы сможете просматривать HTML-страницы прямо в терминале (без изображений). Медиафайлы можно загрузить с помощью утилиты wget")

skip = input()

print("Другие наши творения Вы можете увидеть на https://github.com/EverlastingLetov")

skip = input()

url = input("Введите URL: ")
print("/n" * 100)
site = requests.get(url)
pagify = html2text.HTML2Text()
pagify.ignore_links = True
page = pagify.handle(site.text)
print(page)