import json
#распарсить нашу переменную json_text и вывести текст второго сообщения с помощью функции print.
json_text='{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'

obj_json = json.loads(json_text)

key = "messages"
if key in obj_json:
    #print(obj_json[key])
    #print(len(obj_json[key]))
    if len(obj_json[key]) >= 2:
        key2 = "message"
        if key2 in obj_json[key][1]:
            print("Текст второго обращения:",obj_json[key][1][key2])
        else:
            print(f"{key2} отсутствует в строке obj_json[{key}][1].")
    else:
        print("В тексте меньше 2х элементов.")
else:
    print(f"{key} отсутствует в строке json_text.")