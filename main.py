def fMax1(a, b, c):
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

f1 = fMax1(a=2, b=7, c=6)
print(f1)

f1_1 = fMax1(a=-2, b=7, c=6)
print(f1_1)



#Функция max
def fMax2(a, b, c):
  if a < 0:
    return -1
  else:
    x = [a, b, c]
    max_numb = max(x)
    return max_numb

print("\n""Функция max")
f2 = fMax2(a=2, b=7, c=6)
print(f2)

f2_1 = fMax2(a=-2, b=7, c=6)
print(f2_1)