import fastapi
import database
import pydantic_models
import config

import fastapi
import database
import pydantic_models
import config

app = fastapi.FastAPI()

fake_database = {'users':[

    {
        "id":1,             # тут тип данных - число
        "name":"Anna",      # тут строка
        "nick":"Anny42",    # и тут
        "balance": 15300    # а тут float
     },

    {
        "id":2,             # у второго пользователя
        "name":"Dima",      # такие же
        "nick":"dimon2319", # типы
        "balance": 160.23     # данных
     }
    ,{
        "id":3,             # у третьего
        "name":"Vladimir",  # юзера
        "nick":"Vova777",   # мы специально сделаем
        "balance": "25000"     # нестандартный тип данных в его балансе
     }
],}

@app.get('/hello')
def hello():
    return "hello"

@app.get('/about/us')
def about():
    return {"We Are":"Legion"}


@app.get('/get_info_by_user_id/{id:int}')
def get_info_about_user(id):
    return fake_database['users'][id-1]

@app.get('/get_user_balance_by_id/{id:int}')
def get_user_balance(id):
    return fake_database['users'][id-1]['balance']


@app.get('/get_total_balance')
def get_total_balance():
    total_balance: float = 0.0
    for user in fake_database['users']:
        total_balance += pydantic_models.User(**user).balance
    return total_balance

