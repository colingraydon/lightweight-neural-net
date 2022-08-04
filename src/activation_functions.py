import math
class activation_functions:

    def sigmoid(z):

        return 1 / (1 + math.exp(-z))

    def tanh_function(z):
    
        return math.tanh(z)

    def relu(z):

        if (z > 0):
            result = z
        else:
            result = 0
        return result

    def leaky_relu(z):
        #Alpha coefficient is .1, anything else would make this a random relu function
        a = .1
        if (z > 0):
            result = z
        else:
            result = a * z


    
