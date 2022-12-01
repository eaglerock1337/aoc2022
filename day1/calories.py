def get_elf_array(lines):
  """
  Get an array of each elf's caloric count
  """
  elves = []
  count = 0

  for line in lines:
    if line == "\n":
      elves.append(count)
      count = 0
    else:
      count += int(line)

  return elves

def get_top_elf(lines):
  """
  Get the top elf from the input using the following rules:
  - elves give items with caloric amounts in sequence
  - between each elf is an empty line
  - each elf is identified by their number in line
  """
  topelf = 0
  topcount = 0
  curelf = 1
  curcount = 0

  for line in lines:
    if line == "\n":
      if curcount > topcount:
        topelf = curelf
        topcount = curcount
      
      curelf += 1
      curcount = 0

    else:
      curcount += int(line)

  return topelf, topcount


def day1():
  """
  Part 1: Determine the elf with the most calories
  """

  inputfile = open("input.txt", "r")  
  data = inputfile.readlines()
  elf, count = get_top_elf(data)

  print(f"Elf #{elf} was the winner with {count} calories.")    

  """
  Part 2: Get calories from top three elves
  """
  elfarray = get_elf_array(data)
  elfarray.sort(reverse=True)
  count = elfarray[0] + elfarray[1] + elfarray[2]

  print(f"The top 3 elves are carrying {count} calories.")  

if __name__ == "__main__":
  day1()