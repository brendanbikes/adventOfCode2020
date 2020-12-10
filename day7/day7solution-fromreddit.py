import re

bag_contents_lookup = dict()
bag_parent_lookup = dict()
bag_regex = re.compile("^([a-z ]+) bags contain ((?:(?:[0-9a-z ]+)(, )*)+)\.$")
bag_contents_regex = re.compile("^([0-9]+) ([a-z ]+) bags*$")
with open("day7input.txt", "r") as puzzle_input:
  for line in puzzle_input:
    # Parse line into parent bag and bag contents
    match = bag_regex.match(line.rstrip())
    bag_type = match.group(1)
    bag_contents = list()
    bag_contents_lookup[bag_type] = bag_contents
    
    # Add contents to bag based on amount:type tuple
    for inner_bag_line in match.group(2).split(", "):
      bag_contents_match = bag_contents_regex.match(inner_bag_line)
      
      if bag_contents_match is not None:
        inner_bag_type = bag_contents_match.group(2)
        bag_contents.append((int(bag_contents_match.group(1)), inner_bag_type))

        # Create a mapping of bags this fits in so we can trace inner bag to top most bag
        parent_set = bag_parent_lookup.get(inner_bag_type, None)
        if parent_set is None:
          parent_set = set()
          bag_parent_lookup[inner_bag_type] = parent_set
        
        parent_set.add(bag_type)

def get_parent_bag_types(bag_type):
  if bag_type in bag_parent_lookup:
    for parent_bag_type in bag_parent_lookup[bag_type]:
      yield parent_bag_type
      
      for inner_parent_type in get_parent_bag_types(parent_bag_type):
        yield inner_parent_type

def get_inner_bag_count(bag_type):
  inner_bag_count = 0
  
  # inner_bag = tuple. First is quantity, second is type
  for inner_bag in bag_contents_lookup[bag_type]:
    inner_bag_count += inner_bag[0] + inner_bag[0] * get_inner_bag_count(inner_bag[1])

  return inner_bag_count

def part1():
  unique_bag_types = set(get_parent_bag_types("shiny gold"))
  return len(unique_bag_types)

def part2():
  return get_inner_bag_count("shiny gold")

print("Part 1 Result: ", part1())
print("Part 2 Result: ", part2())