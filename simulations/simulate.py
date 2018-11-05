import os
import matplotlib.pyplot as plt
import matplotlib.patches as mp
import numpy as np
from fastcluster import linkage_vector
from cluster_utils import extract
from validation import validation


'''
for sig in range(1, 4):
  res = []
  for rep in range(100):
    print(sig, rep)
    cur_res = []
    for i in range(50, 100):
    
      N = 50
      
      X, y = [], [] # initialise as empty
 
      
	  #cluster_sizes = [int(N * i/100), int(N*(1-i/100)), int(N*(1-i/100))] # set size of clusters
      
      s1 = int((i/100) *  N) # proportion of the data
      s2 = int(np.floor((N-s1)/2))
      s3 = int(np.ceil((N-s1)/2))
      cluster_sizes = [s1, s2, s3]
      
	  #print(np.sum(cluster_sizes))
      
      centres = [[0, 0, 0], [5, 5, 5], [10, 10, 10]]
      covar = [[sig, 0, 0], [0, sig, 0], [0, 0, sig]]

      for j, size in enumerate(cluster_sizes):

        X.append(np.random.multivariate_normal(mean = centres[j], cov = covar, size = size))
        y.append([j+1] * size)
      
      X = np.vstack(X)
      y = np.concatenate(y)
    
      l = linkage_vector(X, 'ward')
      e = extract(l, 1, 20)
      v = validation(X, e)
    
      cur_res.append(v)
    res.append(cur_res)
    
  res = np.array(res, 'int')
  np.savetxt('simulation_{}.csv'.format(sig), res, delimiter=',')
''' 
 
plt.style.use(os.path.join(os.curdir, "..", "single.mplstyle"))

#http://colorbrewer2.org/#type=sequential&scheme=BuGn&n=3

colors = ["#7fc97f", "#beaed4", "#fdc086"]
for sig in range(1, 4):
  res = np.genfromtxt('simulation_{}.csv'.format(sig), delimiter=',')
  plt.plot(np.arange(50, 100), np.sum(res==3, 0), linestyle = 'None', marker='o', color = colors[sig-1])
 
 
plt.xlabel("Proportion of data points in dominant cluster")
plt.ylabel("Proportion of repitions concluding 3 clusters")

handles = []
for i in range(3):
  handles.append(mp.Patch(color= colors[i], label = "${}\sigma$".format(i+1)))
plt.legend(handles = handles)

 
plt.savefig("sim.png", dpi = 600)
plt.show()

  
