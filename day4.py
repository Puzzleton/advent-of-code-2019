input = '272091-815432'
range_start, range_end = input.split('-')

VALID_PASSWORD = 5
GENERIC_INVALID_PASSWORD = -1

output = 0

# def parseInputIntoStrings():

def passwordChecker(password):
  # '133456' -> ['1', '3', '3', '4', '5', '6']
  characters = list(password)

  # INVALID: Length not 6
  if len(characters) != 6:
    return -1
  
  # INVALID: Password out of range
  if password < range_start or password > range_end:
    return -1

  # INVALID: No repeats or descending value or triplet
  is_repeat_present = False
  # Loop through characters, comparing digit ahead for ascending value or repeat
  for index, value in enumerate(characters):
    if index < len(characters) - 1:
      value_ahead_one_position = characters[index + 1]
      if value > value_ahead_one_position:
        return index
      # if index < len(characters) - 2:
      #   value_ahead_two_positions = characters[index + 2]
      #   if value == value_ahead_one_position and value == value_ahead_two_positions:
      #     return False
      if value == value_ahead_one_position:
        is_repeat_present = True
    else:
      if not(is_repeat_present):
        return -1
  return 5

# Example steps to find the next valid password:
# Check 272091 as our start input (*** = INVALID)
# Find the next available password by copying the digit before the first descending value (277777)
# Find the next available password by increasing the number by 1 until it creates a descending value (277778, 277779, ***277780***)
# From the invalid descending value, the next valid password is created by copying the digit before the first descending value (277788)
# 277789
# ***277790*** copy -> 277799
# ***277800*** copy -> 277888
def findNextValidPassword(password):
  return str(int(password) + 1)

def main():
  valid_counter = 0
  current_password = range_start
  first_result = passwordChecker(current_password)
  if first_result == VALID_PASSWORD:
    valid_counter += 1
  while current_password < range_end:
    next_password = findNextValidPassword(current_password)
    if next_password <= range_end:
      valid_counter += 1
    current_password = next_password
  print(valid_counter)

main()
