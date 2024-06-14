def count_char(word):

  char_count = {}

  for char in word.lower():

    if char not in char_count:
      char_count[char] = 1

    else:
      char_count[char] += 1

  print(char_count)
