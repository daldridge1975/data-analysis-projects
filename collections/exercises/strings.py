# ---- Exercise 2: Bracket Notation Basics ----

text = 'Strings_are_sequences_of_characters.'
word = 'tomato'

# 1. Print a slice of the first 12 characters from 'text'.

# first_12_characters= text[0:12]
# # print(text)    

# 2. Print a slice of the last 12 characters from 'text'. You should NOT have to count the index values yourself!
# last_12_characters = text[-12:]
# print(last_12_characters)

# 3. Print a slice of the middle 12 characters from 'text'.
# length = len(text)
# slice_length= 12
# middle_12_characters= text[last_12_characters__index:first_12_characters__index
                           

# ---- Exercise 3: Looping Through a String ----

# Use index values to loop backwards through 'word'.

1. 
# word= "success"
# index= len(word)-1
# for index in range(index, -1,-1):
#     print(word[])
  
    



# 2. Refactor the code to use the accumulator pattern to build up and print the reversed string. For example, if given 'good', print 'doog' on one line.
# 
# word= "good"
# reversed_word= ""
# index= len(word)-1
# for index in range(index, -1, -1):
#     print(word[index])

# 3. Refactor the code to print a combination of the original and reversed string. For example, given 'tomato', print 'tomatootamot'. (If you want to be fancy, print 'tomato | otamot').
word= "good"
reversed_word= word[::-1]
combined_string= f"{word} | {reversed_word}"
print(combined_string)