import requests
class MyRequests():
    @staticmethod
    def post (url:str,data:dict=None,headers:dict=None,cookies:dict=None):
        return MyRequests._send(url,data,headers,cookies,'POST')
    def get (url:str,data:dict=None,headers:dict=None,cookies:dict=None):
        return MyRequests._send(url,data,headers,cookies,'GET')
    def put (url:str,data:dict=None,headers:dict=None,cookies:dict=None):
        return MyRequests._send(url,data,headers,cookies,'PUT')
    def delete (url:str,data:dict=None,headers:dict=None,cookies:dict=None):
        return MyRequests._send(url,data,headers,cookies,'DELETE')

    @staticmethod
    def _send(url:str,data:dict,headers:dict,cookies:dict,method:str):
        url=f"https://playground.learnqa.ru/api{url}"

        if headers is None:
            headers = {}
        if cookies is None:
            cookies = {}

        if method == 'GET':
            resource = requests.get(url,params=data,headers=headers,cookies=cookies)
        elif method == 'POST':
            resource = requests.post(url, data=data, headers=headers, cookies=cookies)
        elif method == 'PUT':
            resource = requests.put(url, data=data, headers=headers, cookies=cookies)
        elif method =='DELETE':
            resource = requests.delete(url, data=data, headers=headers, cookies=cookies)
        else:
            raise Exception(f"Bad http method '{method}' was received")

        return resource
