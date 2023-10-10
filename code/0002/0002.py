# github.com/bryangoodrich/python-exercises
# code/0002/0002.py
sz = 3  # chunk size
data = [1, 2, 3, 4, 5, 6, 7, 8]
starts = range(0, len(data), sz)  # [0, 3, 6]
batches = [data[i:(i+sz)] for i in starts]
print(batches)  
# [[1, 2, 3], [4, 5, 6], [7, 8]]