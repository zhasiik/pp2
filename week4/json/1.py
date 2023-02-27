import json

j = open("D:\pp2\week4\json\sample-data.txt", "r")
data = json.load(j)
print(data['imdata'][0]['l1PhysIf']['attributes'])
