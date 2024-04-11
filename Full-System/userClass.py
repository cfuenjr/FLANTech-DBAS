import numpy as np
import copy


class Entry:
    def __init__(self):
        self.gait90 = np.array([])
        self.gait45 = np.array([])
        self.fingerprint = np.array([])

    def deep_copy(self):
        return copy.deepcopy(self)
