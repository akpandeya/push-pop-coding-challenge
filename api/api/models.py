from pydantic import BaseModel

class Resolved(BaseModel):
    index : int
    code : int
    text : str