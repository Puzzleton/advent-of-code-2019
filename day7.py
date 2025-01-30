import itertools

ORIGINAL_INPUT = '3,8,1001,8,10,8,105,1,0,0,21,34,59,68,85,102,183,264,345,426,99999,3,9,101,3,9,9,102,3,9,9,4,9,99,3,9,1002,9,4,9,1001,9,2,9,1002,9,2,9,101,5,9,9,102,5,9,9,4,9,99,3,9,1001,9,4,9,4,9,99,3,9,101,3,9,9,1002,9,2,9,1001,9,5,9,4,9,99,3,9,1002,9,3,9,1001,9,5,9,102,3,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,99'
TEST_INPUT_1 = '3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0'
TEST_INPUT_2 = '3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0'
TEST_INPUT_3 = '3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0'
ALL_POSSIBLE_PHASE_SETTINGS = list(itertools.permutations([0,1,2,3,4]))

input = ORIGINAL_INPUT
inputList = input.split(',')
inputList = [int(inputString) for inputString in inputList]
currentGlobalInputIndex = 0
globalPosition = 0
highestOutput = 0
output = 0
globalInputs = []

def resetOpCodeVariables(inputs):
  global globalPosition
  global output
  global globalInputs
  global currentGlobalInputIndex
  input = ORIGINAL_INPUT
  inputList = input.split(',')
  inputList = [int(inputString) for inputString in inputList]
  globalInputs = inputs
  currentGlobalInputIndex = 0
  globalPosition = 0
  output = 0

def opcode1(aPosition, bPosition, cPosition):
  # adds together numbers read from two positions and stores the result in a third position
  inputList[cPosition] = inputList[aPosition] + inputList[bPosition]

def opcode2(aPosition, bPosition, cPosition):
  # multiplies together numbers read from two positions and stores the result in a third position
  inputList[cPosition] = inputList[aPosition] * inputList[bPosition]

def opcode3(position):
  # looks at the next global input and saves it to the position given by its only parameter
  global currentGlobalInputIndex
  inputList[position] = globalInputs[currentGlobalInputIndex]
  currentGlobalInputIndex += 1

def opcode4(position):
  # outputs the value of its only parameter
  global output
  output = inputList[position]

def opcode5(a, b):
  global globalPosition
  # jump-if-true: if the first parameter (a) is non-zero, it sets the instruction pointer (globalPosition) to the value from the second parameter (b). Otherwise, it increments the instruction pointer by 3.
  if inputList[a] == 0:
    globalPosition += 3
  else:
    globalPosition = inputList[b]

def opcode6(a, b):
  global globalPosition
  # jump-if-false: if the first parameter is zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it increments the instruction pointer by 3.
  if inputList[a] == 0:
    globalPosition = inputList[b]
  else:
    globalPosition += 3

def opcode7(a, b, position):
  # less than: if the first parameter (a) is less than the second parameter (b), it stores `1` in the position given by the third parameter. Otherwise, it stores `0`.
  if inputList[a] < inputList[b]:
    inputList[position] = 1
  else:
    inputList[position] = 0

def opcode8(a, b, position):
  # equals: if the first parameter is equal to the second parameter, it stores `1` in the position given by the third parameter. Otherwise, it stores `0`.
  if inputList[a] == inputList[b]:
    inputList[position] = 1
  else:
    inputList[position] = 0

# Pass parameterModes as a string (e.g. `000` or `010`)
def getParameterValues(parameterModes, *parameters):
  parameterValues = []
  for index, parameter in enumerate(parameters):
    # 0 = "position mode"
    # 1 = "immediate mode"
    mode = parameterModes[2 - index]
    if mode == '0':
      parameterValues.append(inputList[parameter])
    else:
      parameterValues.append(parameter)
  return parameterValues

def runOpCodeComputer(inputs):
  global globalPosition
  resetOpCodeVariables(inputs)

  while globalPosition < len(inputList):
    opcode = "{:05d}".format(inputList[globalPosition])
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
      # print(inputList)
      globalPosition = len(inputList)
      break
    else:
      print(modes, opcode)
      raise Exception('Invalid opcode')

# Loop through phase settings permutations
for phaseSettings in ALL_POSSIBLE_PHASE_SETTINGS:
  # Loop through current phase settings
  for phaseSetting in phaseSettings:
    # Run op code computer with previous inputList
    runOpCodeComputer([phaseSetting, output])
    
  if output > highestOutput:
    highestOutput = output
  # Finished all phase settings in list, reset initial output to 0
  output = 0


print(highestOutput)

