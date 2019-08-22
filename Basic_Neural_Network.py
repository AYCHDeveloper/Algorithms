import numpy as np
class NeuralNetwork():
	def __init__(self):
		# seeding for random number generaion
		np.random.seed(5)

		#converting weights to a 3 by 1 matrix with values from -1 to 1 and mean 0
		self.synaptic_weights = 2*np.random.random((3,1)) -1

	def sigmoid(self, x):
		#applying the sigmoid function
		return 1 / (1+np.exp(-x))

	def sigmoid_derivatives(self,x):
		#computing derivative to the sigmoid function
		return x*(1-x)

	def train(self,training_inputs, training_outputs, training_iterations):
		#training the model to make accurate predictions while adjusting weights continously
		for iteration in range(training_iterations):
			#pass the training data through neuron
			output = self.think(training_inputs)

			#compute error rate for back-propagation
			error = training_outputs-output

			#performing the weight adjustments
			adjustments = np.dot(training_inputs.T, error*self.sigmoid_derivatives(output))

			self.synaptic_weights += adjustments

	def think(self, inputs):
		#passing the inputs via the neuron to get output
		#converting values to floats

		inputs = inputs.astype(float)
		output = self.sigmoid(np.dot(inputs, self.synaptic_weights))
		return output


if __name__ == "__main__":
	#initializing the neuron class
	neural_network = NeuralNetwork()

	print("Basic Implementation of NeuralNetwork without any Library")
	print("---------------------------------------------------------")
	print("This network is created for predicting the output of boolean values")
	print("Suppose The training samples given are as follows along with outputs:")
	print("Input1: Input2: Input3   == Output")
	print("0: 0: 1   == 0")
	print("1: 1: 1   == 1")
	print("1: 0: 1   == 1")
	print("0: 1: 1   == 0")
	print("Now from looking at above sample you know that 0,0,1 the input will be 1")
	print("But what if you encounter new sample like 1,1,1 == ?? what will be output ?")
	print("You can ask from trained neural network for prediction.")
	

	print("Beginning Randomly Generated Weights: ")
	print(neural_network.synaptic_weights)

	#training data consisting of 4 examples--3 input values and 1 output
	training_inputs = np.array([[0,0,1],
								[1,1,1],
								[1,0,1],
								[0,1,1]])

	training_outputs = np.array([[0,1,1,0]]).T

	#training_takes place here
	neural_network.train(training_inputs, training_outputs, 15000)
	print("Ending Weights Afer Training:")
	print(neural_network.synaptic_weights)

	print("Please Input 3 boolean values and neural network will predict the output")
	user_input_one = str(input("User Input One: "))
	user_input_two = str(input("User Input Two: "))
	user_input_three = str(input("User Input Three: "))

	print("Considering New Situation:  ", user_input_one, user_input_two, user_input_three)
	print("New Output data: ")
	output = neural_network.think(np.array([user_input_one,user_input_two,user_input_three]))
	if output > 0.5 :
		output=1
		print("The output is: ",output)
	else:
		output=0
		print("The output is:",output)	
	print("The end");