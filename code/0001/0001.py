# github.com/bryangoodrich/python-exercises
# code/0001/0001.py
source = "input.txt"
target = "output.csv"
with open(source) as source_fh, open(target, 'w') as output_fh:
    data = source_fh.read().replace(";", "\n")
    bytes_written = output_fh.write(data)
