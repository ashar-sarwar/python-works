print("hello")
message="python"
print(message)
name="ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name #This method of combining strings is called concatenation
print(full_name)

favorite_language = 'python '
print(favorite_language)                        # strips eliminates whitespaces
favorite_language = favorite_language.rstrip()
print(favorite_language)


favorite_language = ' python'
print(favorite_language)
favorite_language = favorite_language.lstrip()
print(favorite_language)

favorite_language = '  python '
print(favorite_language)
favorite_language = favorite_language.strip()
print(favorite_language)

print('Albert Einstein once said, "A person who never made a mistake never tried anything new."')

print(3 ** 2 )#this means 3 has power 2

age = 21
message = "Happy " + str(age) + "st Birthday!" #we use str() for typecasting
print(message)

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

print(bicycles[1])
print(bicycles[-1])
print(bicycles[-2])

print(bicycles[0].title())

message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati' # it overwrites honda
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('unique')
print(motorcycles)

motorcycles.insert(2, 'ducati') # inserts ducati before unique
print(motorcycles)

# on basis of index position
del motorcycles[0]
print(motorcycles)

#here we can also save the value removed on basis of index by pop()
popped_motorcycle = motorcycles.pop() # if you want to save the deleted item
print(motorcycles)                    #last item is deleted if no index provided
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki']
first=motorcycles.pop(0)
print(first)

#on basis of value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

# Sorting a List Permanently with the sort() Method on basis of
# alphabetic order

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

#Sorting a List Temporarily with the sorted() Function

print("\nHere is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)
#Notice that reverse() doesn’t sort backward alphabetically; it simply
#reverses the order of the list


