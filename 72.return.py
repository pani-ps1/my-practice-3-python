def calculateSum(num):
  result = 0
  while num != 0:
    result = result + num
    num = num - 1
  return result

print(calculateSum(10))
