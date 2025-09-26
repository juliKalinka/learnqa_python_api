import requests
import json
import time
#Наша задача - написать скрипт, который делал бы следующее:
#1) создавал задачу
#2) делал один запрос с token ДО того, как задача готова, убеждался в правильности поля status
#3) ждал нужное количество секунд с помощью функции time.sleep() - для этого надо сделать import time
#4) делал бы один запрос c token ПОСЛЕ того, как задача готова, убеждался в правильности поля status и наличии поля result

def  get_respounse(token):
    if token=="":
        respounse = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
    else:
        respounse = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": token})
    respounse_json = json.loads(respounse.text)
    return respounse_json

#1) создавал задачу
print("","1) создали задачу")
respounse_json = get_respounse("")
print("     ",respounse_json)

if "token" not in respounse_json:
    print(f"В вызове нет ключа token")
else:
    if "seconds" not in respounse_json:
        print(f"В вызове нет ключа seconds")
    else:
        start_token = respounse_json["token"]
        start_seconds=respounse_json["seconds"]
        print("     ","Первый запуск, token:", start_token)
        print("     ","Первый запуск, start_seconds:", start_seconds)
        err_token=start_token+"AAA"
        respounse_err_json = get_respounse(err_token)
        print("     ",f"Запуск с ошибочным токеном status: {respounse_err_json}")
        # 2) делал один запрос с token ДО того, как задача готова, убеждался в правильности поля status
        print("2) делаем один запрос с token ДО того, как задача готова, убеждаемся в правильности поля status")
        #ждем половину заявленного времени (округление с недостатком)
        wait_seconds=start_seconds//2
        print("     ",f"Ждем половину заявленного времени (округление с недостатком): {wait_seconds} сек")
        time.sleep(wait_seconds)
        respounse_json = get_respounse(start_token)
        if "status" not in respounse_json:
            print(f"Во втором вызове нет ключа status")
        else:
            print("     ",f"Второй запуск, status: {respounse_json["status"]} - это {"ожидаемый" if respounse_json["status"]=="Job is NOT ready" else "неожиданный"} статус")
        wait_seconds = start_seconds-wait_seconds
        # 3) ждал нужное количество секунд с помощью функции time.sleep() - для этого надо сделать import time
        print(f"3) Ждем остальное время: {wait_seconds} сек")
        time.sleep(wait_seconds)
        # 4) делал бы один запрос c token ПОСЛЕ того, как задача готова, убеждался в правильности поля status и наличии поля result
        print("4) делаем один запрос c token ПОСЛЕ того, как задача готова, убеждаемся в правильности поля status и наличии поля result")
        respounse_json = get_respounse(start_token)
        if "status" not in respounse_json:
            print(f"В вызове нет ключа status")
        else:
            if "result" not in respounse_json:
                print(f"В вызове нет ключа result")
            else:
                print("     ",f"Третий запуск, status: {respounse_json["status"]} - это {"ожидаемый" if respounse_json["status"]=="Job is ready" else "неожиданный"} статус")
                print("     ",f"Третий запуск, result: {respounse_json["result"]}")
