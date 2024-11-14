input = '272091-815432'
range_start, range_end = input.split('-')

VALID_PASSWORD = 5
GENERIC_INVALID_PASSWORD = -1

output = 0

# def parseInputIntoStrings():

# 133456
# 3 3 3 5 8 8

def passwordChecker(password):
  # '133456' -> ['1', '3', '3', '4', '5', '6']
  characters = list(password)

  # INVALID: Length not 6
  if len(characters) != 6:
    return GENERIC_INVALID_PASSWORD
  
  # INVALID: Password out of range
  if password < range_start or password > range_end:
    return GENERIC_INVALID_PASSWORD

  # INVALID: No repeats or descending value or triplet
  is_repeat_present = False
  # Loop through characters, comparing digit ahead for ascending value or repeat
  for index, value in enumerate(characters):
    if index < len(characters) - 1:
      value_ahead_one_position = characters[index + 1]
      # We detect a descending value
      if value > value_ahead_one_position:
        return index
      # We find the surrounding values
      value_behind_one_position = None
      value_ahead_two_positions = None
      if index > 0:
        value_behind_one_position = characters[index - 1]
      if index < len(characters) - 2:
        value_ahead_two_positions = characters[index + 2]

      # We detect a double
      if value == value_ahead_one_position and value != value_ahead_two_positions and value != value_behind_one_position:
        is_repeat_present = True
    else:
      if not(is_repeat_present):
        return GENERIC_INVALID_PASSWORD
  return VALID_PASSWORD

# Potential for optimization by calculating next valid password instead of incrementing by 1
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
    if next_password <= range_end and passwordChecker(next_password) == VALID_PASSWORD:
      valid_counter += 1
    current_password = next_password
  print(valid_counter)

main()
