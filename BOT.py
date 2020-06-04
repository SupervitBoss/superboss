import logging
import pyowm
from aiogram import Bot, Dispatcher, executor, types


"""                Start BOT             """
API_TOKEN = '1180307400:AAFQuCyllhdb_Wd9jJLDxWI3F6WsRerEMVQ'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


"""               Start WEATHER           """
owm = pyowm.OWM('1d8ecc8ebb1cb5c85e3455cb5a5658e7')
mgr = owm.weather_manager()






@dp.message_handler()
async def echo1(message: types.message):
    a = message.text
    observation = mgr.weather_at_place(a)
    w = observation.weather
    w_list = (list(str(w)))[::-1]
    w_list = w_list[1:(w_list.index('='))]
    w_list = w_list[::-1]
    w1 = ''
    for v in w_list:
        w1 += str(v)
    
    if w1 == 'clear sky':
        a = ('Ясно')
    elif w1 == 'fog':
        a = ('Туман')
    elif w1 == 'few clouds':
        a = ('мало облаков')
    elif w1 == 'broken clouds':
        a = ('небольшие облака')
    elif w1 == 'scattered clouds':
        a = ('немного хмарно')
    elif w1 == 'overcast clouds':
        a = ('хмарно')
    elif w1 == 'light rain':
        a = ('небольшой дождь')
    elif w1 == 'moderate rain':
        a = ('умеренный дождь')
    elif w1 == 'heavy intensity rain':
        a = ('сильный дождь')
    elif w1 == 'thunderstorm with light rain':
        a = ('гроза с небольшим дождем')
    else:
        a = ('выходить не стоит')
    
    b1 = w.temperature('celsius')['temp']
    
    print(b1)
    print(w1)
    
    if b1 >= 26:
        b = 'Тепло, одевай легкую одежду'
    elif 26 > b1 > 20:
        b = 'Прохладно, одень теплую одежду'
    elif 20 >= b1 > 10:
        b = 'Холодно, одень куртку'
    elif 10 >= b1 > 0:
        b = 'Очень холодно, одень теплую куртку'
    elif 0 >= b1 > -10:
        b = 'Холодно, одень пуховик'
    else:
        b = 'Лучше посиди дома'
    
    await message.answer('Сейчас ' + a + '\n' + 'Температура: ' + str(b1) + '\n' + str(b))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)