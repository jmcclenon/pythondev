class Person:
  def __init__(self, fname, lname, age, account_number, date_joined):
    self.fname = fname
    self.account_number = account_number
    self.age = age
    self.lname = lname
    self.date_joined = date_joined

p1 = Person("big Jack", "Maxwell", 36,45521452111,"08/31/1944")
p2 = Person("Bill", "Williams", 24, 383882338823, "09/22/1990")

print(p1.fname)
print(p1.lname)
print(p1.age)
print(p1.account_number)
print(p1.date_joined)
print(p2.fname)
print(p2.lname)
print(p2.age)
print(p2.account_number)
print(p2.date_joined)

