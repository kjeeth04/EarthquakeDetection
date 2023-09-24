from fastapi import FastAPI , Request
import uvicorn
import requests
from mangum import Mangum

Core = FastAPI()

#send text message to users
# pulls users IP and sends to front end
@Core.get("/ip")
def Homepage(request:Request):
    userIp = request.client.host
    return {"i see you":userIp}

@Core.get("/")
def read_root():
    return {"Hello": "World"}

handler = Mangum(Core)


if __name__ == "__main__":
    uvicorn.run("Main:Core", host="0.0.0.0", port=8000)
