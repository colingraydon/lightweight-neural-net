import math

class activation_functions_prime:

    def sigmoid_prime(z):

        result = (1 / (1 + math.exp(-z))) * (1 - (1 / (1 + math.exp(-z))))
        return result

    def tanh_prime(z):

        return (1 - math.tanh(z) ** 2)

    def relu_prime(z):

        if (z > 0):
            result = 1
        else:
            result = 0
        return result

    def leaky_relu_prime(z):
        #this is the alpha coefficient required to make a leaky relu function
        a = .1
        if (z > 0):
            result = 1
        else:
            result = a
        return result
    