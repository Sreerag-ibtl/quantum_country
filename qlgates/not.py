import numpy as np

class Not:

    """
    A class that implement quantum NOT gate.
    """

    def __init__(self):

        """
        Constructor.
        """
        
        self.X = np.array((0, 1), (1, 0))

    def apply_on(self, state):

        """
        Apply NOT operation on quantum state,
        state.
        """

        return np.dot(self.X, state)
