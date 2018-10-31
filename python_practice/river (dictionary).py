rivers={
    'nile':'egypt',
    'jhelum':'Pakistan',
     'ravi':'India'
}
for name,country in rivers.items():
    print("The river " + name.title() + " flows in " + country.title())

for name in rivers.keys():
    print(name)

print("\n")

for country in set(rivers.values()):  # 'set' simply return the unique values and prevents any repetition
    print(country)

print("\n")

favorite_languages = {
 'jen': ['python', 'ruby'],
 'sarah': ['c'],
 'edward': ['ruby', 'go'],
 'phil': ['python', 'haskell']
 }

for name, languages in favorite_languages.items():
 print("\n" + name.title() + "'s favorite languages are:")
 for language in languages:
  print("\t" + language.title())