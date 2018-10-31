cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
 if car == 'bmw':
  print(car.upper())
 else:
  print(car.title())

#Checking Whether a Value Is in a List
requested_toppings = ['mushrooms', 'onions', 'pineapple']
if 'mushrooms' in requested_toppings:
    print("jani hagi")

#Checking Whether a Value Is Not in a List
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
 print(user.title() + ", you can post a response if you wish.")

print('\n')
age = 12
if age < 4:
 print("Your admission cost is $0.")
elif age < 18:
 print("Your admission cost is $5.")
else:
 print("Your admission cost is $10.")