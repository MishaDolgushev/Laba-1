from faker import Faker
import pandas as pd
import numpy as np
import alphabets
import time
from datetime import  datetime


fake = Faker(locale="ru_RU")
filename = 'data.csv'
data = [['Пользователь', 'IP', 'Платформы', 'Дата просмотра', 'Кол-во рекламы', 'Время просмотра рекламы', 'Вид рекламы']]

def random_dates(start, end):
    start = datetime.strptime(start, '%d/%m/%Y')
    end = datetime.strptime(end, '%d/%m/%Y')
    ndays = (end - start).days + 1
    return start.date() + pd.to_timedelta(np.random.randint(0, ndays), unit = 'D')

def adversting_time(n, coeff):
    if coeff == None:
        coeff = np.random.randint(20, 361)
    time_format = time.strftime("%H:%M:%S", time.gmtime(n*coeff))
    return time_format

def generate(data_size, start_date, end_date, time_advertising_video):
    global data

    for i in range(data_size):
        user = fake.free_email()
        IP = fake.ipv4()
        platform = np.random.choice(alphabets.social_networks)
        date = random_dates(start_date, end_date)
        advertisement_count = np.random.randint(1, 100)
        adversting_time_ = adversting_time(advertisement_count, time_advertising_video)
        type_advertising = np.random.choice(alphabets.products[int(date.strftime('%m'))%12//3])
        data.append([user, IP, platform, date, advertisement_count, adversting_time_, type_advertising])
    data = pd.DataFrame(data)
    data.to_excel('data.xlsx', index = False, header = False)