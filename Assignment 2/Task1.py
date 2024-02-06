from functools import cache

# Found from Wikipedia

# Function to calculate the minimum number of scalar multiplications
# required to multiply a chain of matrices with given dimensions
def matrixChainOrder(dims: list[int]) -> int:
    @cache
    def a(i, j):
        # Base case: if there is only one matrix in the chain, return 0
        if i == j:
            return 0
        
        # Calculate the minimum number of scalar multiplications
        # by considering all possible split points in the chain
        return min((a(i, k) + dims[i] * dims[k] * dims[j] + a(k, j) 
                   for k in range(i + 1, j)), default=0)

    # Call the recursive function with the start and end indices of the chain
    return a(0, len(dims) - 1)
