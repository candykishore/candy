from fastapi import FastAPI
from pydantic import BaseModel
class Kishore(BaseModel):
    age=19
    Date of birth=16-01-2003
    College code=6117
    Register number=611720104040

nsit=FastAPI()

@nsit.get("/{Name:path}")
def Kishore(Name:str):
     return{"Narasu's Sarathy Institute Of Technology":Name}

@nsit.post("/item")
def reg(i: Kishore):return(i)
