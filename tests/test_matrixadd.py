'''
Created on Dec. 6, 2019

@author: lauzo
'''

from matrixadd import matrix_add
import unittest


class MatrixAddTest(unittest.TestCase):
    
    def test_add(self):
        matrix1 = [[1, -2], [-3, 4]]
        matrix2 = [[2, -1], [0, -1]]
        result = matrix_add.add(matrix1, matrix2)
        self.assertEqual(result, [[3, -3], [-3, 3]],
                         'The result of the matrix add is wrong')

