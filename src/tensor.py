import numpy as np
import random
import math

class tensor:


    def __init__(self, rows, columns, t=None):
        self.rows = rows
        self.columns = columns
        self.t = t
        


    def get_rows(self):

        return self.rows
    
    def get_columns(self):

        return self.columns

    def compare_tensor_dimensions(t1, t2):

        if (t1.get_rows() != t1.get_rows() or t1.get_columns() != t2.get_columns()):
            raise Exception("These tensors have different dimensions")

    #this will primarily be used for randomizing weights and bias
    def randomize_new_tensor(t1, lower_bound, upper_bound):

        r = t1.get_rows()
        c = t1.get_columns()
        i = 0
        temp_list = []
        while (i < (r * c)):
            temp_list.append(random.uniform(lower_bound, upper_bound))
            i += 1
        t1.t = temp_list
        return t1


    #cmoputes the dot product between 2 tensors, returns a new tensor
    def compute_dot_product(t1,t2):

        r1 = t1.get_rows()
        r2 = t2.get_rows()
        c1 = t1.get_columns()
        c2 = t2.get_columns()
        i = 0
        temp_list = []
        while (i < (r1 * c2)):
            temp_list.append(0)
            i += 1
        dot_product_tensor = tensor(r1,c2, temp_list)
        i = 0
        while (i < r1):
            j = 0
            while (j < c2):
                product = 0
                k = 0
                while (k < c1):
                    a = t1.t[i * c1 + k]
                    b = t2.t[k * c2 + i]
                    product += a * b
                    k+=1
                dot_product_tensor.t[i * c2 + j] = product
                j+=1
            i+=1
        return dot_product_tensor


    #transposes a tensor
    def transpose(t1):

        c = t1.get_rows()
        r = t1.get_columns()
        i = 0
        temp_list = []
        while (i < (r * c)):
            temp_list.append(0)
            i += 1
        i = 0
        transposed_tensor = tensor(r, c, temp_list)
        while (i < r):
            j = 0
            while (j < c):
                transposed_tensor.t[i  *c + j] = t1.t[i + j * r]
                j+=1
            i+=1
        
        return transposed_tensor

    #simple addition between 2 tensors
    def tensor_addition(t1, t2):

        r = t1.get_rows()
        c = t2.get_columns()
        i = 0
        temp_list = []
        while (i < r * c):
            temp_list.append(t1.t[i] + t2.t[i])
            i += 1
        new_tensor = tensor(r,c, temp_list)
        return new_tensor
        
    #simple subtraction between 2 tensors
    def tensor_subtraction(t1, t2):

        r = t1.get_rows()
        c = t2.get_columns()
        i = 0
        temp_list = []
        while (i < (r * c)):
            temp_list.append(t1.t[i] - t2.t[i])
            i += 1
        new_tensor = tensor(r,c, temp_list)
        return new_tensor
        
    #multiplies an element of a tensor by  the same element of another tensor
    def tensor_multiplication(t1, t2):

        r = t1.get_rows()
        c = t2.get_columns()
        i = 0
        temp_list = []
        while (i < (r * c)):
            temp_list.append(t1.t[i] * t2.t[i])
            i += 1
        new_tensor = tensor(r,c, temp_list)
        return new_tensor
        
    #divides an element of a tensor by the same element of another tensor
    def tensor_division(t1, t2):

        r = t1.get_rows()
        c = t2.get_columns()
        i = 0
        temp_list = []
        while (i < (r * c)):
            temp_list.append(t1.t[i] / t2.t[i])
            i += 1
        new_tensor = tensor(r,c, temp_list)
        return new_tensor

    #simple scalar multiplication for a tensor
    def tensor_scalar_multiplication(t1, a):
        r = t1.get_rows()
        c = t1.get_columns()
        i = 0
        temp_list = []
        while (i < (r * c)):
            temp_list.append(t1.t[i] * a)
            i += 1
        new_tensor = tensor(r,c, temp_list)
        return new_tensor

    #computes square root of every element for a tensor
    def tensor_square_root(t1):
        r = t1.get_rows()
        c = t1.get_columns()
        i = 0
        temp_list = []
        while(i < (r * c)):
            temp_value = t1.t[i]
            temp_list.append(math.sqrt(temp_value))
            i += 1
        new_tensor = tensor(r,c, temp_list)
        return new_tensor

    #sets every element of the tensor to the same value, value
    def set_tensor_value(t1, value):

        r = t1.get_rows()
        c = t1.get_columns()
        i = 0
        temp_list = []
        while (i < (r * c)):
            temp_list.append(value)
            i += 1
        new_tensor = tensor(r,c, temp_list)
        return new_tensor

    #prints out a tensor
    def print_tensor(t1):

        i = 0
        r = t1.get_rows()
        c = t1.get_columns()

        while (i < (c * r)):

            print(t1.t[i], end=" ")
            if (i%c == 1 and i > 0):
                print()
            i += 1


    #prints out an unformatted tensor
    def print_tensor_unformatted(t1):

        print(t1.t)

    





    

        

    

    



    