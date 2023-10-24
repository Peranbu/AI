import numpy as np



# Define the sigmoid activation function

def sigmoid(x):

    return 1 / (1 + np.exp(-x))



# Define the derivative of the sigmoid function

def sigmoid_derivative(x):

    return x * (1 - x)



# Define the feedforward neural network class

class NeuralNetwork:

    def __init__(self, input_size, hidden_size, output_size):

        # Initialize weights with random values

        self.input_size = input_size

        self.hidden_size = hidden_size

        self.output_size = output_size

        self.weights_input_hidden = np.random.uniform(size=(input_size, hidden_size))

        self.weights_hidden_output = np.random.uniform(size=(hidden_size, output_size))



    def feedforward(self, X):

        # Forward pass through the network

        self.hidden_layer_input = np.dot(X, self.weights_input_hidden)

        self.hidden_layer_output = sigmoid(self.hidden_layer_input)

        self.output_layer_input = np.dot(self.hidden_layer_output, self.weights_hidden_output)

        self.output_layer_output = sigmoid(self.output_layer_input)

        return self.output_layer_output



    def train(self, X, y, learning_rate):

        # Backpropagation

        output_error = y - self.feedforward(X)

        output_delta = output_error * sigmoid_derivative(self.output_layer_output)



        hidden_layer_error = output_delta.dot(self.weights_hidden_output.T)

        hidden_layer_delta = hidden_layer_error * sigmoid_derivative(self.hidden_layer_output)



        # Update the weights

        self.weights_hidden_output += self.hidden_layer_output.T.dot(output_delta) * learning_rate

        self.weights_input_hidden += X.T.dot(hidden_layer_delta) * learning_rate



# Example usage

if __name__ == "__main__":

    # Define the input, hidden, and output layer sizes

    input_size = 2

    hidden_size = 4

    output_size = 1



    # Create a neural network

    neural_network = NeuralNetwork(input_size, hidden_size, output_size)



    # Training data (XOR problem)

    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

    y = np.array([[0], [1], [1], [0]])



    # Training loop

    epochs = 10000

    learning_rate = 0.1



    for epoch in range(epochs):

        neural_network.train(X, y, learning_rate)



    # Testing the trained network

    for i in range(len(X)):

        output = neural_network.feedforward(X[i])

        print(f"Input: {X[i]} Output: {output}")

