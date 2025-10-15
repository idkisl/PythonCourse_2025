import sys
import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('name', type=str, help='Name')
parser.add_argument('--age', type=int, help='Age', default=32, required=False)
args = parser.parse_args()
print(args)


# print(sys.argv)
# os.rename("my_csv_sample.csv", "csv_sample.csv")