
# Defualt argurment
def countrys(country="a",cities="b"):
    return(f"my country is{country} and my city is{cities}")
print(countrys())
print(countrys(country="Kenya"))
print(countrys(country="Kenya",cities="Nairobi"))
print(countrys("Kenya","Nairobi"))
def firstname(*names):
    for name in names:
        print(f"hello{name}")
print(countrys("Kenya","Uganda","Tanzania","Rwanda"))
name="Uganda"
print(countrys[::-1])
print(countrys[::-2])

