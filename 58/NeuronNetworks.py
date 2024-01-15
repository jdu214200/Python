from numpy import exp, array, random, dot

training_set_inputs = array([[0, 0, 1],
                             [1, 1, 1],
                             [1, 0, 1],
                             [0, 1, 1]])
training_set_outputs = array([[0, 1, 1, 0]]).T

class NeuralNetwork():
    def __init__(self):
        random.seed(1)
        self.synaptic_weights = 2 * random.random((3, 1)) - 1

    def __sigmoid(self, x):
        return 1 / (1 + exp(-x))

    def __sigmoid_derivative(self, x):
        return x * (1 - x)

    def train(self, training_set_inputs, training_set_outputs, number_of_training_iterations):
        for iteration in range(number_of_training_iterations):
            output = self.think(training_set_inputs)
            error = training_set_outputs - output
            adjustment = dot(training_set_inputs.T, error * self.__sigmoid_derivative(output))
            self.synaptic_weights += adjustment

    def think(self, inputs):
        return self.__sigmoid(dot(inputs, self.synaptic_weights))

neural_network = NeuralNetwork()
print("Vaznlar generatsiyalangan qiymatlar:")
print(neural_network.synaptic_weights)

neural_network.train(training_set_inputs, training_set_outputs, number_of_training_iterations=10000)
print("O'qitishdan keyin vaznlarning yangi qiymatlar:")
print(neural_network.synaptic_weights)

print("Yangi namunaning chiqish qiymatini aniqlash [1, 0, 0] -> ?:")
print(neural_network.think(array([1, 0, 0])))
