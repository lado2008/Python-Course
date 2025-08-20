"""
Python-ში სტრინგები შეიძლება ჩაიწეროს როგორც ერთიან ბრჭყალში(')
ასევე ორიან ბრჭყალში(")
"""
#ორივე ერთი და იგივეა
print("Hello")
print('Hello')

"""
ასევე შესაძლებელია ორივე ტიპის ბრჭყალებში(' , ") ჩაიწეროს კიდევ რამოდენიმე ბრჭყალი,
იმ პირობით, რომ ისინი არ ემთხვევეა სტრიქონის გარშემო არსებულ ბრჭყალებს
"""
print("Hi, his name is 'Jon'")
print('Hi, his name is "Jon"')

"""
Python-ში შესაძლებელია მრავალსტრიქონიანი string-ების 
მინიჭება სამი ბრჭყალის გამოყენებით(''')
"""

a = """Python is a programming language 
that lets you work quickly and integrate 
systems more effectively."""
print(a)

b = """Python is a programming language 
that lets you work quickly and integrate 
systems more effectively."""
print(b)


"""
ბევრი სხვა პოპულარული პროგრამირების ენის მსგავსად, 
Python-ში სტრიქონები unicode-ის სიმბოლოების მასივებია.
"""
c = "Hello, World!"
print(c[1]) #კვადრატული ფრჩხილების გამოყენება შესაძლებელია სტრიქონის ელემენტებზე წვდომისთვის.

"""
რადგან string-ები მასივებია, სტრიქონის 
სიმბოლოების ამოღება შესაძლებელია for ციკლით
"""
for x in "something":
    print(x)


print("Length of C:", len(c)) # სტრიქონის სიგრძის გასაგებად გამოიყენება len() ფუნქცია


"""
იმის გასაგებად, არის თუ არა სქტიქონში გარკვეული ფრაზა ან სიმბოლო,
შეგვიძლია გამოვიყენოთ keyword-ი "in"

და იმის შესამოწმებლად, არის თუ არა სტრიქონში გარკვეული ფრაზა ან სიმბოლო,
შეგვიძლია გამოვიყენოთ keyword-ი "not in"
"""
some_text = "Python is a programming language"
print("Python" in some_text) # აბრულებს True ან False
print("Something" not in some_text) # აბრულებს True ან False

if "Python" in some_text: 
    print("Yes, 'Python' is in this text")

if "Something" not in some_text:
    print("No 'Something' is not in this text")


"""
Python - Slicing Strings

ჩვენ შეგვიძლია სიმბოლოების რეინჯის/დიაპაზონის დაბრუნება Slice-ის გამოყენებით
"""
d = "Hello, World!"
print(d[2:5]) # სტრიქონის ნაწილის დასაბრუნებლად უნდა მივუთითოდ "საწყისი" და "საბოლოო" ინდექსები, გამოყოფილი ორწერტილით 
print(d[:5]) # საწყისი ინდექსის გამოტოვებით, რეინჯი პირველი სიმბოლოდან დაიწყება
print(d[2:]) # საბოლოო ინდექსის გამოტოვებით, რეინჯი ბოლომდე გადავა
print(d[-5: -2]) #უარყოფითი ინდექსებით შესაძლებელია დაიწყო slice-ი სტრიქონის ბოლოდან


"""
Python-ში არის ჩაშენეული მეთოდეები რომლებიც შეიძლება გამოვიყენოთ სტრინგის მოდიფიკაციისთვის 
ყველა მეთოდი: https://www.w3schools.com/python/python_strings_methods.asp
"""

a = "Hello, World! "
print(a.upper()) # მეთოდი upper()აბრუნებს სტრიქონს დიდი ასოებით
print(a.lower()) # მეთოდი lower()აბრუნებს სტრიქონს პატარა ასოებით
print(a.strip()) # მეთოდი strip()შლის ნებისმიერ ცარიელ სივრცეს დასაწყისიდან ან ბოლოდან
print(a.replace("H", "J")) # მეთოდი replace()ცვლის სტრიქონს სხვა სტრიქონით
print(a.split(",")) # მეთოდი split()ყოფს სტრიქონს ქვესტრინგებად, თუ ის პოულობს გამყოფის ეგზემპლარებს და აბრუნებს სიას

"""
ორი სტრიქონის შესაერთებლად ან გასაერთიანებლად შეგვიძლია გამოვიყენოთ "+" ოპერატორი 
(ეს მუშაობს მხოლოდ String-ებზე)
"""
a = "Hello"
b = "World"
c = a + b
print(c)

"""
სხვა ტიპის ცვალდების გამოსაყენებად შესაძლებელია ქვედა formationg-ის გამოყენება 
"""
age = 29
text = f"My name is John, I am {age}"
print(text)
