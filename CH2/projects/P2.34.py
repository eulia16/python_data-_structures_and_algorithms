#program that inputs a document and the outputs a bar chart plot of the frequencies of each alphabet character that appears in that document
#we will use the text file we downloaded from the internet called sample1.txt for simplicity's sake

from collections import Counter
import matplotlib.pyplot as plt

path = 'sample1.txt'
fp = open(path, 'r')
#print(fp.read())
string = fp.read()

collection = Counter(string)
print(collection)

fp.close()

#we now have all the characters counted in a data structure, we will now use matplotLib to display the frequency of each letter of the alphabet in a bar chart plot

letters = collection.keys()
values = collection.values()

print(letters)
print(values)

fig = plt.figure(figsize = (10, 5))

plt.bar(letters, values, color = "maroon", width = 0.4)

plt.xlabel("letters in document")
plt.ylabel("frequency of letters")
plt.title("Some cool shit yo")
plt.show()

