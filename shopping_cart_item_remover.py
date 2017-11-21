f = open('shoppingcart.txt', 'r')
items = f.readlines()

while(True):
    userInput = str(input('What items do you want removed from your shopping cart: '))
    if(userInput == 'end'):
        break
    userInput = userInput + '\n'
    if(userInput in items):
        items.remove(userInput)

f = open('shoppingcart.txt', 'w')
for item in items:
    f.write(item)
f.close()
