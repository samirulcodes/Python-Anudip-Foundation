# Q1.WAP to Count occurrences of each word in a sentence
# string = "To change the overall look of your document. To change the look available in the gallery"

string = "To change the overall look of your document. To change the look available in the gallery"

# Split the string into words
words = string.split()

# Creating an empty dictionary to store word counts (here we can use list also to store words)
word_count = {}

# Count the occurrences of each word
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Print the word counts
for word, count in word_count.items():
    print(f"{word}: {count}")

# output :
# To: 2
# change: 2
# the: 3
# overall: 1
# look: 2
# of: 1
# your: 1
# document.: 1
# available: 1
# in: 1
# gallery: 1


# Q2.WAP to Remove newlines from a string
# string = "\nBest \nDeeptech \nPython \nTraining\n"

string = "\nBest \nDeeptech \nPython \nTraining\n"

# Removing the newlines using the replace method
removing_newLine = string.replace('\n', '')

print(removing_newLine)  
# output -- Best Deeptech Python Training


# Q3. WAP to Reverse words in a string
# string = "Deeptech Python Training"

string = "Deeptech Python Training"

# Split the string into words
words = string.split()

# Reverse the order of words using slicing
reversed_words = words[::-1]

# Join the reversed words back into a string using join method
reversed_string = ' '.join(reversed_words)

print(reversed_string)



# Q4  Count and display vowels in a text
# string = "Welcome to python Training"

string = "Welcome to python Training"

# Defining vowels
vowels = "aeiouAEIOU"

# Initializing vowel count to 0
vowel_count = 0

# Iterate through each character in the string
for char in string:
    if char in vowels:
        vowel_count += 1

print(f"Number of vowels in: {string} is: {vowel_count}")
# output -- Number of vowels in: Welcome to python Training is: 8

