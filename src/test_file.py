from layer import layer
from tensor import tensor
from activation_functions import activation_functions
from network import network
from file_parser import file_parser
from activation_layer import activation_layer
from output_layer import output_layer

class test_class:

    if __name__ == "__main__":

        layer1 = layer(100, 10, activation_functions.sigmoid)
        layer2 = layer(10, 5, activation_functions.sigmoid)
        


        neural_network = network()




        #neural_network.add_layer(layer1)
        #neural_network.add_layer(output_layer(output_layer_input_dimension, output_layer_output_dimension, activation_functions.sigmoid()))
