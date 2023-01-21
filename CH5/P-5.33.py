'''Write a python program for a matrix class that can add and multiply two-dimensional arrays of
numbers. assuming the dimensions  agree appropriately  for the operation
'''

class Matrix:

    def __init__(self, array):
        self.row = len(array)#row is defined by the
        self.column = len(array[0])#column is defined by the number of values in the first index of the list
        self.matrix = array

    def get_size(self):
        return self.row, self.column

    def get_rows(self, i):
        return self.matrix[i][:]

    def get_columns(self, i):
        return self.matrix#left off here, finish later had to leave





if __name__ == '__main__':
    #proper way to initialize a 2d array in python is result = [ [0] * c for j in range(r) ]


