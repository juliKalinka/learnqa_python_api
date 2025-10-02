import requests
#С помощью конструкции response.history необходимо узнать,
# сколько редиректов происходит от изначальной точки назначения до итоговой. И какой URL итоговый.
respounse = requests.get("https://playground.learnqa.ru/api/long_redirect")
try:
    len_hist = len(respounse.history)
    if len_hist > 0:
        print("Итоговый url: ",respounse.history[len_hist-1].url)
    else:
        print("Истории нет!")
    print("Количество редиректов: ", len_hist)
except:
    print("ответ не получен!")