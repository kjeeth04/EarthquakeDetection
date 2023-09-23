import pandas as pd

def animalValue():
    for datum in df["AnimalActivityDuration_min"]:
        if datum == 45:
            return True
    return False

def groundwaterValue():
    for datum in df["GroundWaterChange_m"]:
        if datum >= 1.0:
            return True
    return False
    
def electricalChargeValue():
    for datum in df["ElectricalChange_uV"]:
        if datum >= 60:
            return True
    return False



try:
    data = pd.read_csv("testdata2.csv")
except FileNotFoundError:
    print("The file 'testdata.csv' does not exist in the current working directory.")
except Exception as e:
    print(f"An error occurred: {e}")
    
df = pd.DataFrame(data)

#Determines if the city needs to be put on Alert
onAlert = False
#Is true when a large earthquake is incoming
earthquakeSize = None

for datum in df["SeismicFrequency_Hz"]:
    if datum < 0.1:
        onAlert = True
        earthquakeSize = "L"
        break
    elif datum <= 1:
        onAlert = True
        earthquakeSize = "M"
    elif datum <= 20 and earthquakeSize != "M":
        onAlert = True
        earthquakeSize = "S"

#Determines whether or not to send an alert
if onAlert:
    if earthquakeSize == "L":
        #Issue Earthquake Warning Immediatey
        print("Issue Warning")
    elif earthquakeSize == "M":
        #Issue Earthquake Warning after getting 1 more additional form of proof
        if (animalValue() or groundwaterValue() or electricalChargeValue()):
            print("Issue Warning")
        else:
            print("No warning needed")
    elif earthquakeSize == "S":
        #Issue Earthquake Warning after getting 2 more additional forms of proof
        Counter = 0
        if animalValue():
            Counter += 1
        if groundwaterValue():
            Counter += 1
        if electricalChargeValue():
            Counter += 1
            
        if Counter >= 2:
            print("Issue Warning")
        else:
            print("No warning needed")
else:
    #No upcoming earthquake detected
    print("No warning needed")


