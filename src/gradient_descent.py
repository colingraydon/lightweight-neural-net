from activation_layer import activation_layer
class gradient_descent:

    def __init__(self, learning_rate):

        self.learning_rate = learning_rate

    def propagate_back(self, l:activation_layer, input):

        l.propagate_backward(input, self.learning_rate)