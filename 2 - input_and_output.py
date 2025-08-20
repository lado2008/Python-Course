
"""
print() ფუნქციის გამოყენებით, შესაძლებელია output-ის სხვადასხვა
ფორმატში გამოჩენა/გამოსახვა.
"""
name = 'Hi, Everyone'
print("Hello World")
print(name) #ცვლადის დაბეჭვდვა 


"""
input() ფუნქციის გამოიყებება მომხმარებლის input-ის მისაღებად.
"""
name = input("Enter your name: ")  
print("Hello,", name, "!")

"""
ასევე შესაძლებელია რამოდენიმე input-ის მიღება ერთ ხაზე,
მომხმარებლის მიერ შეყვანილი მნიშვნელობა იყოფა თითოეული
მნიშვნელობისთვის ცალკეულ ცვლადებად split() მეთოდის გამოყენებით
"""
x, y = input("Enter two values: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)