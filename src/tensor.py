import numpy as np
import random
import math

class tensor:

    rows = None
    columns = None
    t = []

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns

    def get_rows(self):

        return self.rows
    
    def get_columns(self):

        return self.columns

    def compare_tensor_dimensions(t1, t2):

        if (t1.get_rows() != t1.get_rows or t1.get_columns != t2.get_columns):
            raise Exception("These tensors have different dimensions")

    #this will primarily be used for randomizing weights and bias
    def randomize_new_tensor(t1, lower_bound, upper_bound):

        for i in t1:
            t1.t[i] = random.uniform(lower_bound, upper_bound)



    #cmoputes the dot product between 2 tensors, returns a new tensor
    def compute_dot_product(t1,t2):

        r = t1.get_rows()
        c = t2.get_columns()
        dot_product_tensor = tensor(r,c)
        i = 0
        while (i < r):
            j = 0
            while (j < c):
                product = 0
                k = 0
                while (k < t1.get_columns()):
                    a = t1.t[i * t1.columns() + k]
                    b = t2.t[k * c + i]
                    product += a * b
                    k+=1
                dot_product_tensor.t[i * c + j] = product
                j+=1
            i+=1
        return dot_product_tensor


    #transposes a tensor
    def transpose(t1):

        r = t1.get_rows()
        c = t1.get_columns()
        transposed_tensor = tensor(r,c)
        i = 0
        while (i < r):
            j = 0
            while (j < c):
                transposed_tensor.t[i  *c + j] = t1[i + j * r]
                j+=1
            i+=1
        
        return transposed_tensor

    #simple addition between 2 tensors
    def tensor_addition(t1, t2):

        r = t1.get_rows()
        c = t2.get_columns()
        new_tensor = tensor(r,c)
        for i in t1:
            new_tensor.t[i] = t1.t[i] + t2.t[i]
        return new_tensor
        
    #simple subtraction between 2 tensors
    def tensor_subtraction(t1, t2):

        r = t1.get_rows()
        c = t2.get_columns()
        new_tensor = tensor(r,c)
        for i in t1:
            new_tensor.t[i] = t1.t[i] - t2.t[i]
        return new_tensor
        
    #multiplies an element of a tensor by  the same element of another tensor
    def tensor_multiplication(t1, t2):

        r = t1.get_rows()
        c = t2.get_columns()
        new_tensor = tensor(r,c)
        for i in t1:
            new_tensor.t[i] = t1.t[i] * t2.t[i]
        return new_tensor
        
    #divides an element of a tensor by the same element of another tensor
    def tensor_division(t1, t2):

        r = t1.get_rows()
        c = t2.get_columns()
        new_tensor = tensor(r,c)
        for i in t1:
            new_tensor.t[i] = t1.t[i] / t2.t[i]
        return new_tensor

    #simple scalar multiplication for a tensor
    def tensor_scalar_multiplication(t1, a):
        r = t1.get_rows()
        c = t1.get_columns()
        new_tensor = tensor(r,c)
        for i in t1:
            new_tensor.t[i] = t1.t[i] * a
        return new_tensor

    #computes square root of every element for a tensor
    def tensor_square_root(t1):
        r = t1.get_rows()
        c = t1.get_columns()
        new_tensor = tensor(r,c)
        for i in t1:
            new_tensor.t[i] = t1.t[math.sqrt(i)]
    

        

    

    



    