'''P-5.32:
Write a Python function that takes two three dimensional numeric data sets and adds them componentwise
'''

def component_wise_addition(n1, n2):
    '''the n1 and n2 format looks like a list of a list of a list, creating a 3d data set, we will add them
    component wise as the problem dictates'''
    result = n1
    for i in range(len(n1)):
        for j in range(len(n2)):
            result[i][j] = n1[i][j] + n2[i][j]
    return result


if __name__ == '__main__':
    data1 = [[22, 18, 709, 5, 33], [45, 32, 830, 120, 750], [4, 880, 45, 66, 61]]
    data2 = [[33, 38, 719, 1, 33], [435, 332, 8340, 1520, 7550], [54, 8580, 545, 656, 561]]
    print(component_wise_addition(data1, data2))