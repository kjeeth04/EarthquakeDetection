from fastapi import FastAPI , Request
import uvicorn
import requests
from fastapi.staticfiles import StaticFiles
from mangum import Mangum
from fastapi.templating import Jinja2Templates

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


Core.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@Core.get("/test",)
async def read_item(request: Request):
    return templates.TemplateResponse("earthquake_map.html", {"request": request})




if __name__ == "__main__":
    uvicorn.run("Main:Core", host="0.0.0.0", port=8000)
