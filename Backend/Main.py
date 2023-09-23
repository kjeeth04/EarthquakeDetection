from fastapi import FastAPI
import uvicorn


Core = FastAPI()

# Endpoints
@Core.get("/test")
def Homepage():
    return {"worked": True}


if __name__ == "__main__":
    uvicorn.run("your_module_name:Core", host="0.0.0.0", port=8000)
