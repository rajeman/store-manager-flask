from flask import Flask
import json
from app import create_app


def test_client():
    app = create_app('testing')
    client = app.test_client()
    response = client.get('/student/rojoy')
    data = json.loads(response.get_data())
    assert data == {'student': 'rojoy'}
