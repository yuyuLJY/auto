from fastapi import FastAPI

app = FastAPI()

@app.post("/")
async def get_analysis(test: str):
    print(test)
    return test
