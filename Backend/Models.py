import pandas as pd
import math
import random
random.seed()

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

def calculate_magnitude(reference_amplitude=1):
    #Finds the highest amplitude to base the magnitude on
    highestAmplitude = 0
    for datum in df["SeismicWaveAmplitude_mm"]:
        if datum > highestAmplitude:
            highestAmplitude = datum
            
    #Converts Amplitude from milimeters to nanometers
    highestAmplitude *= 1000000
            
    return round(math.log10(highestAmplitude / reference_amplitude), 1)

try:
    df = pd.read_csv("testdata.csv")  # Read CSV file directly into DataFrame
except FileNotFoundError:
    print("The file 'testdata2.csv' does not exist in the current working directory.")  # Correct filename in print statement
    exit()  # Exit the script if file not found
except Exception as e:
    print(f"An error occurred: {e}")
    exit()  # Exit the script if any other exception occurs

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
magnitude = None
depth = 0
if onAlert:
    if earthquakeSize == "L":
        #Issue Earthquake Warning Immediately, giving magnitude and depth as well
        magnitude = calculate_magnitude()
        depth = random.randint(1, 10)
    elif earthquakeSize == "M":
        #Issue Earthquake Warning after getting 1 more additional form of proof
        if (animalValue() or groundwaterValue() or electricalChargeValue()):
            #Issue Earthquake Warning Immediately, giving magnitude and depth as well
            magnitude = calculate_magnitude()
            depth = random.randint(1, 10)
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
            #Issue Earthquake Warning Immediately, giving magnitude and depth as well
            magnitude = calculate_magnitude()
            depth = random.randint(1, 10)

        else:
            print("No warning needed")
else:
    #No upcoming earthquake detected
    print("No warning needed")


