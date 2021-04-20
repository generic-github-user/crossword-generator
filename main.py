import numpy as np

class Crossword:
    def __init__(self):
        self.words = []
        """A list of words/phrases used to generate the crossword"""
        self.grid = np.array(dtype=str)
