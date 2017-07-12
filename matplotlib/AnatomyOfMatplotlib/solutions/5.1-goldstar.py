import matplotlib.pyplot as plt
from matplotlib.collections import StarPolygonCollection

fig, ax = plt.subplots(1, 1)

offsets = zip([0.2, 0.4, 0.6, 0.8], [0.5] * 4)
collection = StarPolygonCollection(5,
                                   offsets=offsets,
                                   transOffset=ax.transData,
                                   facecolors=['gold'],
                                   sizes=[75])
ax.add_collection(collection)
plt.show()
