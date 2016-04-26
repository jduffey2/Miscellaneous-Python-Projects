import random
import array
class Neuron(object):
	"""docstring for Neuron"""
	def __init__(self,inputs):
		super(Neuron, self).__init__()
		self.weights = []
		self.learn = 0.3
		for x in range(1,inputs + 1):
			self.weights.append(random.random())

	def load(self,file):
		f = open(file,'r')
		temp = f.read()
		wght = [float(x) for x in temp.split(",")]
		self.weights = wght

	def activate(self, sum):
		if sum > 1:
			return 1
		return 0

	def run(self, inputs):
		total = 0
		for i in range(len(self.weights)):
			total += inputs[i] * self.weights[i]
		return self.activate(total)

	def train(self, inputs, desired):
		guess = self.run(inputs)
		error = desired - guess
		for i in range(len(self.weights)):
			self.weights[i] += self.learn * error * inputs[i]