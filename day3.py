# input = '''R75,D30,R83,U83,L12,D49,R71,U7,L72
# U62,R66,U55,R34,D71,R55,D58,R83'''
input = '''R1006,D541,R261,U378,L530,U165,L175,U143,R162,D504,R985,U33,R544,D168,L498,D549,R88,D243,L36,U944,R261,D91,L957,D579,L224,D732,R312,U378,R82,D200,L510,U747,R588,U667,L495,D147,L100,U482,R896,D711,L513,U44,L685,U547,L132,D23,R139,U786,L908,U912,R531,U564,L970,D562,R422,U919,R108,D275,R431,U697,L85,D762,L25,D633,R878,U566,L550,D288,L29,D788,R930,U619,L612,U228,R25,D133,R219,U367,L889,U735,L994,U513,R34,D429,L750,U83,R204,U68,R769,D833,L545,D621,L747,U714,R655,U112,L629,D353,L450,D588,R775,U493,L252,D486,L405,D350,R970,D73,L750,D731,L962,D242,R947,D348,L252,D392,L94,U970,R616,U505,L782,D375,R849,U971,R57,D25,R68,U174,L670,U735,R66,D994,R868,U285,L866,U433,L169,D575,L374,U169,R180,D251,R671,D703,R708,D60,L251,D164,L106,U974,R670,U760,L235,U377,R318,U294,L421,D904,L571,U157,R428,D416,L237,D850,L827,U702,L134,D67,R327,U976,L307,D454,L646,U919,L92,D523,R828,D544,L557,D142,L671,D862,R118,U244,L667,U356,L554,U969,R348,D895,L735,D948,R920,U470,R819,D256,R169,D410,R977,U487,L64,U466,L574,U891,R29,D767,L224,D922,L782,U433,L478,U582,L603,U339,L658,U188,L95,U766,R958,U313,L881,D869,L633,U551,R270,U444,R399,D698,L923,U213,R245,D486,R34,U514,R450,U739,R102,U181,L826,D839,L948,D11,R51,U146,R415,U683,R352,U387,R158,D88,L576,U600,R955,D22,R884,D772,L576,D74,L937,U832,R198,D721,R393,U847,R828,U975,L452,U796,R950,U568,R117,U114,L983,U514,R564,U569,L141,D464,R463,U635,L772,U634,R614,D160,R388,D550,L933,D832,R94,D855,L18,U241,L805,U517,R384,D464,L271,U788,R718,U495,R103
L1000,D65,L329,D227,R798,U36,R263,D232,R771,D768,R223,D898,L637,U402,L867,U694,R362,U199,L769,U956,L180,U123,L495,U660,L861,D652,R222,D166,R47,D766,R709,U859,L639,U841,L407,D392,R503,D596,R614,D448,L340,D562,L913,U942,L426,D84,R385,U202,R676,U379,L231,D124,L568,D134,L271,D777,R765,U979,R678,D478,R307,D568,L318,D705,R787,U322,R233,D423,L617,U955,R32,U989,R356,U922,R444,U443,R136,U140,L298,U348,L121,U332,R285,D302,L844,D234,L468,U395,R20,D245,L583,U173,L928,U598,L383,D188,L945,D382,L929,D181,L650,U394,L938,U805,L680,U676,R136,U925,L899,U990,R661,D621,R612,D587,R609,U560,R650,D416,L285,D152,R906,U47,L721,D206,L602,U258,R667,U443,L291,D375,L977,D148,R394,U758,L43,D953,R143,D60,R851,D887,R718,D505,R407,D321,R140,D675,L42,U235,L626,D673,L271,D398,L190,U30,L225,D612,R896,U757,L340,D280,L742,U188,L372,D7,R677,U248,R694,U581,L220,U372,R497,U89,R952,D221,L71,D962,L992,U420,R741,U96,R625,U794,L602,U229,R635,D585,R119,U501,R640,D283,L963,U385,L967,D503,L453,D578,L465,D318,L968,U979,L650,D894,L210,U855,R298,D66,R378,D223,L475,D950,L417,D276,L494,D690,R516,D352,L603,U211,R171,U553,L437,U865,L378,D223,R814,D779,L780,D738,R920,D462,L230,U574,L880,D252,R710,D476,L184,U635,R453,U115,R96,U169,R995,D523,R562,D480,L791,U865,R568,D149,L539,U610,R107,D604,R95,D982,R360,U141,L567,D555,R481,U716,R753,D576,R54,D343,R663,U676,R907,D202,R230,U827,L583,U937,R818,D579,R502,D713,R61,U402,L527,D955,R117,U214,R580,U636,R721,U55,L899,U667,R595,U790,L384,U416,L375,D1,L653,U611,L187,D256,L931'''
output = None

def manhattanDistance(point1, point2):
  return abs(point1['x'] - point2['x']) + abs(point1['y'] - point2['y'])

# "Point" = Dictionary
# a = {
#   'x': 4,
#   'y': 5,
#   'totalDistance': 0,
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
#   'totalDistance': 0,
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
#   'totalDistance': 0,
# }, {
#   'start': {
#     'x': 25,
#     'y': 0
#   },
#   'end': {
#     'x': 25,
#     'y': 30
#   },
#   'totalDistance': 0,
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

intersectionPoints = []

def buildLineSegment(direction, distance, startPoint):
  result = { 'start': startPoint, 'end': None }
  totalDistance = startPoint['totalDistance'] + distance
  match direction:
    case 'U':
      result['end'] = { 'x': startPoint['x'], 'y': startPoint['y'] + distance, 'totalDistance': totalDistance }
    case 'D':
      result['end'] = { 'x': startPoint['x'], 'y': startPoint['y'] - distance, 'totalDistance': totalDistance }
    case 'L':
      result['end'] = { 'x': startPoint['x'] - distance, 'y': startPoint['y'], 'totalDistance': totalDistance }
    case _:
      result['end'] = { 'x': startPoint['x'] + distance, 'y': startPoint['y'], 'totalDistance': totalDistance }
  return result

def buildLineSegments():
  wire1, wire2 = input.split('\n')
  for move in wire1.split(','):
    direction = move[:1]
    distance = int(move[1:])
    if direction == 'U' or direction == 'D':
      startPoint = {'x': 0, 'y': 0, 'totalDistance': 0} if len(horizontalLineSegments1) == 0 else horizontalLineSegments1[-1]['end']
      lineSegment = buildLineSegment(direction, distance, startPoint)
      verticalLineSegments1.append(lineSegment)
    if direction == 'L' or direction == 'R':
      startPoint = {'x': 0, 'y': 0, 'totalDistance': 0} if len(verticalLineSegments1) == 0 else verticalLineSegments1[-1]['end']
      lineSegment = buildLineSegment(direction, distance, startPoint)
      horizontalLineSegments1.append(lineSegment)
  for move in wire2.split(','):
    direction = move[:1]
    distance = int(move[1:])
    if direction == 'U' or direction == 'D':
      startPoint = {'x': 0, 'y': 0, 'totalDistance': 0} if len(horizontalLineSegments2) == 0 else horizontalLineSegments2[-1]['end']
      lineSegment = buildLineSegment(direction, distance, startPoint)
      verticalLineSegments2.append(lineSegment)
    if direction == 'L' or direction == 'R':
      startPoint = {'x': 0, 'y': 0, 'totalDistance': 0} if len(verticalLineSegments2) == 0 else verticalLineSegments2[-1]['end']
      lineSegment = buildLineSegment(direction, distance, startPoint)
      horizontalLineSegments2.append(lineSegment)

buildLineSegments()

def findSmallestDistance():
  smallestTotalDistance = None
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
      # Calculate: Manhattan distance from vertical start point -> horizontal start point
      distance = horizontalLineSegment['start']['totalDistance'] + verticalLineSegment['start']['totalDistance'] + manhattanDistance(verticalLineSegment['start'], horizontalLineSegment['start'])
      if (smallestTotalDistance is None or distance < smallestTotalDistance) and distance > 0:
        smallestTotalDistance = distance
      

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
      # Calculate: Manhattan distance from vertical start point -> horizontal start point
      distance = horizontalLineSegment['start']['totalDistance'] + verticalLineSegment['start']['totalDistance'] + manhattanDistance(verticalLineSegment['start'], horizontalLineSegment['start'])
      if (smallestTotalDistance is None or distance < smallestTotalDistance) and distance > 0:
        smallestTotalDistance = distance

  return smallestTotalDistance

print(findSmallestDistance())
