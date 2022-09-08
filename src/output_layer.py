from activation_layer import activation_layer
from tensor import tensor

import math
import layer

class output_layer(activation_layer):

    def __init__(self, input_dimensions, output_dimensions, activation_function, activation_function_prime, weights=None, bias=None, input_tensor=None, output_tensor=None, dz=None):
        # super().__init__
        self.input_dimensions = input_dimensions
        self.output_dimensions = output_dimensions
        self.activation_function = activation_function
        self.activation_function_prime = activation_function_prime
        self.input_tensor = input_tensor
        self.weights = tensor(output_dimensions, input_dimensions)
        self.bias = tensor(output_dimensions, columns=1)
        self.set_weights()
        self.set_bias()

    #overrode method as there is no next layer in which to feed_input
    def propagate_forward(self):

        self.output_tensor = tensor.compute_dot_product(self.weights, self.input_tensor)
        temp_tensor = tensor(self.output_tensor.rows, self.output_tensor.columns)
        temp_tensor.t = []
        i = 0
        while (i < temp_tensor.rows * temp_tensor.columns):
            temp_tensor.t.append(self.activation_function(self.output_tensor.t[i]))
            i += 1


    def propagate_backward(self, test, learning_rate):

        print(test.rows)
        print("test.rows is above, printed from propagate backward")
        print(test.columns)
        print("test.weights.columns, printed from propagate backward")
        print(self.output_tensor.rows)
        print("output tensor rows is above, printed from propagate backward")
        print(self.output_tensor.columns)
        print("output tensor columns, printed from propagate backward")
        self.dz = tensor.tensor_subtraction(self.output_tensor, test)
        self.update_weights(learning_rate)

    #overrode the method as there is no next layer
    def calculate_dz(self, test):

        self.dz = tensor.tensor_subtraction(self.output_tensor, test)

    #overrode because dt will have a different value
    def propagate_backward_adam(self, learning_rate, epoch_number, test):

        dt = self.get_weights()
        self.vdw = tensor.tensor_addition(tensor.tensor_scalar_multiplication(self.vdw, self.beta1), tensor.tensor_scalar_multiplication(dt, (1 - self.beta1)))
        self.sdw = tensor.tensor_addition(tensor.tensor_scalar_multiplication(self._sdw, self.beta2), tensor.tensor_scalar_multiplication(tensor.tensor_multiplication(dt, dt), (1-self.beta2)))
        new_vdw = tensor.tensor_scalar_multiplication(self._vdw, (1 / (1-math.exp(self.beta1, epoch_number))))
        new_sdw = tensor.tensor_scalar_multiplication(self._sdw, (1 / (1-math.exp(self.beta2, epoch_number))))
        temp_tensor = tensor(new_sdw.get_rows(), new_sdw.get_columns())
        new_tensor = tensor.tensor_division(new_vdw, tensor.tensor_subtraction(tensor.tensor_square_root(new_sdw), tensor.tensor_scalar_multiplication(temp_tensor, self.epsilon)))
        self.weights = tensor.tensor_subtraction(self.weights, tensor.tensor_scalar_multiplication(new_tensor, learning_rate))

