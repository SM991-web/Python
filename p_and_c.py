import numpy as np

arr = np.array([1, 2, 3, 4, 5])
permuted_arr = np.random.permutation(arr)
print(permuted_arr)

random_permutation = np.random.permutation(10)
print(random_permutation)

replacement_sample = np.random.choice([10, 20, 30, 40, 50], size=4, replace=True)
print(replacement_sample)

replacement_sample = np.random.choice([10, 20, 30, 40, 50], size=4, replace=False)
print(replacement_sample)
