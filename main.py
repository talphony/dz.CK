def dif(a, b, c):
  if a < 0:
    a = -1
    print ("Число 'a' отрицательное: ", a)
  else:
    x = [a, b, c]
    maxNumb = max(x)
    print("Максимальный элемент: ", maxNumb)

dif(a=2, b=3, c=6)