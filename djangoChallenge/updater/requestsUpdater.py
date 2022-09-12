import requests


def send_request(request_type, request_body):
    request = request_type
    if request == 'POST':
        request_body = request_body
    
    if request_type == 'POST':
        requests.post('http://127.0.0.1:8000/admin/scheduler/individual/add/', data=request_body)
    elif request_type == 'GET':
        requests.get('http://127.0.0.1:8000/admin/scheduler/individual/')