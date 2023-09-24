import requests
import datetime
currentTime = datetime.datetime.now()
realTime = currentTime.strftime("%m/%d/%Y - %H:%M")
def Sendall(Message:str,Reciver) -> tuple:
    key = "a7841a21d167c73e6c21920b9ada3cf790eb6713Mnr07elgGYuy7uldxcgyDikf2"
    resp = requests.post('https://textbelt.com/text', {
    'phone': Reciver,
    'message': Message,
    'key': key,
    })
    return resp.json()

def allCast(message,Numbers: list[int]):
    for nums in Numbers:
        print(Sendall(message,nums))
    print("casted message to all users")

groupmemebers = ["2159397696","2673562603","6109611239","90852528880"]
Mes = f"""
*Incoming Earthquake Alert**
Alert Level: Moderate
Magnitude: 5.2
Location: 30 miles northeast of philadelphia
Depth: 10 miles
Time: {realTime}

"""
#print(allCast(Mes,groupmemebers)) workds fine
#print(allCast())