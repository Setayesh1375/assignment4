list = []
list_non_repetitive = []
number = int(input(" tedad adad list "))
i=0
for  i in range(number):
  x = int (input("adad ra vared konid " ))
  list.append(x)
  i+=1
print("list = " , list)

for x in list:
  if x not in list_non_repetitive :
     list_non_repetitive.append(number)

print("list_non_repetitive : " , list_non_repetitive)     