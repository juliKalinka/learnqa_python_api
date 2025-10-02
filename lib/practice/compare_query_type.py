import requests
#1. Делает http-запрос любого типа без параметра method, описать что будет выводиться в этом случае.
respounse = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type")
wrong_res=respounse.text
print("1. http-запрос любого типа (например, post) без параметра method выводит:", wrong_res)

#2. Делает http-запрос не из списка. Например, HEAD. Описать что будет выводиться в этом случае.
temp_method = {"method": "HEAD"}
respounse = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method": "HEAD"})
print("2. http-запрос не из списка. Например, HEAD выводит:", respounse.text, ".")

list_methods = ["POST", "GET", "PUT", "DELETE"]
success_res = {"success": "!"}
#3. Делает запрос с правильным значением method. Описать что будет выводиться в этом случае.
print("3. Делает запрос с правильным значением method. Описать что будет выводиться в этом случае:")
for item in list_methods:
    #print(item)
    method = {"method": item}
    match item:
        case "POST":
            respounse = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method)
        case "GET":
            respounse = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=method)
        case "PUT":
            respounse = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method)
        case "DELETE":
            respounse = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method)
        case _:
            print("Неизвестная функция запроса")
    res = respounse.text
    print("     При вызове метода",item.lower(), "c параметром",item,"получили:",res)


#4. С помощью цикла проверяет все возможные сочетания реальных типов запроса и значений параметра method.
# Например с GET-запросом передает значения параметра method равное ‘GET’, затем ‘POST’, ‘PUT’, ‘DELETE’ и так далее.
# И так для всех типов запроса. Найти такое сочетание, когда реальный тип запроса не совпадает со значением параметра,
# но сервер отвечает так, словно все ок. Или же наоборот, когда типы совпадают, но сервер считает, что это не так.
print("4. С помощью цикла проверяет все возможные сочетания реальных типов запроса....:")
for i in range(0, len(list_methods)):
    for j in range(0, len(list_methods)):
        if i != j:
            method = {"method": list_methods[i]}
            match  list_methods[j]:
                case "POST":
                    respounse = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method)
                case "GET":
                    respounse = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=method)
                case "PUT":
                    respounse = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method)
                case "DELETE":
                    respounse = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method)
                case _:
                    print("Неизвестная функция запроса")
            res = respounse.text
            #print("***     При вызове метода", list_methods[i], " c параметром ", list_methods[j], " получили: ", res)
            if res != wrong_res:
                 print("     При вызове метода", list_methods[j].lower(), "c параметром", list_methods[i], "получили:", res)

