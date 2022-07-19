td = [
  [1,2,3],
  [4,5,6],
  [9,8,9]
]

def diagonal(td):
  leftD = 0
  rightD = 0
  length = len(td) - 1
  
  for iIndex, i in enumerate(td):
    for jIndex, j in enumerate(i):
      if(iIndex == jIndex):
        leftD = leftD + j
      
      if(length == jIndex):
        rightD = rightD + j
        length -=1
  return abs(leftD - rightD)

diff = diagonal(td)
print(diff)