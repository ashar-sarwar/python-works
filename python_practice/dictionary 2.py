favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
print("Sarah's favorite language is " +
favorite_languages['sarah'].title() + ".")

#Looping Through All Key-Value Pairs
user={
    'username':'fermi',
    'first':'enrico',
    'last':'rodriguez'
}

for key,value in user.items():
    print("\nKey:"+ key + "\nValue:"+value)

for initials in user.keys():
    print(initials.title())

#same as you write :
print("\n")
for initials in user:
    print(initials.title()) # because of default behaviour will only give keys

#Looping Through a Dictionary’s Keys in Order

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
for name in sorted(favorite_languages.keys()):
  print(name.title() + ", thank you for taking the poll.")


