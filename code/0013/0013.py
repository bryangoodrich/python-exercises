# github.com/bryangoodrich/python-exercises
# code/0013/0013.py
# python 0013.py -j incorrect_input
#   usage: 0013.py [-h] [--job JOB]
#   0013.py: error: Please provide a module name using --job or -j.
# python 0013.py --job job1
#   Running job 1 ...
#   Time taken: 7.006964683532715 seconds
# python 0013.py --job job2
#   Running job 2 ...
#   Time taken: 5.004326343536377 seconds
import sys
import importlib
import argparse
import time

def main(args):
    parser = argparse.ArgumentParser(description='Load a job module to run.')
    parser.add_argument('--job', '-j', type=str, help='Name of the job module.')
    args = parser.parse_args(sys.argv[1:])
    if not args.job:
        parser.error('Please provide a module name using --job or -j.')

    try:
        job_module = importlib.import_module(f'packit.{args.job}')
        start_time = time.time()
        job_module.run()
        end_time = time.time()
        print(f'Time taken: {end_time - start_time} seconds')
    except ModuleNotFoundError:
        print(f"Module '{args.job}' not found in the 'package'.")

if __name__ == "__main__":
    args = sys.argv[1:]
    main(args)
