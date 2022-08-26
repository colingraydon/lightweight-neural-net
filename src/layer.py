#this is an class which will be extended
class layer:

    def __init__(self, input_dimensions, output_dimensions, activation_function, activation_function_prime, next_layer=None, previous_layer=None):
        self.input_dimensions = input_dimensions
        self.output_dimensions = output_dimensions
        self.activation_function = activation_function
        self.activation_function_prime = activation_function_prime

    
    def set_next_layer(self,l1):
        self.next_layer = l1

    def set_previous_layer(self,l1):
        self.previous_layer = l1

    def get_next_layer(l1):
        return l1.next_layer
    
    def get_previous_layer(l1):
        return l1.previous_layer

    