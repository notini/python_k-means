import random

class dataGenerator():
	
	def generateCartesianPoints(self, valueRange, numberOfPoints):
		values = [[round(random.uniform(valueRange[0], valueRange[1]),2), round(random.uniform(valueRange[0], valueRange[1]),2)] for i in range(numberOfPoints)]
		return values
		