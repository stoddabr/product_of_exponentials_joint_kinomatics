import numpy as np
from scipy.linalg import expm, sinm, cosm
from typing import Optional

class Joint:
    def __init__(self, w:np.ndarray, v: np.ndarray):
        self.w = w
        self.v = v

    def expc(self, theta:np.number,
        w:Optional[np.ndarray] = False, 
        v:Optional[np.ndarray] = False):
        """ exponential coordinate at theta """
        if w is False:
            w = self.w
        if v is False:
            v = self.v

        s = self.skew_s(w,v)
        # return ExpCMat( expm( s * theta ) )
        return expm( s * theta )


    def skew_s(self, 
        w:Optional[np.ndarray] = False, 
        v:Optional[np.ndarray] = False):
        """ create skew symmetric matrix """
        if w is False:
            w = self.w
        if v is False:
            v = self.v

        # [S] = [
        #     [w] v
        #     0   0
        # ]
        skew_symmetric_screw = np.array([
            [0,     -w[2],  w[1],   v[0] ],
            [w[2],  0,      -w[0],  v[1] ],
            [-w[1], w[0],   0,      v[2] ],
            [0, 0, 0, 0],
        ])

        return skew_symmetric_screw


# class ExpCMat:
#     def __init__(self, m):
#         self.m = m

#     def __mul__ (self, other):
#         """ ie self * other """
#         return np.dot(self.m, other)
    
#     def __rmul__(self, other):
#         """ ie other * self """
#         return np.dot(other, self.m)