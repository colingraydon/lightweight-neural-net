import numpy as np

class tensor:

    rows = None
    columns = None
    object_matrix = []

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
                    a = t1.object_matrix[i * t1.columns() + k]
                    b = t2.object_matrix[k * c + i]
                    total += a * b
                    k+=1
                j+=1
            i+=1


    #transposes a tensor
    def transpose(t):

        r = t.get_rows()
        c = t.get_columns()
        transposed_tensor = tensor(r,c)
        i = 0
        while (i < r):
            j = 0
            while (j < c):
                transposed_tensor.object_matrix[i  *c + j] = t[i + j * r]
                j+=1
            i+=1
        
        return t

    def tensor_addition(t1, t2):

        r = t1.get_rows()
        c = t2.get_columns()
        new_tensor = tensor(r,c)
        for i in t1:
            new_tensor.object_matrix[i] = t1.object_matrix[i] + t2.object_matrix[i]
        return new_tensor
        
    def tensor_subtraction(t1, t2):

        r = t1.get_rows()
        c = t2.get_columns()
        new_tensor = tensor(r,c)
        for i in t1:
            new_tensor.object_matrix[i] = t1.object_matrix[i] - t2.object_matrix[i]
        return new_tensor
        
    def tensor_multiplication(t1, t2):

        r = t1.get_rows()
        c = t2.get_columns()
        new_tensor = tensor(r,c)
        for i in t1:
            new_tensor.object_matrix[i] = t1.object_matrix[i] * t2.object_matrix[i]
        return new_tensor
        
    def tensor_division(t1, t2):

        r = t1.get_rows()
        c = t2.get_columns()
        new_tensor = tensor(r,c)
        for i in t1:
            new_tensor.object_matrix[i] = t1.object_matrix[i] / t2.object_matrix[i]
        return new_tensor

    def tensor_scalar_multiplication(t, a):
        r = t.get_rows()
        c = t.get_columns()
        new_tensor = tensor(r,c)
        for i in t:
            new_tensor.object_matrix[i] = t.object_matrix[i] * a
        return new_tensor

    

        

    

    



    