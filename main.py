import string

def count_characters(text):
    # Create an empty dictionary to store the character counts
    char_count = {}
    
    # Loop through each character in the text
    for char in text.lower():
        if char in string.ascii_lowercase:  # Only count alphabetic characters
            if char in char_count:
                char_count[char] += 1  # Increment the count if the character already exists
            else:
                char_count[char] = 1  # Initialize the count if the character is encountered for the first time
    
    return char_count

def count_words(text):
    # Split the text into words and count them
    words = text.lower().split()
    word_count = {}
    
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
            
    return word_count

# Open the file and read the contents
with open('books/frankenstein.txt') as f:
    file_contents = f.read()

# Call the functions and capture the results
character_count = count_characters(file_contents)
word_count = count_words(file_contents)

# Print the character counts in the required format
print("Character counts (alphabetic only):")
for char, count in sorted(character_count.items()):
    print(f"'{char}': {count}")

# Print a newline for separation
print("\nWord counts:")
# Print the word counts (optional, you can filter for specific words if needed)
for word, count in sorted(word_count.items()):
    print(f"'{word}': {count}")

