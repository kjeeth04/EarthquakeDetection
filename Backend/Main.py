from fastapi import FastAPI , Request
import uvicorn
import requests

Core = FastAPI()

#send text message to users
# pulls users IP and sends to front end
@Core.get("/")
def Homepage(request:Request):
    userIp = request.client.host
    return {"i see you":userIp}






if __name__ == "__main__":
    uvicorn.run("Main:Core", host="0.0.0.0", port=8000)
