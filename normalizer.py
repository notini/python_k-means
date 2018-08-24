class normalizer():

	"""@Params: data = vector of values to be normalized
				newMin and newMax = desired min and max normalization values"""
	def normalize_data(self, data, newMin, newMax):
		normalized_data = []
		minX, minY, maxX, maxY = self.getMinMax(data)
		for value in data:
			normalized_data.append([((newMax-newMin)/(maxX-minX))*(value[0]-maxX)+newMax, ((newMax-newMin)/(maxY-minY))*(value[1]-maxY)+newMax])
		return normalized_data
		
	def getMinMax(self, data):
		minX = data[0][0]
		minY = data[0][1]
		maxX = data[0][0]
		maxY = data[0][1]
		for value in data:
			if value[0] < minX:
				minX = value[0]
			if value[0] > maxX:
				maxX = value[0]
			if value[1] < minY:
				minY = value[1]
			if value[1] > maxY:
				maxY = value[1]
		return minX, minY, maxX, maxY
		