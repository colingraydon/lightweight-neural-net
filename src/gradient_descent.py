from activation_layer import activation_layer
from optimizer import optimizer
from layer import layer
from activation_layer import activation_layer
from output_layer import output_layer
class gradient_descent(optimizer):

    def __init__(self, learning_rate):

        self.learning_rate = learning_rate

    def propagate_back(self, l, test, epoch_number):

        l.propagate_backward(test, self.learning_rate)