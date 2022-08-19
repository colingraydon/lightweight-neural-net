import activation_layer
import tensor
import math
import layer

class output_layer(activation_layer):

    def __init__(self, rows, columns, activation_function, activation_function_prime):
        super().__init__(rows)
        super().__init__(columns)
        super().__init__(activation_function)
        super().__init__(activation_function_prime)
        self.set_weights()
        self.set_bias()

    #overrode method as there is no next layer in which to feed_input
    def propagate_forward(self):

        self._output_tensor = tensor.compute_dot_product(self._weights, self._input_tensor)
        for i in self._output_tensor:
            self._output_tensor.t[i] = self.activation_function(self._output_tensor.t[i])


    def propagate_backward(self, test, learning_rate):

        self._dz = tensor.tensor_subtraction(self._output_tensor, test)
        self.update_weights(learning_rate)

    #overrode the method as there is no next layer
    def calculate_dz(self, test):

        self._dz = tensor.tensor_subtraction(self._output_tensor, test)

    #overrode because dt will have a different value
    def propagate_backward_adam(self, learning_rate, epoch_number, test):

        dt = self.get_weights()
        self._vdw = tensor.tensor_addition(tensor.tensor_scalar_multiplication(self._vdw, self.beta1), tensor.tensor_scalar_multiplication(dt, (1 - self.beta1)))
        self._sdw = tensor.tensor_addition(tensor.tensor_scalar_multiplication(self._sdw, self.beta2), tensor.tensor_scalar_multiplication(tensor.tensor_multiplication(dt, dt), (1-self.beta2)))
        new_vdw = tensor.tensor_scalar_multiplication(self._vdw, (1 / (1-math.exp(self.beta1, epoch_number))))
        new_sdw = tensor.tensor_scalar_multiplication(self._sdw, (1 / (1-math.exp(self.beta2, epoch_number))))
        temp_tensor = tensor(new_sdw.get_rows(), new_sdw.get_columns())
        new_tensor = tensor.tensor_division(new_vdw, tensor.tensor_subtraction(tensor.tensor_square_root(new_sdw), tensor.tensor_scalar_multiplication(temp_tensor, self.epsilon)))
        self._weights = tensor.tensor_subtraction(self._weights, tensor.tensor_scalar_multiplication(new_tensor, learning_rate))

