#this is an class which will be extended

class layer:

    next_layer = None
    previous_layer = None

    def __init__(self, input_dimensions, output_dimensions, activation_function):
        self.input_dimensions = input_dimensions
        self.output_dimensions = output_dimensions
        self.activation_function = activation_function

    
    def set_next_layer(l1):
        next_layer = l1

    def set_previous_layer(l1):
        previous_layer = l1

    def get_next_layer(l1):
        return l1.next_layer
    
    def get_previous_layer(l1):
        return l1.previous_layer

    