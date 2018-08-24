import matplotlib.pyplot as plt
import random
import copy

from dataGenerator import dataGenerator
from normalizer import normalizer
from scipy.spatial import distance

class k_means():

	def clusterize(self, data, amountOfClusters):
		clusters = {} #'keys are cluster IDs. Each ID contains indexes to the 'data' vector, corresponding to the values attributed to the cluster.
		#arbitrarily choose cluster centers
		centers = []
		idxs = list(range(len(data)))
		iterationCounter = 1
		random.shuffle(idxs)
		for i in range(amountOfClusters):
			clusters[i] = []
			centers.append(data[idxs.pop()])
		#while moves are being made, move coordinates around to nearest cluster and recalculate centers.
		moveMade = True
		while moveMade:
			moveMade = False
			if iterationCounter > 1:
				#first centers are randomly selected
				centers = self.calculateCenters(clusters, data)
			auxClusters = copy.deepcopy(clusters)
			self.clearClusters(clusters)
			clusters = self.rearrange(centers, data, clusters)
			modified = self.dict_compare(clusters, auxClusters)
			#if len(modified) > 0, a move was made since last iteration
			if len(modified) > 0:
				moveMade = True
			iterationCounter = iterationCounter + 1
		return clusters
		
	#Rearranges (or not) selected cluster for each value based on distance to clusters center.
	def rearrange(self, centers, data, clusters):
		for idx in range(len(data)):
			best = distance.euclidean(data[idx], centers[0]); bestIdx = 0
			for i in range(len(centers)):	
				d = distance.euclidean(data[idx], centers[i])
				if d < best:
					best = d; bestIdx = i
			clusters[bestIdx].append(idx)
		return clusters
		
	#Calculates the center of each cluster.
	def calculateCenters(self, clusters, data):
		centers = []
		for key, values in clusters.items():
			x = 0; y = 0
			for value in values:
				x = x + data[value][0]; y = y + data[value][1]
			centers.append([x/len(values),y/len(values)])
		return centers

	#Checks if dictionaries are equal. Used to check if a move was made on last iteration of the algorithm.
	def dict_compare(self, d1, d2):
		d1_keys = set(d1.keys())
		d2_keys = set(d2.keys())
		intersect_keys = d1_keys.intersection(d2_keys)
		modified = {o : (d1[o], d2[o]) for o in intersect_keys if d1[o] != d2[o]}
		return modified
		
	#Empties clusters.
	def clearClusters(self, clusters):
		for key, value in clusters.items():
			clusters[key] = []
		
	#Plots data values.
	def plotPoints(self, data):
		for coords in data:
			plt.scatter(coords[0], coords[1])
		plt.show()
		
	#Plots each cluster with a different color.
	def plotCluster(self, clusters, data):
		colors = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 'brown', 'orange', 'silver']
		for key, cluster in clusters.items():
			for value in cluster:
				plt.scatter(data[value][0], data[value][1], color=[colors[key]])
		plt.show()