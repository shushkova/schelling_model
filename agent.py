import math
import random

class Agent:
    def __init__(self, type, n):
        self.ag_type = type
        self.location = random.randint(1, n), random.randint(1, n)
        self.satisf = None

    def get_location(self):
        return self.location

    def get_type(self):
        return self.ag_type

    def get_distance(self, agent):
        return (math.pow((self.location[0] - agent.location[0]), 2) + math.pow((self.location[1] - agent.location[1]),
                                                                               2))

    """  def satisfaction(self, agents):
      cnt = 0
      for agent in agents:
        if self.get_distance(agent) < 2:
          if self.type == agent.type:
            cnt += 1
      return cnt / 8"""

    def satisfaction(self, agent):
        if self.ag_type == agent.get_type():
            return 1
        return 0

    def change_satisf(self, status):
        self.satisf = status

    def change_location(self, n):
        self.location = random.randint(1, n), random.randint(1, n)

    def generate_location(self, n):
        return random.randint(1, n), random.randint(1, n)

    def set_location(self, x, y):
        self.location = x, y