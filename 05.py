my_str =raw_input  ('enter string')
rev_str = reversed(my_str)
if list(my_str) == list(rev_str):
      print("String is palindrome")
else:
      print("String is not palindrome")
