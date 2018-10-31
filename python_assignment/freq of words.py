import sys
freq = {}   # frequency of words in text
line = input()
print(line.split())
for word in line.split():
    freq[word] = freq.get(word,0)+1
    print(freq[word])

    words = freq.keys()
    print(words)
for w in words:
    print ("%s:%d" % (w,freq[w]))



# split is for taking words in place as a single one before any space

# getk