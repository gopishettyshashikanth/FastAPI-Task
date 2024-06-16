from fastapi import FastAPI
from typing import List
from multiprocessing import Pool, cpu_count
from fastapi import HTTPException
from models import AddInputs
import logging
from datetime import datetime

app = FastAPI()
now = datetime.now()

# # Configure logging
logging.basicConfig(level=logging.INFO)

def add_numbers(numbers):
    return sum(numbers)

def parallel_addition(numbers_list):
    # Create a multiprocessing pool
    num_processes = cpu_count()
    with Pool(num_processes) as pool:
        results = pool.map(add_numbers, numbers_list)
    return results


@app.post("/add")
async def perform_addition(numbers_list: AddInputs):
    try:
        start_time = now.strftime("%d/%m/%Y %H:%M:%S")
        results = parallel_addition(numbers_list.num_list)
        end_time = now.strftime("%d/%m/%Y %H:%M:%S")
        results = {
            "batchid":numbers_list.batchid,
            "response":results,
            "status":"complete",
            "started_at":start_time,
            "completed_at": end_time
        }
        return results
    except Exception as e:
        logging.error(f"Error occurred during addition of input lists: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

