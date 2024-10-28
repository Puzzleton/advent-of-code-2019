input = '1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,2,19,9,23,1,23,5,27,2,6,27,31,1,31,5,35,1,35,5,39,2,39,6,43,2,43,10,47,1,47,6,51,1,51,6,55,2,55,6,59,1,10,59,63,1,5,63,67,2,10,67,71,1,6,71,75,1,5,75,79,1,10,79,83,2,83,10,87,1,87,9,91,1,91,10,95,2,6,95,99,1,5,99,103,1,103,13,107,1,107,10,111,2,9,111,115,1,115,6,119,2,13,119,123,1,123,6,127,1,5,127,131,2,6,131,135,2,6,135,139,1,139,5,143,1,143,10,147,1,147,2,151,1,151,13,0,99,2,0,14,0'

inputList = input.split(',')

output = [int(inputString) for inputString in inputList]

output[1] = 53
output[2] = 98

def opcode1(aPosition, bPosition, cPosition):
  aValue = output[aPosition]
  bValue = output[bPosition]
  cValue = output[cPosition]
  output[cValue] = output[aValue] + output[bValue]

def opcode2(aPosition, bPosition, cPosition):
  aValue = output[aPosition]
  bValue = output[bPosition]
  cValue = output[cPosition]
  output[cValue] = output[aValue] * output[bValue]

for position in range(0, len(output) - 1, 4):
  if output[position] == 1:
    opcode1(position + 1, position + 2, position + 3)
  elif output[position] == 2:
    opcode2(position + 1, position + 2, position + 3)
  elif output[position] == 99:
    print(output) 
    break
