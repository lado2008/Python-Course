"""
bool მნიშვნელობები წარმოადგენს ორიდან ერთ-ერთ მნიშვნელობას: True ან False

როდესაც ორ მნიშვნელობას ადარებთ, გამოსახულება ფასდება და
Python აბრუნებს ლოგიკურ პასუხს
"""
print(10 > 8)
print(10 == 8)
print(10 < 8)

"""
როდესაც if ოპერატორში პირობა სრულდება, ის აბრუნებს True ან False 
"""
a = 200
b = 100

if b > a:
    print("b is greater than a")
else:
    print("b is not greader than a")

"""
ფუნქცია bool() საშუალებას იძლევა შაფასოსო ნებისმიერი მნიშვნელობა და სანაცვლოდ მოგვცეს True ან False

მნიშვნელობების უმეტესობა True-ა:
- ნებისმიერი String-ი არის True, ცარიელი String-ების გარდა.
- ნებისმიერი რიცხვი არის True, გარდა 0
- ნებისმიერი სია, Tuple-ი, სიმრავლე და Dictionary-ი არის True, ცარიელი სიების გარდა.

არც ისე ბევრი მნიშვნელობაა, რომელიც ფასდება False, გარდა ცარიელი მნიშვნელობებისა, როგორიცაა (), [], {}, "", რიცხვი 0და მნიშვნელობა None.
"""
x = "Hello"
y = 15

# True:
print(bool(x)) 
print(bool(y))

bool("something") 
bool(123) 
bool(["one", "two", "three"])

# False
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

"""
ასვე შესაძლებელია ფუნქციების შექმნა, რომლებიც აბრუნებენ ლოგიკურ მნიშვნელობებს  
"""
def myFunction():
    return True

if myFunction():
    print("Yes")
else:
    print("No")

"""
Python-ში არის isinstance() ფუნქცია რომელიც გამოიყენება იმის დასადგენად,
ობიექტი გარკვეული მონაცემთა ტიპისაა თუ არა
"""
x = 200
print(isinstance(x, int))