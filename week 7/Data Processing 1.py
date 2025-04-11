
def row_index_with_most_number_of_zeros(matrix:list)->int:
    '''
    Given a matrix, find the index of the row with the 
    maximum number of zeros in it.

    Arguments: matrix: list[list] 
    Rertun: int - index of the row with the maximum number of zeros.
    '''
    max_zeros = -1
    max_index = -1

    for i, row in enumerate(matrix):
        zero_count = row.count(0)
        if zero_count > max_zeros:
            max_zeros = zero_count
            max_index = i

    return max_index