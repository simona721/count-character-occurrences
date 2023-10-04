print("Counting character occurrences.")

text = "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Optio, nulla!"

count = {}

for i in text:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

print(count)


#For a specific character
counter = text.count("o")
#print(f"The number of o in text is: {counter}")