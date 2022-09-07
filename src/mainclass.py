from file_parser import file_parser
from activation_layer import activation_layer
from activation_functions import activation_functions
from activation_functions_prime import activation_functions_prime
from output_layer import output_layer
from adam_optimizer import adam_optimizer
from gradient_descent import gradient_descent
from layer import layer
from network import network
from tensor import tensor
import math


class mainclass:

    if __name__ == "__main__":

        neural_network = network()
        file_path = "/Users/colingraydon/Downloads/mnist_test.csv"
        
        p = file_parser()

        #mnist_test.csv has 785 columns, one of which is the "answer", numbers were not chosen arbitrarily
        first_column = 1
        last_column = 785

        test_column = 0
        activation_layer_input_dimension = 784
        activation_layer_output_dimension = 512
        output_layer_input_dimension = 512
        output_layer_output_dimension = 10

        mnist_input = p.parse_range(file_path, first_column, last_column)
        mnist_test = p.parse_column(file_path, test_column)
        

        mnist_test = p.one_hot_mnist(mnist_test)


        neural_network.add_layer(activation_layer(activation_layer_input_dimension, activation_layer_output_dimension, activation_functions.sigmoid, activation_functions_prime.sigmoid_prime))
        neural_network.add_layer(output_layer(output_layer_input_dimension, output_layer_output_dimension, activation_functions.sigmoid, activation_functions_prime.sigmoid_prime))

        input_tensor = tensor(512, 784, mnist_input)
        input_tensor = tensor.convert_to_float(input_tensor)
        input_tensor = tensor.tensor_scalar_multiplication(input_tensor, .004)
        test = tensor(10, 10, mnist_test)
        transposed_input = tensor.transpose(input_tensor)
        transposed_test = tensor.transpose(test)

        training_iterations = 10000
        learning_rate = .003

        neural_network.run_train(training_iterations, transposed_input, transposed_test, gradient_descent(learning_rate))

