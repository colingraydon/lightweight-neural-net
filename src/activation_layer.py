from layer import layer
from tensor import tensor
import math



class activation_layer(layer):



    #these values are standard for adam optimization. 
    #beta1 is for first moment estimates, beta2 for second moment estimates
    #epsilon just prevents any divide by 0 errors.
    beta1 = .9
    beta2 = .999
    epsilon = 10 ** -8



    def __init__(self, input_dimensions, output_dimensions, activation_function, activation_function_prime, weights=None, bias=None, input_tensor=None, output_tensor=None, dz=None, vdw=None, sdw=None):

        super().__init__(input_dimensions, output_dimensions, activation_function, activation_function_prime)
        self.input_tensor = input_tensor
        self.weights = tensor(output_dimensions, input_dimensions)
        self.bias = tensor(output_dimensions, columns=1)
        self.weights = self.set_weights()
        self.bias = self.set_bias()

    #3 is chosen here because that is the number of neurons
    def set_weights(self):

        self.weights = tensor.randomize_new_tensor(self.output_dimensions, self.input_dimensions, 0, 3)

    def update_weights(self, learning_rate):

        self.weights = tensor.tensor_subtraction(self.weights, tensor.tensor_scalar_multiplication(self.get_dw(), learning_rate))

    def get_weights(self):

        return self.weights

    def set_bias(self):
        
        columns = 1
        self.bias = tensor.randomize_new_tensor(self.output_dimensions, columns, 0, 3)

    def get_bias(self):

        return self.bias

    #returns the dw tensor
    def get_dw(self):

        return tensor.compute_dot_product(self.dz, tensor.transpose(self.input_tensor))


    #backward propagation for an adam optimizer
    #There's a whole bunch of math here but essentially the weights are being adjusted via beta1, beta2, epsilon, and various linear algebra formulas
    def propagate_backward_adam(self, learning_rate, epoch_number):

        dt = self.get_dw()
        self.vdw = tensor.tensor_addition(tensor.tensor_scalar_multiplication(self.vdw, self.beta1), tensor.tensor_scalar_multiplication(dt, (1 - self.beta1)))
        self.sdw = tensor.tensor_addition(tensor.tensor_scalar_multiplication(self.sdw, self.beta2), tensor.tensor_scalar_multiplication(tensor.tensor_multiplication(dt, dt), (1-self.beta2)))
        new_vdw = tensor.tensor_scalar_multiplication(self.vdw, (1 / (1-math.exp(self.beta1, epoch_number))))
        new_sdw = tensor.tensor_scalar_multiplication(self.sdw, (1 / (1-math.exp(self.beta2, epoch_number))))
        temp_tensor = tensor(new_sdw.get_rows(), new_sdw.get_columns())
        new_tensor = tensor.tensor_division(new_vdw, tensor.tensor_subtraction(tensor.tensor_square_root(new_sdw), tensor.tensor_scalar_multiplication(temp_tensor, self.epsilon)))
        self.weights = tensor.tensor_subtraction(self.weights, tensor.tensor_scalar_multiplication(new_tensor, learning_rate))

    #Takes the dot product of the weights and the input tensor, runs it through the activation function
    #Sets the next layer with this tensor
    def propagate_forward(self):

        # print(self.weights.rows)
        # print("weights.rows is above, printed from propagate forward")
        # print(self.weights.columns)
        # print("self.weights.columns, printed from propagate forward")
        # print(self.input_tensor.rows)
        # print("input rows is above, printed from propagate forward")
        # print(self.input_tensor.columns)
        # print("input columns, printed from propagate forward")
        self.output_tensor = tensor.compute_dot_product(self.weights, self.input_tensor)
        temp_tensor = tensor(self.output_tensor.rows, self.output_tensor.columns)
        temp_tensor.t = []
        i = 0
        while (i < temp_tensor.rows * temp_tensor.columns):
            temp_tensor.t.append(self.activation_function(self.output_tensor.t[i]))
            i += 1
        self.feed_input(temp_tensor)
        
    # def propagate_backward(self, t1, learning_rate):
    #     self.calculate_dz()
    #     #updating the weights with the learning rate
    #     self.weights = tensor.tensor_subtraction(self.weights, tensor.tensor_scalar_multiplication(learning_rate, self.get_dw()))

    def propagate_backward(self, learning_rate, test=None):

        self.calculate_dz()
        #updating the weights with the learning rate
        self.weights = tensor.tensor_subtraction(self.weights, tensor.tensor_scalar_multiplication(learning_rate, self.get_dw()))

    
    #Takes the dot product of the transposed weights tensor with the next layer's dz.
    #Multiplies that tensor by a tensor of the output tensor, after running the output tensor through the derivative of the activation function
    def calculate_dz(self):

        next_dz = self.next_layer.get_dz()
        weights_transposed = tensor.transpose(self.weights)
        print("---------------------------------")
        print("weights transposed rows is", weights_transposed.rows)
        print("weights transposed columns is", weights_transposed.columns)
        print("next dz rows is", next_dz.rows)
        print("next dz columns is", next_dz.columns)
        dot_product_next_dz_and_weights_transposed = tensor.compute_dot_product(weights_transposed, next_dz)
        temp_tensor = tensor(self.rows, self.columns)
        temp_tensor.t = []
        i = 0
        while (i < (temp_tensor.rows * temp_tensor.columns)):
            temp_tensor.t.append(self.activation_function_prime(self.output_tensor.t[i]))
            i += 1
        self.dz = tensor.tensor_multiplication(dot_product_next_dz_and_weights_transposed, temp_tensor)


    #sets input for next layer
    def feed_input(self,t1):

        self.next_layer.initialize_input(t1)

    #sets input tensor for that layer
    def initialize_input(self, t1):

        self.input_tensor = t1
        self.set_bias()
        self.set_weights()

    def get_outtput_tensor(self):

        return self.output_tensor

    def get_dz(self):

        return self.dz
    


    


        