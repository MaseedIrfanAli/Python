# Question 1: Accessing the First Character
# The first character of a string can be accessed using indexing at position 0.

sample_string = "Hello world"
first_character = sample_string[0]
print("First character:", first_character)
# Explanation: Indexing starts at 0, so sample_string[0] gives the first character.


# Question 2: Accessing the Last Character
# The last character of a string can be accessed using negative indexing, e.g., -1.

sample_string = "Goodbye"
last_character = sample_string[-1]
print("Last character:", last_character)
# Explanation: Negative indexing starts from the end, so -1 refers to the last character.

# Question 3: Slicing a Substring
# A substring can be extracted using slicing, specifying start and end indices.

phrase = "Hello world"
hello = phrase[0:5]
print("Extracted substring:", hello)
# Explanation: Slicing from 0 to 5 extracts "Hello".

# Question 3: Slicing a Substring
# A substring can be extracted using slicing, specifying start and end indices.

phrase = "Hello world"
hello = phrase[0:5]
print("Extracted substring:", hello)
# Explanation: Slicing from 0 to 5 extracts "Hello".

# Question 4: Reversing a String
# A string can be reversed using slicing with a step of -1.

sample_string = "Python"
reversed_string = sample_string[::-1]
print("Reversed string:", reversed_string)
# Explanation: Slicing with a step of -1 reverses the string.


# Question 5: Skipping Characters in a Slice
# Every other letter can be extracted using a step in the slice notation.

sample_string = "abcdefghijk"
every_other_letter = sample_string[::2]
print("Every other letter:", every_other_letter)
# Explanation: The step parameter 2 in slicing skips every other character.

# Question 6: Default Values in Slicing
# Omitting the start or end index in slicing uses default values for the beginning or end of the string.

phrase = "Hello world"
first_five = phrase[:5]
after_three = phrase[3:]
print("First five characters:", first_five)
print("After the third character:", after_three)
# Explanation: [:5] slices from the beginning to index 4, and [3:] slices from index 3 to the end.


# Question 7: Negative Indices in Slicing
# Negative indices can be used to slice from the end of the string.

phrase = "Hello world"
world = phrase[-5:]
print("Extracted word:", world)
# Explanation: Negative indices count backwards, so -5: slices the last five characters.


# Question 8: Length of a Slice
# The length of a slice can be determined using the len() function.

hello = "Hello world"[:5]
length_of_hello = len(hello)
print("Length of 'Hello':", length_of_hello)
# Explanation: len() calculates the number of characters in the slice.


# Question 9: Slicing with Out-of-range Indices
# Using out-of-range indices in slicing does not throw an error; Python handles it gracefully.

short_string = "Short"
slice_out_of_range = short_string[0:100]
print("Slice with out-of-range index:", slice_out_of_range)
# Explanation: Python slices up to the end of the string without errors, even if the end index is out of range.


# Question 10: Immutable Strings Modification Attempt
# Attempting to change a character in a string through indexing is not possible due to string immutability.

# sample_string = "Python"
# sample_string[0] = "J"  # This would raise a TypeError because strings are immutable.

# Explanation: Since strings are immutable, attempting to change them directly through indexing results in an error.









 
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Question 1: Creating Strings
# Strings in Python can be created by enclosing text in single ('') or double ("") quotes.
# This allows for the creation of text-based data in your code.

greeting = "Hello World!"
print("Greeting:", greeting)
# Explanation: The greeting variable is assigned a string enclosed in double quotes.

# Question 2: String Length Concept
# The len() function can be used to find out the number of characters in a string, including spaces.

example_string = "Python is fun!"
length = len(example_string)
print("Number of characters:", length)
# Explanation: len() counts each character (including spaces) in the string.


# Question 3: Concatenating Strings
# Two or more strings can be joined together (concatenated) using the + operator.

hello = "Hello"
world = "World"
greeting = hello + " " + world
print("Greeting:", greeting)
# Explanation: The + operator is used to concatenate "Hello" and "World" with a space in between.

# Question 4: Using Newline Characters
# The newline character \n is used to create a new line in a string.

multi_line_string = "Hello\nWorld!"
print("Multi-line String:\n", multi_line_string)
# Explanation: \n within the string causes "World!" to be printed on a new line.


# Question 5: Accessing String Characters
# Individual characters in a string can be accessed using indexing. Indexes start at 0.

string = "Data"
first_character = string[0]
print("First character:", first_character)
# Explanation: The first character of "Data" is accessed using string[0].


# Question 6: Understanding String Slicing
# String slicing is used to extract a portion of a string using the syntax [start:end].

phrase = "Hello World!"
world = phrase[6:11]
print("Extracted part:", world)
# Explanation: Slicing from index 6 to 11 extracts "World" from "Hello World!".


# Question 7: Immutability of Strings
# Strings in Python are immutable, meaning once created, their characters cannot be changed.

original = "Hello"
# Attempt to change 'H' to 'J' will result in an error
# Correct approach is to create a new string
corrected = "J" + original[1:]
print("Corrected string:", corrected)
# Explanation: Demonstrates creating a new string "Jello" since strings are immutable.

# Question 8: The Significance of Escape Characters
# Escape characters like \n (newline) and \t (tab) allow for inserting special characters in strings.

example_with_tab = "Hello\tWorld!"
print("String with tab:", example_with_tab)
# Explanation: \t inserts a tab space between "Hello" and "World!".
# Question 9: String Concatenation Without Operators
# String literals placed next to each other are automatically concatenated.

concatenated_string = "Hello " "World!"
print("Concatenated string:", concatenated_string)
# Explanation: Placing string literals next to each other concatenates them.

# Question 10: Incorporating Variables in Strings
# Before the introduction of f-strings, variables could be included in strings through concatenation or the str() function.

age = 25
message = "Your age is " + str(age)
print("Message:", message)
# Explanation: Demonstrates using the str() function to include the integer variable age in a string.
###############################################################################
# Question 1: Finding a Substring
# To find the first occurrence of a substring, the find() method can be used.

sample_string = "Learning Python with Python tutorials"
index_of_python = sample_string.find("Python")
print("First occurrence of 'Python':", index_of_python)
# Explanation: find() returns the lowest index where the substring "Python" begins.

# Question 2: Counting Substring Occurrences
# The count() method returns the number of non-overlapping occurrences of a substring.

sample_string = "This is an island"
count_is = sample_string.count("is")
print("'is' appears:", count_is, "times")
# Explanation: count("is") counts how many times "is" appears in the string.
# Question 3: Checking String Start
# The startswith() method checks if a string starts with a specified prefix.

sample_string = "Python programming is fun."
starts_with_python = sample_string.startswith("Python")
print("Starts with 'Python':", starts_with_python)
# Explanation: startswith("Python") returns True if the string starts with "Python".

# Question 4: Reversing Words Order
# To reverse the order of words in a sentence, split the string into words, reverse the list, then join it back into a string.

sentence = "Hello World Python"
reversed_order = " ".join(sentence.split()[::-1])
print("Reversed order of words:", reversed_order)
# Explanation: Splitting the string into a list of words, reversing it, and then joining back into a string.

# Question 4: Reversing Words Order
# To reverse the order of words in a sentence, split the string into words, reverse the list, then join it back into a string.

sentence = "Hello World Python"
reversed_order = " ".join(sentence.split()[::-1])
print("Reversed order of words:", reversed_order)
# Explanation: Splitting the string into a list of words, reversing it, and then joining back into a string.

# Question 6: Removing Leading Characters
# To remove all leading characters (not just whitespace), the lstrip() method can be used.

sample_string = "0001234"
trimmed_string = sample_string.lstrip("0")
print("Trimmed leading zeros:", trimmed_string)
# Explanation: lstrip("0") removes all leading "0" characters

# Question 7: Checking Digit Characters
# To check if a string consists only of digit characters, the isdigit() method can be used.

sample_string = "12345"
all_digits = sample_string.isdigit()
print("All digit characters:", all_digits)
# Explanation: isdigit() returns True if all characters in the string are digits.


# Question 8: Swapping Letter Case
# To swap the case of all letters in a string, the swapcase() method can be used.

sample_string = "Python 3.9"
swapped_case_string = sample_string.swapcase()
print("Swapped case string:", swapped_case_string)
# Explanation: swapcase() inverts the case of all letters.

# Question 9: Joining with a Separator
# To create a string from a collection of strings with a separator, the join() method is used.

fruit_list = ["apple", "banana", "cherry"]
comma_separated = ",".join(fruit_list)
print("Comma-separated string:", comma_separated)
# Explanation: join() concatenates elements with a comma.

# Question 10: Stripping Substring from Ends
# To remove specified characters from both the beginning and end of a string, strip() can be used.

sample_string = "xxHello Worldxx"
trimmed_string = sample_string.strip("x")
print("Trimmed string:", trimmed_string)
# Explanation: strip("x") removes "x" characters from both ends of the string.