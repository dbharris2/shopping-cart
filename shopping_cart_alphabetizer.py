f = open('shoppingcart.txt', 'r')
items = f.readlines()
items.sort()
print(items)
# for item in items:
#     f.write(item + '\n')
f.close()

f = open('shoppingcart.txt', 'w')
for item in items:
    f.write(item)
f.close()
