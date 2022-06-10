import requests

url = 'http://localhost:5000/distance'

def test_10km():
    data = { 'distance' : 10.0, 'unit' : 'km' }
    res = requests.post(url=url, json=data)

    assert res.status_code == 200
    content = res.json()
    assert content['distance'] == 6.213712
    assert content['unit'] == 'mi'

def test_nan():
    data = { 'distance' : 'not a number', 'unit' : 'mi' }
    res = requests.post(url=url, json=data)

    assert res.status_code == 400

def test_40mi():
    data = { 'distance' : 40.0, 'unit' : 'mi' }
    res = requests.post(url=url, json=data)

    assert res.status_code == 200
    content = res.json()
    assert content['distance'] == 64.37376
    assert content['unit'] == 'km'

def test_get():
    res = requests.get(url=url)
    assert res.status_code == 200

    content = res.json()
    assert content['mi'] == 1.0
    assert content['km'] == 1.609344
