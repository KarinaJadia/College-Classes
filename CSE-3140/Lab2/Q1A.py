import os

DIRECTORY = '/home/cse/Lab2/Solutions'

def make_list(directory):
  pythons = []
  for file in os.listdir(directory):
    if file[-3:] == ".py":
      pythons.append(file)
  return pythons

def main():
  python_files = make_list(DIRECTORY)
  output_filename = "files.txt"

  with open(output_filename, 'w') as output_file:
    for file in python_files:
      output_file.write(file + '\n')

if __name__ == "__main__":
  main()