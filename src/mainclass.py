import parser
import activation_layer
import activation_functions
import output_layer
import adam_optimizer
import gradient_descent
import layer
import network
import optimizer
import tensor
import math


class mainclass:

    if __name__ == "__main__":

        neural_network = network()
        file_path = "Users/colingraydon/Downloads/mnist_test.csv"
        p = parser()

        #mnist_test.csv has 785 columns, numbers were not chosen arbitrarily
        first_column = 1
        last_column = 785
        test_column = 0
        activation_layer_input_dimension = 784
        activation_layer_output_dimension = 512
        output_layer_input_dimension = 512
        output_layer_output_dimension = 10

        mnist_input = p.parse(file_path, first_column, last_column)
        mnist_test = p.parse(file_path, test_column)
        mnist_test = p.one_hot_mnist(mnist_test)




        neural_network.add_layer(activation_layer(activation_layer_input_dimension, activation_layer_output_dimension, activation_functions.sigmoid()))
        neural_network.add_layer(output_layer(output_layer_input_dimension, output_layer_output_dimension, activation_functions.sigmoid()))

        input_tensor = tensor(10, 784, mnist_input)
        input_tensor = tensor.tensor_scalar_multiplication(.004, input)
        test = tensor(10, 10, mnist_test)

        transposed_input = tensor.transpose(input_tensor)
        transposed_test = tensor.transpose(test)

        training_iterations = 100
        learning_rate = .003
        neural_network.run_train(training_iterations, transposed_input, transposed_test, gradient_descent(learning_rate))

