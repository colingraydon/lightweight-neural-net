from tensor import tensor
import sys
class test_class:

    if __name__ == "__main__":



        l1 = [1,4,9,16, 2, 2]
        l2 = [1, 1, 1, 2, 2, 2]
        test1 = tensor(2,3, l1)
        test2 = tensor(3,2, l2)
        temp = tensor.compute_dot_product(test1, test2)
        temp.print_tensor()
