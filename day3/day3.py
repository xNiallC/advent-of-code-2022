import string, math
from boilerplate import InitialiseInput

def main():
  initialised_input = InitialiseInput()
  content = initialised_input.get_text_content()

  all_letters = list(string.ascii_letters)

  # Part 1
  duplicate_letters = []
  for rucksack in content:
    rucksack_contents = list(rucksack)
    number_contents = len(rucksack_contents)
    middle_list = math.floor(number_contents / 2)
    first_compartment = rucksack_contents[:middle_list]
    second_compartment = rucksack_contents[middle_list:]
    duplicate_compartment_items = list(set(first_compartment) & set(second_compartment))
    for item in duplicate_compartment_items:
      duplicate_letters.append(item)

  # print(duplicate_letters)
  letter_priorities = [all_letters.index(dupe) + 1 for dupe in duplicate_letters]
  # print(letter_priorities)
  # print(sum(letter_priorities))

  # Part 2
  current_three_group = []
  duplicate_letters = []
  for index, rucksack in enumerate(content):
    current_three_group.append(rucksack)
    if index != 0 and (index + 1) % 3 == 0:
      group_dupe = list((set(current_three_group[0]) & set(current_three_group[1]) & set(current_three_group[2])))[0]
      duplicate_letters.append(group_dupe)
      print(current_three_group)
      current_three_group = []

  letter_priorities = [all_letters.index(dupe) + 1 for dupe in duplicate_letters]
  print(sum(letter_priorities))




if __name__ == '__main__':
  main()