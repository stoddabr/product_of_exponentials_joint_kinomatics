import numpy as np
from Joint import Joint

if __name__ == "__main__":
    l0 = l1 = l2 = 1
    theta = np.array([0.0, np.pi/2, -np.pi/2, 1.0])

    m = np.array([
        [1.0, 0, 0, 0],
        [0, 1, 0, l1+l2],
        [0, 0, 1, l0],
        [0, 0, 0, 1]
    ])

    # joints in {s}
    js1 = Joint(w=np.array([0,0,1]),
        v=np.array([0,0,0]))
    js2 = Joint(w=np.array([0,0,1]),
        v=np.array([l1,0,0]))
    js3 = Joint(w=np.array([0,0,1]),
        v=np.array([l1+l2,0,0]))
    js4 = Joint(w=np.array([0,0,0]),
        v=np.array([0,0,1]))

    # joints in {b}
    jb1 = Joint(w=np.array([0,0,1]),
        v=np.array([-l1-l2,0,0]))
    jb2 = Joint(w=np.array([0,0,1]),
        v=np.array([-l2,0,0]))
    jb3 = Joint(w=np.array([0,0,1]),
        v=np.array([0,0,0]))
    jb4 = Joint(w=np.array([0,0,0]),
        v=np.array([0,0,1]))

    # evaluate 
    ts = np.dot(js1.expc(theta[0]), np.dot(js2.expc(theta[1]), np.dot(js3.expc(theta[2]), np.dot(js4.expc(theta[3]), m ))))
    tb = np.dot(m, np.dot( jb1.expc(theta[0]), np.dot( jb2.expc(theta[1]), np.dot( jb3.expc(theta[2]), jb4.expc(theta[3]) ))))

    print(ts)
    print(tb)
