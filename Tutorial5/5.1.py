import numpy as np

def transpose(mata, matb):
    try:
        arr_a = np.array(mata)
        arr_b = np.array(matb)
        
        if arr_a.shape != arr_b.shape:
            raise ValueError("dimesnions must be same")
        
        mat_sum = arr_a + arr_b
        
        mat_tran = mat_sum.T
        
        return mat_sum, mat_tran
    except Exception as error:
        return str(error)


data1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
data2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

sum_res, tran_res = transpose(data1, data2)
print("Matrix Sum:")
print(sum_res)
print("\nTransposed Sum:")
print(tran_res)