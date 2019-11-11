import requests
import json
import logging
from time import sleep

logging.basicConfig(
    filename="logs/server.log",
    filemode='a',
    level=logging.INFO,
    format='{levelname} {asctime} {name} : {message}',
    style='{'
)
log = logging.getLogger(__name__)


def main(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        logging.error(f'Http Error: {errh}')
    except requests.exceptions.ConnectionError as errc:
        logging.error(f'Error Connecting: {errc}')
    except Exception as err:
        logging.error(f'Other error: {err}')
    else:
        data = json.loads(r.content)
        logging.info("Сервер доступний. Час на сервері: %s", data['date'])
        logging.info("Запитувана сторінка: : %s", data['current_page'])
        logging.info("Відповідь сервера містить наступні поля:")
        for key in data.keys():
            logging.info("Ключ: %s, Значення: %s", key, data[key])


if __name__ == '__main__':
    while True:
        main("http://localhost:8000/health")
        sleep(60)