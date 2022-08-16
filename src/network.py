#this class will create the basic network of layers

from email import header
import layer
import tensor
class network:

    head = layer()
    tail = layer()

    def __init__(self, next_layer, prev_layer):

        self.next_layer = next_layer
        self.prev_layer = prev_layer

    def add_layer(self, l):

        if (head == None):
            head = l
            tail = head
        else:
            tail.set_next_layer(l)
            l.set_previous_layer(tail)
            tail = l
    
    def run_real(training, input, test_tensor, optimize, epoch_number):

        epoch_number = 1
        network.head.initialize_input(input)
        current = network.head
        while (current is not network.tail):
            current.propagate_forwards()
            current = current.next()
        current.propagate_forwards()
        while (current is not None):
            optimize.propagate_backwards(current, test_tensor, epoch_number)
            current = current.prev_layer

    def run_train(training_iterations, input, test_tensor, optimize):

        epoch_number = 1
        network.head.set_input(input)
        current = network.head
        while (current is not network.tail):
            current.propagate_forward()
            current = current.get_next()

        current.propagage_forward()

        print("Prediction is")
        tensor.print_tensor(current.get_output_tensor())
        print("Actual is")
        tensor.print_tensor(test_tensor)

        i = 0
        while (i < training_iterations):

            network.run_real(input, test_tensor, optimize, epoch_number)
            print("Iteration is", epoch_number)
            epoch_number += 1

        network.head.set_input(input)
        current = network.head
        while (current is not network.tail):
            current.propagate_forward()
            current = current.get_next()
        
        print("Prediction is")
        tensor.print_tensor(current.get_output_tensor())
        print("Actual is")
        tensor.print_tensor(test_tensor)



    

            
            

