# input = '''R75,D30,R83,U83,L12,D49,R71,U7,L72
# U62,R66,U55,R34,D71,R55,D58,R83'''
input = '''R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'''
output = None

def manhattanDistance(point1, point2):
  return abs(point1['x'] - point2['x']) + abs(point1['y'] - point2['y'])

# "Point" = Dictionary
# a = {
#   'x': 4,
#   'y': 5
# }

# "Line Segment" = Dictionary of Points
# c = {
#   'start': {
#     'x': 0,
#     'y': 0
#   },
#   'end': {
#     'x': 0,
#     'y': 0
#   },
# }

# "Map" = List of Line Segments
# map = [{
#   'start': {
#     'x': 0,
#     'y': 0
#   },
#   'end': {
#     'x': 25,
#     'y': 0
#   },
# }, {
#   'start': {
#     'x': 25,
#     'y': 0
#   },
#   'end': {
#     'x': 25,
#     'y': 30
#   },
# }]

# How do we calculate intersection?
#            8,15
#        c
# d      |
# 4------X-------
#        |
#        |
#        |
# 0,0    0,8

verticalLineSegments1 = []
horizontalLineSegments1 = []

verticalLineSegments2 = []
horizontalLineSegments2 = []

def buildLineSegment(direction, distance, startPoint):
  result = { 'start': startPoint, 'end': None }
  match direction:
    case 'U':
      result['end'] = { 'x': startPoint['x'], 'y': startPoint['y'] + distance }
    case 'D':
      result['end'] = { 'x': startPoint['x'], 'y': startPoint['y'] - distance }
    case 'L':
      result['end'] = { 'x': startPoint['x'] - distance, 'y': startPoint['y'] }
    case _:
      result['end'] = { 'x': startPoint['x'] + distance, 'y': startPoint['y'] }
  return result

def buildLineSegments():
  wire1, wire2 = input.split('\n')
  for move in wire1.split(','):
    direction = move[:1]
    distance = int(move[1:])
    if direction == 'U' or direction == 'D':
      startPoint = {'x': 0, 'y': 0} if len(horizontalLineSegments1) == 0 else horizontalLineSegments1[-1]['end']
      lineSegment = buildLineSegment(direction, distance, startPoint)
      verticalLineSegments1.append(lineSegment)
    if direction == 'L' or direction == 'R':
      startPoint = {'x': 0, 'y': 0} if len(verticalLineSegments1) == 0 else verticalLineSegments1[-1]['end']
      lineSegment = buildLineSegment(direction, distance, startPoint)
      horizontalLineSegments1.append(lineSegment)
  for move in wire2.split(','):
    direction = move[:1]
    distance = int(move[1:])
    if direction == 'U' or direction == 'D':
      startPoint = {'x': 0, 'y': 0} if len(horizontalLineSegments2) == 0 else horizontalLineSegments2[-1]['end']
      lineSegment = buildLineSegment(direction, distance, startPoint)
      verticalLineSegments2.append(lineSegment)
    if direction == 'L' or direction == 'R':
      startPoint = {'x': 0, 'y': 0} if len(verticalLineSegments2) == 0 else verticalLineSegments2[-1]['end']
      lineSegment = buildLineSegment(direction, distance, startPoint)
      horizontalLineSegments2.append(lineSegment)

buildLineSegments()

def findSmallestDistance():
  smallestManhattanDistance = None
  for verticalLineSegment in verticalLineSegments1:
    for horizontalLineSegment in horizontalLineSegments2:
      # Check: horizontal y is between the start and end y values of the vertical line
      if not(
        (horizontalLineSegment['start']['y'] >= verticalLineSegment['start']['y'] and horizontalLineSegment['start']['y'] <= verticalLineSegment['end']['y']) or
        (horizontalLineSegment['start']['y'] >= verticalLineSegment['end']['y'] and horizontalLineSegment['start']['y'] <= verticalLineSegment['start']['y'])
      ):
        continue
      # Check: vertical x is between the start and end x values of the horizontal line
      if not(
        (verticalLineSegment['start']['x'] >= horizontalLineSegment['start']['x'] and verticalLineSegment['start']['x'] <= horizontalLineSegment['end']['x']) or
        (verticalLineSegment['start']['x'] >= horizontalLineSegment['end']['x'] and verticalLineSegment['start']['x'] <= horizontalLineSegment['start']['x'])
      ):
        continue
      # Calculate: Manhattan distance from (0, 0) -> (vertical x, horizontal y)
      distance = manhattanDistance({'x': 0, 'y': 0}, {'x': verticalLineSegment['start']['x'], 'y': horizontalLineSegment['start']['y']})
      if (smallestManhattanDistance is None or distance < smallestManhattanDistance) and distance > 0:
        smallestManhattanDistance = distance
      

  for verticalLineSegment in verticalLineSegments2:
    for horizontalLineSegment in horizontalLineSegments1:
      # Check: horizontal y is between the start and end y values of the vertical line
      if not(
        (horizontalLineSegment['start']['y'] >= verticalLineSegment['start']['y'] and horizontalLineSegment['start']['y'] <= verticalLineSegment['end']['y']) or
        (horizontalLineSegment['start']['y'] >= verticalLineSegment['end']['y'] and horizontalLineSegment['start']['y'] <= verticalLineSegment['start']['y'])
      ):
        continue
      # Check: vertical x is between the start and end x values of the horizontal line
      if not(
        (verticalLineSegment['start']['x'] >= horizontalLineSegment['start']['x'] and verticalLineSegment['start']['x'] <= horizontalLineSegment['end']['x']) or
        (verticalLineSegment['start']['x'] >= horizontalLineSegment['end']['x'] and verticalLineSegment['start']['x'] <= horizontalLineSegment['start']['x'])
      ):
        continue
      # Calculate: Manhattan distance from (0, 0) -> (vertical x, horizontal y)
      distance = manhattanDistance({'x': 0, 'y': 0}, {'x': verticalLineSegment['start']['x'], 'y': horizontalLineSegment['start']['y']})
      if (smallestManhattanDistance is None or distance < smallestManhattanDistance) and distance > 0:
        smallestManhattanDistance = distance

  return smallestManhattanDistance

print(findSmallestDistance())
