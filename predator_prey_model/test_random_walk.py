"""
Testing the RandomWalker by having an ABM composed only of random walker
agents.
"""

from mesa import Model
from mesa.space import MultiGrid
from mesa.time import RandomActivation
from mesa.visualization.TextVisualization import TextVisualization, TextGrid

from wolf_sheep.random_walk import RandomWalker


class WalkerAgent(RandomWalker):
    """
    Agent which only walks around.
    """

    def step(self):
        self.random_move()


class WalkerWorld(Model):
    """
    Random walker world.
    """

    height = 10
    width = 10

    def __init__(self, height, width, agent_count):
        """
        Create a new WalkerWorld.
        Args:
            height, width: World size.
            agent_count: How many agents to create.
        """
        self.height = height
        self.width = width
        self.grid = MultiGrid(self.height, self.width, torus=True)
        self.agent_count = agent_count

        self.schedule = RandomActivation(self)
        # Create agents
        for i in range(self.agent_count):
            x = self.random.randrange(self.width)
            y = self.random.randrange(self.height)
            a = WalkerAgent(i, (x, y), self, True)
            self.schedule.add(a)
            self.grid.place_agent(a, (x, y))

    def step(self):
        self.schedule.step()

