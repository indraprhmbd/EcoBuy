from pydantic import BaseModel


class RequestCreate(BaseModel):
    waste_id: int

class RequestResponse(BaseModel):
    status: str

class CompleteResponse(BaseModel):
    status: str
