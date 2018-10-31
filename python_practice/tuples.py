dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#we cannot do  dimensions[0] = 250 it will give
#TypeError: 'tuple' object does not support item assignment

dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
 print(dimension)

dimensions = (400, 100)   # it is ok as we can overwrite a tuple
print("\nModified dimensions:")
for dimension in dimensions:
 print(dimension)

print("\n\n\n")

foods=('karahi','korma','bihari kabab','ande wala burger')
print("Previous menu")
for food in foods:
    print(food)

print("\n\n")
print("Updated menu")
foods=('kunna','biryani','bihari kabab','ande wala burger')
for food in foods:
    print(food)

