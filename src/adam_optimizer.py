import layer

class adam_optimizer:

    def __init__(self, learning_rate, epoch_number):

        self.learning_rate = learning_rate
        self.epoch_number = epoch_number

    def propagate_backwards(self, l):
        
        l.propagate_backwards_adam(self.learning_rate, self.epoch_number)

    def propagate_backwards(self, l, test):
        l.dz(test)
        l.propagate_backwards_adam(self.learning_rate, self.epoch_number)

    
