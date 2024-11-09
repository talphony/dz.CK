def fMaxUs(a, b, c):
  a = int(input("Введите число: "))
  if a < 0:
    return -1
  else:
    max_numb = 0
    if a > max_numb:
      max_numb = a
    if b > max_numb:
      max_numb = b
    if c > max_numb:
      max_numb = c
    return max_numb

fUs = fMaxUs(a=0, b=7, c=6)
print(fUs)


#Функция max
def fMax(a, b, c):
  a = int(input("Введите число: "))
  if a < 0:
    return -1
  else:
    x = [a, b, c]
    max_numb = max(x)
    return max_numb

print("\n""Функция max")
fM = fMax(a = 0, b=7, c=6)
print(fM)
