import sys
import math

if len(sys.argv) != 2 or math.isnan(int(sys.argv[1])):
  raise Exception('A single global input of type integer is required (e.g. `python3 day5.py 1`)')
globalInput = int(sys.argv[1])

input = '3,225,1,225,6,6,1100,1,238,225,104,0,1101,65,73,225,1101,37,7,225,1101,42,58,225,1102,62,44,224,101,-2728,224,224,4,224,102,8,223,223,101,6,224,224,1,223,224,223,1,69,126,224,101,-92,224,224,4,224,1002,223,8,223,101,7,224,224,1,223,224,223,1102,41,84,225,1001,22,92,224,101,-150,224,224,4,224,102,8,223,223,101,3,224,224,1,224,223,223,1101,80,65,225,1101,32,13,224,101,-45,224,224,4,224,102,8,223,223,101,1,224,224,1,224,223,223,1101,21,18,225,1102,5,51,225,2,17,14,224,1001,224,-2701,224,4,224,1002,223,8,223,101,4,224,224,1,223,224,223,101,68,95,224,101,-148,224,224,4,224,1002,223,8,223,101,1,224,224,1,223,224,223,1102,12,22,225,102,58,173,224,1001,224,-696,224,4,224,1002,223,8,223,1001,224,6,224,1,223,224,223,1002,121,62,224,1001,224,-1302,224,4,224,1002,223,8,223,101,4,224,224,1,223,224,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1008,226,677,224,102,2,223,223,1005,224,329,1001,223,1,223,7,677,226,224,102,2,223,223,1006,224,344,1001,223,1,223,1007,226,677,224,1002,223,2,223,1006,224,359,1001,223,1,223,1007,677,677,224,102,2,223,223,1005,224,374,1001,223,1,223,108,677,677,224,102,2,223,223,1006,224,389,101,1,223,223,8,226,677,224,102,2,223,223,1005,224,404,101,1,223,223,7,226,677,224,1002,223,2,223,1005,224,419,101,1,223,223,8,677,226,224,1002,223,2,223,1005,224,434,101,1,223,223,107,677,677,224,1002,223,2,223,1006,224,449,101,1,223,223,7,677,677,224,1002,223,2,223,1006,224,464,101,1,223,223,1107,226,226,224,102,2,223,223,1006,224,479,1001,223,1,223,1007,226,226,224,102,2,223,223,1006,224,494,101,1,223,223,108,226,677,224,1002,223,2,223,1006,224,509,101,1,223,223,1108,226,677,224,102,2,223,223,1006,224,524,1001,223,1,223,1008,226,226,224,1002,223,2,223,1005,224,539,101,1,223,223,107,226,226,224,102,2,223,223,1006,224,554,101,1,223,223,8,677,677,224,102,2,223,223,1005,224,569,101,1,223,223,107,226,677,224,102,2,223,223,1005,224,584,101,1,223,223,1108,226,226,224,1002,223,2,223,1005,224,599,1001,223,1,223,1008,677,677,224,1002,223,2,223,1005,224,614,101,1,223,223,1107,226,677,224,102,2,223,223,1005,224,629,101,1,223,223,1108,677,226,224,1002,223,2,223,1005,224,644,1001,223,1,223,1107,677,226,224,1002,223,2,223,1006,224,659,1001,223,1,223,108,226,226,224,102,2,223,223,1006,224,674,101,1,223,223,4,223,99,226'
inputList = input.split(',')
globalPosition = 0

output = [int(inputString) for inputString in inputList]

def opcode1(aPosition, bPosition, cPosition):
  # adds together numbers read from two positions and stores the result in a third position
  output[cPosition] = output[aPosition] + output[bPosition]

def opcode2(aPosition, bPosition, cPosition):
  # multiplies together numbers read from two positions and stores the result in a third position
  output[cPosition] = output[aPosition] * output[bPosition]

def opcode3(position):
  # takes a single integer as input and saves it to the position given by its only parameter
  output[position] = globalInput

def opcode4(position):
  # outputs the value of its only parameter
  print(output[position])

def opcode5(a, b):
  global globalPosition
  # jump-if-true: if the first parameter (a) is non-zero, it sets the instruction pointer (globalPosition) to the value from the second parameter (b). Otherwise, it increments the instruction pointer by 3.
  if output[a] == 0:
    globalPosition += 3
  else:
    globalPosition = output[b]

def opcode6(a, b):
  global globalPosition
  # jump-if-false: if the first parameter is zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it increments the instruction pointer by 3.
  if output[a] == 0:
    globalPosition = output[b]
  else:
    globalPosition += 3

def opcode7(a, b, position):
  # less than: if the first parameter (a) is less than the second parameter (b), it stores `1` in the position given by the third parameter. Otherwise, it stores `0`.
  if output[a] < output[b]:
    output[position] = 1
  else:
    output[position] = 0

def opcode8(a, b, position):
  # equals: if the first parameter is equal to the second parameter, it stores `1` in the position given by the third parameter. Otherwise, it stores `0`.
  if output[a] == output[b]:
    output[position] = 1
  else:
    output[position] = 0

# Pass parameterModes as a string (e.g. `000` or `010`)
def getParameterValues(parameterModes, *parameters):
  parameterValues = []
  for index, parameter in enumerate(parameters):
    # 0 = "position mode"
    # 1 = "immediate mode"
    mode = parameterModes[2 - index]
    if mode == '0':
      parameterValues.append(output[parameter])
    else:
      parameterValues.append(parameter)
  return parameterValues

while globalPosition < len(output):
  opcode = "{:05d}".format(output[globalPosition])
  modes = opcode[:3]
  opcode = opcode[-2:]
  
  if opcode == '01':
    opcode1(*getParameterValues(modes, globalPosition + 1, globalPosition + 2, globalPosition + 3))
    globalPosition += 4
  elif opcode == '02':
    opcode2(*getParameterValues(modes, globalPosition + 1, globalPosition + 2, globalPosition + 3))
    globalPosition += 4
  elif opcode == '03':
    opcode3(*getParameterValues(modes, globalPosition + 1))
    globalPosition += 2
  elif opcode == '04':
    opcode4(*getParameterValues(modes, globalPosition + 1))
    globalPosition += 2
  elif opcode == '05':
    opcode5(*getParameterValues(modes, globalPosition + 1, globalPosition + 2))
  elif opcode == '06':
    opcode6(*getParameterValues(modes, globalPosition + 1, globalPosition + 2))
  elif opcode == '07':
    opcode7(*getParameterValues(modes, globalPosition + 1, globalPosition + 2, globalPosition + 3))
    globalPosition += 4
  elif opcode == '08':
    opcode8(*getParameterValues(modes, globalPosition + 1, globalPosition + 2, globalPosition + 3))
    globalPosition += 4
  elif opcode == '99':
    print(output)
    globalPosition = len(output)
    break
  else:
    print(modes, opcode)
    raise Exception('Invalid opcode')
