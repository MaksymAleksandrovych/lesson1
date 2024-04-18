# import requests
# res_parse_list = []
# response = requests.get("https://coinmarketcap.com/")
# response_text = response.text
# # Розділення тексту за допомогою тегу <span>
# response_parse = response_text.split("<span>")
# # Ітерація по елементам, розділеним за тегом <span>
# for parse_elem_1 in response_parse:
#     # Перевірка, чи елемент починається з символу "$"
#     if parse_elem_1.startswith("$"):
#         # Розділення елемента за допомогою тегу "</span>"
#         for parse_elem_2 in parse_elem_1.split("</span>"):
#             # Перевірка, чи другий розділений елемент починається з символу "$" та має наступний символ цифру
#             if parse_elem_2.startswith("$") and parse_elem_2[1].isdigit():
#                 res_parse_list.append(parse_elem_2)
# # Отримання першого елемента зі списку обмінних курсів Bitcoin
# bitcoin_exchange_rate = res_parse_list[0]
# print(bitcoin_exchange_rate)
# має контекстне меню

# from bs4 import BeautifulSoup
# import requests
# response = requests.get("https://coinmarketcap.com/")
# if response.status_code == 200:  # Перевіряємо, чи успішний HTTP-запит
#     soup = BeautifulSoup(response.text, features="html.parser")
#     # Створюємо об'єкт BeautifulSoup для обробки HTML-вмісту
#        # Знаходимо всі посилання на сторінку ринків Bitcoin
#     soup_list = soup.find_all("a", {"href": "/currencies/bitcoin/#markets"})
#     res = soup_list[0].find("span")  # Знаходимо перше посилання та отримуємо елемент span всередині нього
#     print(res.text)  # Виводимо текст, що міститься в елементі span