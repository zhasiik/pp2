import json

j = open("D:\pp2\week4\json\sample-data.txt", "r")
data = json.load(j)
print("Interface Status")
print(80 * "=")
print("DN", 47 * " ", "Description", 9 * " ", "Speed  MTU")
print(50 * "-", 20 * "-", 6 * "-", 6 * "-")

# Print the output
c = 0
for i in data['imdata']:
    c += 1
    if c < 5 or c > 13:
        print(i['l1PhysIf']['attributes']['dn'], 28*" ", i['l1PhysIf']['attributes']['fecMode'], ' ', i['l1PhysIf']['attributes']['mtu'])
    else:
        print(i['l1PhysIf']['attributes']['dn'], 29*" ", i['l1PhysIf']['attributes']['fecMode'], ' ', i['l1PhysIf']['attributes']['mtu'])