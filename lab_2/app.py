import requests
import ntplib
from datetime import datetime


def get_time_if_url_not_work():
    c = ntplib.NTPClient()
    response = c.request('0.ua.pool.ntp.org', version=3)
    t = datetime.fromtimestamp(response.tx_time).time().strftime('%H:%M:%S %p')
    d = datetime.fromtimestamp(response.tx_time).date().strftime('%Y-%m-%d')
    date = {"date": d, "time": t}
    return date


def main(url=''):
    if not url:
        print("No URL passed to function")
        return False
    try:
        r = requests.get(url=url)
        d = r.json()
    except:
        d = get_time_if_url_not_work()
    if "time" in d.keys():
        print("Time is: ", d['time'])
    try:
        print("Date is: ", d['date'])
    except KeyError:
        print("No date in response!!!")
        raise KeyError

    return True


def get_date(url=''):
    try:
        r = requests.get(url=url)
        return r.json()
    except:
        return get_time_if_url_not_work()


def home_work(t):
    # Ваш захист
    if 'AM' in t:
        res = 'Доброї ночі'
    elif 'PM' in t:
        res = 'Доброго дня'
    print(res)
    return res


if __name__ == "__main__":
    a = "="*40
    print(a + "\nРезультат без параметрів: ")
    main()
    print(a + "\nРезультат з правильною URL: ")
    main('http://date.jsontest.com/')
    d = get_date('http://date.jsontest.com/')
    home_work(d['time'])