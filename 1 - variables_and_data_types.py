"""
ცვალდები (ანუ variables) Python-ში არის მეხსიერების ელემენტები,
რომელშიც შენახულია მონაცემი, რომელსაც შეგიძლია გამოიყენო ან
შეცვალო პროგრამის განმავლობაში.
"""

a = 5    # Int - მთელი რიცხვები 
b = 3.14 # Float - არამთელი/ცვლადი რიცხვები
c = "Hi" # Str - სტრინგები, ტექტური მონაცემები
d = True # Bool - აქვს მხოლოდ ორი მნიშვნელობა: True და False

#type არის მეთოდი რომლითაც შეგვიძლა ცვლადის ტიპის განსაზღვრა
print(type(a), type(b), type(c), type(d))

"""
ქასთინგი - თუ გვსურს ცვლადის მონაცემის ტიპის განსაზღვრა, 
ეს შეიძლება გაკეთდეს ქასთინგით  
"""
x = str(3)  
y = int(3)    
z = float(3)

"""
Python-ის ცვლადების წესები:
- ცვლადის სახელი უნდა იწყებოდეს ასოთი ან ქვედა ხაზის სიმბოლოთი
- ცვლადის სახელი არ შეიძლება დაიწყოს რიცხვით
- ცვლადის სახელი შეიძლება შეიცავდეს მხოლოდ ანბანურ-რიცხვით სიმბოლოებს და ქვედახაზებს
- ცვლადის სახელი არ შეიძლება იყოს Python-ის არცერთი საკვანძო სიტყვა .
"""
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Camel Case - ყველა სიტყვა, პირველის გარდა, დიდი ასოთი იწყება
myVariableName = "John"

# Pascal Case - თითოეული სიტყვა იწყება დიდი ასოთი
MyVariableName = "John"

# Snake Case - თითოეული სიტყვა გამოყოფილია ქვედა ხაზის სიმბოლოთი
my_variable_name = "John"

"""
Python-ში შესაძლებელია, ერთ ხაზზე რამოდენიმე ცვლადის მიშვნელობის მინიჭება
"""
variable1, variable2, variable3 = "One", "Two", "Three"
print(variable1, variable2, variable3)

"""
ასევე შესაძლებელია ერთი და იგივე მნიშვნელობა მიენიჭოს რამოდენიმა ცვლადს ერთ ხაზში
"""
Text1 = Text2 = Text3 = "This is some Text"
print(Text1)
print(Text2)
print(Text3)

"""
თუ List-ში, Tuple-ში და ა.შ. გვაქვს მნიშვნელობების კოლექცია,
Python საშუალებას გვაძლევს ამოვიღოთ მნიშვნელობები ცვლადებში. ამას ეწოდება unpacking.

Tuple-ის გახსნა: https://www.w3schools.com/python/python_tuples_unpack.asp
"""
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

"""
Python-ში არსებობს გლობალური ცვლადბეი რომლებიც ფუნქციების გარეთ იქმნება, 
ზემოდ მოცემული ყველა ცვლადი არის გლობალური

https://www.w3schools.com/python/python_variables_global.asp
"""


"""სხვა მონაცემთა ტიპები""" 
data1 = 1j                            #complex - კომპლექსური რიცხვი (რთული რიცხვები იწერება წარმოსახვითი ნაწილის სახით „j“-თი)
data2 = ["apple", "banana", "cherry"] #list - ცვალებადი კოლექცია (ელემენტების სია)
data3 = ("apple", "banana", "cherry") #tuple - უცვლელი კოლექცია
data4 = range(6)                      #range - რიცხვების მიმდევრობა
data5 = {"name": "Jon", "age": 28}    #dict - სია key: desc წყვილებით
data6 = {"apple", "banana", "cherry"} #set - უნიკალური ელემენტების კოლექცია(ანუ არ იმეორებს ერთი და უგივე მინაცემებს)
data7 = frozenset({"apple", "banana", #frozenset - უცვლელი set-ი
                   "cherry"})
data8 = b"Hello"                      #bytes - უცვლელი ბინარული მონაცემები
data9 = bytearray(5)                  #bytearray - ცვალებადი ბინარული მონაცემები
data10 = memoryview(bytes(5))         #memoryview - "იხილო” ბინარული მონაცემები მეხსიერებაში
data11 = None                         #NoneType - ცარიელი მნიშვნელობა


print("complex ---", data1)
print("list ---", data2)
print("tuple ---", data3)
print("range ---", data4)
print("dict ---", data5)
print("set ---", data6)
print("frozenset", data7)
print("bytes ---", data8)
print("bytearray ---", data9)
print("memoryview ---", data10)
print("NoneType ---", data11)

"""
მონაცემთა ტიპის კონვერტაცია 
- ერთი ტიპიდან მეორეში კონვერტაცია შესაძლებელია
int(), float(), და complex() მეთოდების გამოყენებით
"""
X = 1
Y = 2.3
Z = 1j

#გადაყავს int-დან float-ში
A = float(X)
#გადაყავს float-დან int-ში
B = int(Y)
#გადაყავს int-დან complex-ში 
C = complex(X)

print(A, type(A))
print(B, type(B))
print(C, type(C))

"""
ასევ python-ში არის ჩაშენებული მოდული random-ი რომლის გამოყენებით შესაძლებელი შემთხვევით რიცხვების შქმნა
"""
import random

print("random", random.randrange(1, 10))

#მთელი რიცხვები:
x_1 = int(1) # 1
y_1 = int(2.3) # 2
z_1 = int("3") # 3

#Float-ები
x_2 = float(1) # 1.0
y_2 = float(2.3) # 2.3
z_2 = float("3") # 3.0
w_2 = float("4.2") # 4.2

#String-ები
x_3 = str("something") # "something"
y_3 = str(2) # '2'
z_3 = str(3.0) # '3.0'