import layer
import tensor
import numpy as np


class activation_layer(layer):

    _weights: tensor
    _bias: tensor
    _input_tensor:tensor
    _output_tensor: tensor
    _dz: tensor



    def __init__(self, rows, columns, activation_function, activation_function_prime):

        self.rows = rows
        self.columns = columns
        self.activation_function = activation_function
        self.activation_function_prine = activation_function_prime
        self._weights = self.set_weights()
        self._bias = self.set_bias()

    #3 is chosen here because that is the number of neurons
    def set_weights(self):

        _weights = tensor.randomize_new_tensor(_weights, -3, 3)

    def get_weights(self):

        return self._weights

    def set_bias(self):

        _bias = tensor.randomize_new_tensor(_bias, -3, 3)

    def get_bias(self):

        return self._bias

    #returns the dw tensor
    def get_dw(self):

        return tensor.compute_dot_product(self._dz, tensor.transpose(self._input_tensor))


    #Takes the dot product of the weights and the input tensor, runs it through the activation function
    #Sets the next layer with this tensor
    def propagate_forward(self):

        self._output_tensor = tensor.compute_dot_product(self._weights, self._input_tensor)
        temp_tensor = tensor(self.rows, self.columns)
        for i in temp_tensor:
            temp_tensor.t[i] = self.activation_function(self._output_tensor.t[i])
        self.feed_input(temp_tensor)
        
    def propagate_backward(self, t1, learning_rate):
        self.calculate_dz()
        #updating the weights with the learning rate
        self._weights = tensor.tensor_subtraction(self._weights, tensor.tensor_scalar_multiplication(learning_rate, self.get_dw()))
    
    #Takes the dot product of the transposed weights tensor with the next layer's dz.
    #Multiplies that tensor by a tensor of the output tensor, after running the output tensor through the derivative of the activation function
    def calculate_dz(self):

        next_dz = self.next_layer.get_dz()
        weights_transposed = self.transpose(self._weights)
        dot_product_next_dz_and_weights_transposed = tensor.compute_dot_product(weights_transposed, next_dz)
        temp_tensor = tensor(self.rows, self.columns)
        for i in temp_tensor:
            temp_tensor.t[i] = self.activation_function_prime(self._output_tensor.t[i])
        self._dz = tensor.tensor_multiplication(dot_product_next_dz_and_weights_transposed, temp_tensor)


    def feed_input(self,t1):

        self.next_layer.initialize_input(t1)

    def initialize_input(self, t1):

        self._input_tensor = t1

    def get_outtput_tensor(self):

        return self._output_tensor

    

    def get_dz(self):

        return self._dz
    


    


        