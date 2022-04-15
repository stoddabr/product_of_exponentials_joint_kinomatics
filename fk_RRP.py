import numpy as np
from Joint import Joint


if __name__ == "__main__":
    m = np.array([
        [-1, 0, 0, 0],
        [0, 0, 1, 3],
        [0, 1, 0, 2],
        [0, 0, 0, 1]
    ])

    js1 = Joint(w=np.array([0,0,1]),
        v=np.array([0,0,0]))
    js2 = Joint(w=np.array([1,0,0]),
        v=np.array([0,2,0]))
    js3 = Joint(w=np.array([0,0,0]),
        v=np.array([0,1,0]))

    jb1 = Joint(w=np.array([0,1,0]),
        v=np.array([3,0,0]))
    jb2 = Joint(w=np.array([-1,0,0]),
        v=np.array([0,3,0]))
    jb3 = Joint(w=np.array([0,0,0]),
        v=np.array([0,0,1]))


    theta = [np.pi/2, np.pi/2, 1]

    ts = np.dot(js1.expc(theta[0]), np.dot(js2.expc(theta[1]), np.dot(js3.expc(theta[2]), m )))
    tb = np.dot(m, np.dot(jb1.expc(theta[0]), np.dot(jb2.expc(theta[1]), jb3.expc(theta[2]) )))

    print(ts)
    print(tb)