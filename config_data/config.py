import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
RAPID_API_KEY = os.getenv("RAPID_API_KEY")
DEFAULT_COMMANDS = (
    ("start", "запуск бота"),
    ("help", "вывод справки"),
    ("lowprice", "вывод самых дешёвых отелей в городе"),
    ("highprice", "вывод самых дорогих отелей в городе"),
    ("bestdeal", "вывод отелей, наиболее подходящих по цене и расположению"),
    ("history", "история поиска")
)
RAPID_API_URL = "https://hotels4.p.rapidapi.com/v2/get-meta-data"
RAPID_API_HEADERS = {
    "content-type": "application/json",
    "X-RapidAPI-Key": RAPID_API_KEY,
    "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
}
RAPID_API_ENDPOINTS = {
    "cities-groups": "https://hotels4.p.rapidapi.com/locations/v3/search",
    "hotel-list": "https://hotels4.p.rapidapi.com/properties/v2/list",
    "hotel-photos": "https://hotels4.p.rapidapi.com/properties/v2/detail"
}

LOG_PATH = os.path.abspath(os.path.join('logs', 'debug.log'))


# Информация с сайта https://rapidapi.com/apidojo/api/hotels4/

# import requests
#
# url = "https://hotels4.p.rapidapi.com/locations/v3/search"
# querystring = {"q": "new york", "locale": "en_US", "langid": "1033", "siteid": "300000001"}
# headers = {
#     "X-RapidAPI-Key": "f6872d413emsh9f8e0dc7485974bp1afdb5jsndd773a0322f7",
#     "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
# }
# response = requests.get(url, headers=headers, params=querystring)
# print(response.json())

# import requests
#
# url = "https://hotels4.p.rapidapi.com/properties/v2/list"
#
# payload = {
#     "currency": "USD",
#     "eapid": 1,
#     "locale": "en_US",
#     "siteId": 300000001,
#     "destination": {"regionId": "6054439"},
#     "checkInDate": {
#         "day": 10,
#         "month": 10,
#         "year": 2022
#     },
#     "checkOutDate": {
#         "day": 15,
#         "month": 10,
#         "year": 2022
#     },
#     "rooms": [
#         {
#             "adults": 2,
#             "children": [{"age": 5}, {"age": 7}]
#         }
#     ],
#     "resultsStartingIndex": 0,
#     "resultsSize": 200,
#     "sort": "PRICE_LOW_TO_HIGH",
#     "filters": {"price": {
#         "max": 150,
#         "min": 100
#     } }
# }
# headers = {
#     "content-type": "application/json",
#     "X-RapidAPI-Key": "f6872d413emsh9f8e0dc7485974bp1afdb5jsndd773a0322f7",
#     "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
# }
#
# response = requests.post(url, json=payload, headers=headers)
#
# print(response.json())

# import requests
#
# url = "https://hotels4.p.rapidapi.com/properties/v2/detail"
#
# payload = {
#     "currency": "USD",
#     "eapid": 1,
#     "locale": "en_US",
#     "siteId": 300000001,
#     "propertyId": "9209612"
# }
# headers = {
#     "content-type": "application/json",
#     "X-RapidAPI-Key": "f6872d413emsh9f8e0dc7485974bp1afdb5jsndd773a0322f7",
#     "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
# }
#
# response = requests.post(url, json=payload, headers=headers)
#
# print(response.json())
