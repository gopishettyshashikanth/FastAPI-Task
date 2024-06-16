from pydantic import BaseModel, Field

class AddInputs(BaseModel):
	batchid: str = Field(...,title="batchid", example="id0101")
	num_list: list = Field(...,title="list of numbers", example="[[1,2],[3,4]]")