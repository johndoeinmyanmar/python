import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def plotVectors(vecs, cols, alpha=1):

    plt.axvline(x=0, color='#a9a9a9', zorder=0)
    plt.axhline(y=0, color='#a9a9a9', zorder=0)

    for i in range(len(vecs)):
        if (isinstance(alpha, list)):
            alpha_i = alpha[i]
        else:
            alpha_i = alpha

        x = np.concatenate([[0,0], vecs[i]])
        plt.quiver([x[0]],
                   [x[1]],
                   [x[2]],
                   [x[3]],
                   angles='xy', scale_units='xy', scale=1, color=cols[i],
                   alpha=alpha_i)

        

points = np.array([[1,3],[2,2],[3,1],[4,7],[5,4]])

C = np.array([[-1,0],[0,1]])
np.linalg.det(C)

newPoints = points.dot(C)

plt.figure()
plt.plot(points[:,0],points[:,1])
plt.plot(newPoints[:,0], newPoints[:,1])
plt.show()
