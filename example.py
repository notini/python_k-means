from kMeans import k_means
from normalizer import normalizer
from dataGenerator import dataGenerator

dGen = dataGenerator()
norm = normalizer()

#positions on the data and normalized_data vectors refer to the same values (unnormalized and normalized).
#this is designed to allow us to trace back to the original values.
data = dGen.generateCartesianPoints([0,10000], 500)
normalized_data = norm.normalize_data(data, 0, 100)

#Object declaration.
kMeans = k_means()
#Call to the clusterizer method.
clusters = kMeans.clusterize(normalized_data, 5)

#Plotting clusters
kMeans.plotCluster(clusters, data)