from layer import layer
from tensor import tensor
from activation_functions import activation_functions
from activation_functions_prime import activation_functions_prime
from network import network
from file_parser import file_parser
from activation_layer import activation_layer
from output_layer import output_layer

class test_class:

    if __name__ == "__main__":

        test_tensor = tensor(2,2)
        layer1 = activation_layer(100, 10, activation_functions.sigmoid, activation_functions_prime.sigmoid_prime, input_tensor=test_tensor)
        layer2 = output_layer(10, 5, activation_functions.sigmoid, activation_functions_prime.sigmoid_prime, input_tensor=test_tensor)
        


        neural_network = network()




        neural_network.add_layer(layer1)
        neural_network.add_layer(layer2)
        tensor.print_tensor(layer2.input_tensor)