from fastapi.testclient import TestClient
from main import app
from datetime import datetime

client = TestClient(app)
now = datetime.now()

def test_perform_addition_success():
	response = client.post('/add', json={"batchid": "id0101", "num_list": [[1,2],[3,4]]})
	assert response.status_code == 200
	assert response.json() == {
				  "batchid": "id0101",
				  "response": [3, 7],
				  "status": "complete",
				  "started_at": now.strftime("%d/%m/%Y %H:%M:%S"),
				  "completed_at": now.strftime("%d/%m/%Y %H:%M:%S")
				}

def test_perform_addition_empty_list():
	response = client.post('/add', json={"batchid": "id0102", "num_list": [[]]})
	assert response.status_code == 200
	assert response.json() == {
				  "batchid": "id0102",
				  "response": [0],
				  "status": "complete",
				  "started_at": now.strftime("%d/%m/%Y %H:%M:%S"),
				  "completed_at": now.strftime("%d/%m/%Y %H:%M:%S")
				}

def test_perform_addition_without_batchid():
	response = client.post('/add', json={"num_list": [[1,2],[3,4]]})
	assert response.status_code == 422	

def test_perform_addition_without_payload():
	response = client.post('/add', json={"batchid": "id0101"})
	assert response.status_code == 422