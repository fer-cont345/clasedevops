from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def root():
    return{"message":"Hello World"}

@app.get("/myname/{name}")
async def myName(name: str):
    return{"message": f"Hello {name} this is my new API"}

@app.get("/challenge")
async def writeName():
    return{"message":"Hey, there!! My name is Fernando Contreras:)"}