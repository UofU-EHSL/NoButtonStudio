from requests import get
from requests import post

HOME = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiI5ZGU4YjFiNmQ1MDQ0MTExYTkyOTYyY2RjN2YwYmY2NyIsImlhdCI6MTY1MTYyNTA3MSwiZXhwIjoxOTY2OTg1MDcxfQ.2eWmn6yZVOavDIW4YQOMI1FC_jgOgfcng8NBsxOt6NQ"

LOCAL = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiI4ZjdhZWQ1ZGIyNzc0YTVmOTAwOGU3YzkzMTVhZWNhNyIsImlhdCI6MTY1MTYxNjEwOSwiZXhwIjoxOTY2OTc2MTA5fQ.xaN9UJpj4bINN3VBpIHfCgTe-N4EfBy6EEeKspbnWgo"

def lightScene(scene):
    url = "http://localhost:8123/api/services/scene/turn_on"
    headers = {"Authorization": "Bearer " + LOCAL}
    data = {"entity_id": scene}
    response = post(url, headers=headers, json=data)

