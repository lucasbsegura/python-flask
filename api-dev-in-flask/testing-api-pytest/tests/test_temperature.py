import requests

url = 'http://localhost:5000/temperature'

def test_minus40():
    data = { 'temperature' : -40.0, 'unit' : 'c' }
    req = requests.post(url = url, json = data)

    assert req.status_code == 200
    content = req.json()
    assert content['temperature'] == -40.0
    assert content['unit'] == 'f'

def test_nan():
    data = { 'temperature' : 'not a number', 'unit' : 'c' }
    req = requests.post(url = url, json = data)

    assert req.status_code == 400

def test_100f():
    data = { 'temperature' : 100.0, 'unit' : 'f' }
    req = requests.post(url = url, json = data)

    assert req.status_code == 200
    content = req.json()
    assert content['temperature'] > 37.7 and content['temperature'] < 37.8
    assert content['unit'] == 'c'
