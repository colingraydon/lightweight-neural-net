#this class will create the basic network of layers

from layer import layer
from tensor import tensor
class network:


    def __init__(self, head=None, tail=None):

        self.head = head
        self.tail = tail

    def add_layer(self, l:layer):

        if (self.head == None):
            self.head = l
            self.tail = self.head
        else:
            self.tail.set_next_layer(l)
            l.set_previous_layer(self.tail)
            self.tail = l
    
    def run_real(self, input, test_tensor, optimize, epoch_number):

        epoch_number = 1
        self.head.initialize_input(input)
        current = self.head
        while (current is not self.tail):
            current.propagate_forward()
            current = current.next_layer
        current.propagate_forward()
        while (current is not None):
            print("got to line 33")
            optimize.propagate_back(current, test_tensor, epoch_number)
            print("current is", current)
            print("current.previous layer is", current.previous_layer)
            current = current.previous_layer

    def run_train(self, training_iterations, input, test_tensor, optimize):

        epoch_number = 1
        self.head.initialize_input(input)
        current = self.head
        while (current is not self.tail):
            current.propagate_forward()
            current = current.get_next_layer()

        current.propagate_forward()

        # print("Prediction is")
        # tensor.print_tensor(current.output_tensor)
        # print("Actual is")
        # tensor.print_tensor(test_tensor)

        i = 0
        while (i < training_iterations):

            self.run_real(input, test_tensor, optimize, epoch_number)
            print("Iteration is", epoch_number)
            epoch_number += 1

        self.head.set_input(input)
        current = self.head
        while (current is not self.tail):
            current.propagate_forward()
            current = current.get_next()
        
        print("Prediction is")
        tensor.print_tensor(current.get_output_tensor())
        print("Actual is")
        tensor.print_tensor(test_tensor)



    

