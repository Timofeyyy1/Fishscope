from fastapi import FastAPI

app = FastAPI(title="Fishscope API")

@app.get("/")
def read_root():
    return {"message": "Fishscope API is running successfully!"}