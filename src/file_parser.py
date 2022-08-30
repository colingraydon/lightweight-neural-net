
class file_parser:

    zero = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    one =  [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
    two =  [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
    three =[0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    four = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
    five = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    six =  [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
    seven =[0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
    eight =[0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
    nine = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1] 

    def parse_column(self, file_path, column):

        file = open(file_path)
        column_collector = []
        column_pointer = 0
        
        for _ in file:

            line = file.readline()
            word = line.split(",")
            for x in word:

                if (column_pointer == column):
                    column_collector.append(x)
                    break
                else:
                    column_pointer += 1

        file.close()
        return column_collector

    def parse_first_last(self, file_path, first_column, last_column):   

        file = open(file_path)
        column_collector = []
        column_pointer = 0
        
        for _ in file:

            line = file.readline()
            word = line.split(",")
            for x in word:

                if (column_pointer < first_column):
                    column_pointer += 1
                elif (column_pointer > last_column):
                    break
                else:
                    column_collector.append(x)

        file.close()
        return column_collector

    def parse(self, file_path):   

        file = open(file_path)
        column_collector = []
        
        for _ in file:

            line = file.readline()
            word = line.split()
            for x in word:

                column_collector.append(x)

        file.close()
        return column_collector
    
    #parses the mnist data using one-hot encoding
    #passes the file path and calls parse
    def one_hot_mnist_path(self, file_path):

        one_hot_collector = []
        p = file_parser
        column_number = 0
        pre_encoding = p.parse(file_path, column_number)
        for x in pre_encoding:
            if (x == 0):
                one_hot_collector.append(file_parser.zero)
            elif (x == 1):
                one_hot_collector.append(file_parser.one)
            elif (x == 2):
                one_hot_collector.append(file_parser.two)
            elif (x == 3):
                one_hot_collector.append(file_parser.three)
            elif (x == 4):
                one_hot_collector.append(file_parser.four)
            elif (x == 5):
                one_hot_collector.append(file_parser.five)
            elif (x == 6):
                one_hot_collector.append(file_parser.six)
            elif (x == 7):
                one_hot_collector.append(file_parser.seven)
            elif (x == 8):
                one_hot_collector.append(file_parser.eight)
            elif (x == 9):
                one_hot_collector.append(file_parser.nine)

        return one_hot_collector

    #passes a list in and performs one-hot encoding on the list
    def one_hot_mnist(self, column_collector):

        one_hot_collector = []

        for x in column_collector:
            if (x == 0):
                one_hot_collector.append(file_parser.zero)
            elif (x == 1):
                one_hot_collector.append(file_parser.one)
            elif (x == 2):
                one_hot_collector.append(file_parser.two)
            elif (x == 3):
                one_hot_collector.append(file_parser.three)
            elif (x == 4):
                one_hot_collector.append(file_parser.four)
            elif (x == 5):
                one_hot_collector.append(file_parser.five)
            elif (x == 6):
                one_hot_collector.append(file_parser.six)
            elif (x == 7):
                one_hot_collector.append(file_parser.seven)
            elif (x == 8):
                one_hot_collector.append(file_parser.eight)
            elif (x == 9):
                one_hot_collector.append(file_parser.nine)
                
        return one_hot_collector







