alice = [5,6,7]
bob = [3,6,10]

def compare(a, b):
  alicePoints = 0
  bobPoints = 0

  length = len(a)
  for i in range(0, length):
    if(a[i] > b[i]):
      alicePoints += 1
    elif(b[i] > a[i]):
      bobPoints += 1
  
  return [alicePoints, bobPoints]

check = compare(alice, bob)
print(check)
