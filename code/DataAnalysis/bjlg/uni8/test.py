import numpy as np
from scipy import spatial
import pylab as pl
np.random.seed(42)
points2d = np.random.rand(10, 2)
ch2d = spatial.ConvexHull(points2d)
poly = pl.Polygon(points2d[ch2d.vertices], fill=None, lw=2, color='r', alpha=0.5)
ax = pl.subplot(aspect='equal')
pl.plot(points2d[:, 0], points2d[:, 1], 'go')
for i, pos in enumerate(points2d):
    pl.text(pos[0], pos[1], str(i), color='blue')
ax.add_artist(poly)
pl.show()