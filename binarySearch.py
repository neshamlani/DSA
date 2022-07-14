from audioop import reverse


arr = [1,2,3,4,7,10,11,13]

print(arr)

# Linear search code

def locate_card_linear_search(cards, query):
  # for i in range(0, len(list))
  for index, item in enumerate(cards):
    if query == item:
      return index
  return -1

found_linear = locate_card_linear_search(arr, 7)
notFound_linear = locate_card_linear_search(arr, 15)

print(found_linear)
print(notFound_linear)

#Recursive Binary Search code

def check(min, max, cards, query):
  if max >= min:
    current = (min + max) // 2

    if cards[current] == query:
      return current

    elif cards[current] > query:
      return check(min, current -1 , cards, query)

    else:
      return check(current + 1, max, cards, query)
  
  else:
    return -1
  

def locate_card_binary_search(cards, query):
  if len(arr) == 0:
    return -1

  initialMin = 0
  initialMax = len(cards) - 1

  index = check(initialMin, initialMax, cards, query)
  return index

foundBinary = locate_card_binary_search(arr, 13)
print(foundBinary)
