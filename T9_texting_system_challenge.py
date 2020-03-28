"""
Write an algorithm in pseudo code or a language of your choice that finds the largest two or more words 
(from e.g. this dictionary or just a hypothetical empty or example array) that have exactly the same sequence
of keypresses using the T9 texting system. The T9 texting system is a quick way of typing words with a phone keypad.
Each number on the keypad is assigned to multiple letters, but you only press once per letter in the word, without 
indicating which of the 3 or 4 assigned letters you intend to use.

The keypad number-to-letter mappings are:
2: abc
3: def
4: ghi
5: jkl
6: mno
7: pqrs
8: tuv
9: wxyz

So the word "insight" would be 4674448 in T9 (it would not be 444 66 7777 444 4 44 8). An example of two words with the same sequence would be "car" and "abs" (both 227).

"""


def character_to_keypad_number(char):
  """
  Given character return its corresponding keypad number.
  """
  if char in ['a', 'b', 'c']:
    return '2'
  elif char in ['d', 'e', 'f']:
    return '3'
  elif char in ['g', 'h', 'i']:
    return '4'
  elif char in ['j', 'k', 'l']:
    return '5'
  elif char in ['m', 'n', 'o']:
    return '6'
  elif char in ['p', 'q', 'r', 's']:
    return '7'
  elif char in ['t', 'u', 'v']:
    return '8'
  elif char in ['w', 'x', 'y', 'z']:
    return '9'
  
def keypress_from_word(word):
  """
  Given a word, return it's keypress sequence.
  """
  return ''.join([character_to_keypad_number(char) for char in list(word)])
  

def load(this_dictionary):
  """
  Given the dictionary in question, loads the sequence of words into a dictionary. Where the key is the keypress, and the value a list of words that can be made with that corresponding keypress.
  """
  loaded_dict = {}
  for word in this_dictionary:
    keypress = keypress_from_word(word)

    # if keypress key doesn't exist in loaded_dict create an empty list as a value
    if loaded_dict.get(keypress, False) == False:
      loaded_dict[keypress] = []

    loaded_dict[keypress].append(word)

  return loaded_dict

def output(this_dictionary, keypress):
  """
  Given dictionary of words 'this_dictionary', and keypress sequence 'keypress'.
  Output the two largest or more words.
  """
  loaded_dict = load(this_dictionary)
  return loaded_dict[str(keypress)]

# Testing
print(character_to_keypad_number('a')) # expect 2
print(keypress_from_word('cat')) # expect 228

test_dictionary = ['cat', 'car', 'abs']
print(load(test_dictionary)) # expect {'228': ['cat'], '227': ['car', 'abs']}

test_keypress = 227
print(output(test_dictionary, test_keypress)) # expect ['car', 'abs']
