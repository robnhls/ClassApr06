
names = {"Jack", "Clayton", "Gayle", "Janelle", "Jason", "Jimmie",
         "Jack", "Clayton", "Gayle", "Janelle", "Jason", "Jimmie", "MichaelB", "MichaelL"}

dictionary = {"Rolondo": "NYC", "MichaelB": "Columbus", "MichaelL": "Miami",
              "Paul": "St. Paul", "Todd": "Bowie"}


print(len(names))
print(len(dictionary))


for n in names:
    print(n)


s1 = {"a", "b", "c"}
s2 = {"c", "d", "e"}

s3 = s1 | s2
s3 = s1.union(s2) # easier to read, so better


answer = 10 + 3
