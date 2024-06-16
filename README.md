# FastAPI-Task
FastAPI Task

# clone the repo
git clone https://github.com/gopishettyshashikanth/FastAPI-Task.git

# install requirements.txt 
pip install -r requirements.txt

# application run command 
uvicorn main:app --reload

# API Details
API URL : http://127.0.0.1:8000/add
Method : POST
#request:
{
  "batchid": "id0101",
  "num_list": [[1,2],[3,4]]
}

#response:
{
  "batchid": "id0101",
  "response": [3, 7],
  "status": "complete",
  "started_at": "16/06/2024 17:58:57",
  "completed_at": "16/06/2024 17:58:57"
}

#pytest run command
pytest tests/main_test.py
