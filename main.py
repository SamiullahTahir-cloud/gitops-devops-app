from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "GitOps Pipeline Deployed via Render", "status": "success"}
