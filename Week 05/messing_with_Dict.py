# messing with dictionaries
# Author: Darren Miller

car= {
    "make" : "Kia",
    "Model" : "Sportage",
    "Year" : "2014",
    "Owner" : {"name" : "Darren", "driver number" : "1123"}
}
print (car)

for key in car:
    print (key, 'has value', car[key])
