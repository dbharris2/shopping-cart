items = []

while(True):
    userInput = str(input('What items do you want in your shopping cart: '))
    if(userInput == 'end'):
        break
    items.append(userInput)
    print(userInput)

print(items)

f = open('shoppingcart.txt', 'w')
for item in items:
    f.write(item + '\n')
f.close()
