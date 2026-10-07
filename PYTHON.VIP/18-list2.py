
bagkit=['book',True,False,3.14,None,400]
pockets=[]
print(bagkit)
print(pockets)
pockets.append(100)
pockets.append(200)
pockets.append(300)
print(pockets)
pockets.insert(0,50)
pockets.insert(3,75)
pockets.insert(5,25)
print(pockets)
pockets.pop(4)
print(pockets)
pockets.remove(200)
print(pockets)
pockets[0]=30
print(pockets)
'''
pockets.clear()
print(pockets)
'''
del pockets
print(pockets)
print("good by")
