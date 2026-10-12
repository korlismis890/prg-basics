###
# String manipulation
#

movie = "The Lord of the Rings: The Return of the King"

# print number of characters
print('Number of characters: ', len(movie))

# print title in capital letters
print(f'Title in capital letters: {movie.upper()}')

# print title in small letters
print(f'Title in small letters: {movie.lower()}')

# print how many times the vowel "e" appears in the title
print(f"Amount of e's: {movie.count('e')}")

# print where in the text is the word "Lord"
print(f'Place where the word "Lord" is: {movie.find('Lord')}')