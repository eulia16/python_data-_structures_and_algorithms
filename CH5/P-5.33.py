class Matrix:

    def __init__(self, Array1):
        self._array_1 = Array1


    # def Add_2D_Array(self, Array1, Array2):
    #     #see if row lengths match
    #     if len(Array1) != len(Array2):
    #         print('Array row lengths must match');
    #         return
    #     if len(Array1[0]) != len(Array2[0]):
    #         print('Array column lengths must match');
    #         return
    #     sum = 0
    #     #number of rows
    #     for i in range(len(Array1)):
    #         #number of columns(again assuming same matrix dimensions)
    #         for j in range(len(Array1[0])):
    #             #add each part of array1 and array2 to the sum variable
    #             sum += Array1[i][j]
    #             sum += Array2[i][j]
    #
    #     return sum

    def __add__(self, Array2):
        self._array_2 = Array2
        # see if row lengths match
        if len(self._array_1) != len(self._array_2):
            print('Array row lengths must match');
            return
        if len(self._array_1[0]) != len(self._array_2[0]):
            print('Array column lengths must match');
            return
        sum = 0
        # number of rows
        for i in range(len(self._array_1)):
            # number of columns(again assuming same matrix dimensions)
            for j in range(len(self._array_1[0])):
                # add each part of array1 and array2 to the sum variable
                sum += self._array_1[i][j]
                sum += self._array_2[i][j]

        return sum

    def __mul__(self, Array2):
        self._array_2 = Array2
        # see if row lengths match
        if len(self._array_1) != len(self._array_2):
            print('Array row lengths must match');
            return
        if len(self._array_1[0]) != len(self._array_2[0]):
            print('Array column lengths must match');
            return
        product = 1
        # number of rows
        for i in range(len(self._array_1)):
            # number of columns(again assuming same matrix dimensions)
            for j in range(len(self._array_1[0])):
                # add each part of array1 and array2 to the sum variable
                product *= self._array_1[i][j]
                product *= self._array_2[i][j]

        return product








if __name__ == '__main__':
    data1 = [[1 , 2], [2,3], [3,4]]#15
    data2 = [[2,3], [3,4], [4,5]]#21
    matrix = Matrix(data1)
    print(matrix + data2)
    print(matrix * data2)
    #print(matrix.Add_2D_Array(data1, data2))
