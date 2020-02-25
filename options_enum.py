from enum import Enum

class OptionDecision(Enum):
  YES = 1
  NO = 2
  RANDOM = 3

class OptionAmount(Enum):
  RANDOM = -1 # 0-7
  NONE = 0
  ONE = 1
  TWO = 2
  THREE = 3
  FOUR = 4
  FIVE = 5
  SIX = 6
  SEVEN = 7

class OptionCondition(Enum):
  OR = 1
  AND = 2
  BOTH = 3

