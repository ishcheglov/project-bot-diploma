from typing import Dict, List, Union
from utils.api_reqiest import request_to_api
from config_data.config import RAPID_API_HEADERS, RAPID_API_ENDPOINTS
from loguru import logger
import json


@logger.catch
def parse_photos(hotel_id: int) -> Union[List[Dict], None]:
    """
    Функция делает запрос в request_to_api и десериализирует результат. Если запрос получен и десериализация прошла -
    возвращает обработанный результат в виде списка словарей, иначе None.

    """
    payload = {"propertyId": hotel_id}
    response = request_to_api(
        method_type="POST",
        url=RAPID_API_ENDPOINTS['hotel-photos'],
        payload=payload,
        headers=RAPID_API_HEADERS)
    if response and response.text != '':
        result = json.loads(response.text)
        return result
    return None


@logger.catch
def process_photos(all_photos, amount_photos: int) -> Union[List[str], None]:
    """
    Функция получает список словарей - результат парсинга фоток, выбирает нужную информацию, обрабатывает и складывает
    в список result.

    """

    data = all_photos["data"]["propertyInfo"]["propertyGallery"]["images"]
    photos = [data[i]["image"]["url"] for i in range(amount_photos)]

    return photos
