import torch
import time

# check if GPU processing is available
if torch.cuda.is_available():
    # set device to CUDA
    device = torch.device("cuda")
    print("using GPU...")
else:
    # set device to CPU
    device = torch.device("cpu")
    print("using CPU... can't access GPU")

# set matrix size
matrix_size = 64*512

# create 2 matrices and fill with random numbers
x = torch.randn(matrix_size, matrix_size)
y = torch.randn(matrix_size, matrix_size)

# load matrices to device
x_gpu = x.to(device)
y_gpu = y.to(device)
# halt CPU until GPU is done processing
torch.cuda.synchronize()

# run 3 consecutive speed tests
for i in range(3):
    start = time.time()
    # multiply matrices
    result = torch.matmul(x_gpu, y_gpu)
    # halt CPU until GPU is done processing
    torch.cuda.synchronize()
    print("run {}: | speed: {} seconds".format(i, round(time.time() - start, 2)))

print("\nverify device:", result.device)