from boilerplate import InitialiseInput

def main():
  initialised_input = InitialiseInput()
  content = initialised_input.get_text_content()

  elves = []
  current_elf_index = 0
  for line in content:
    if not line:
      current_elf_index += 1
    else:
      if (len(elves) == current_elf_index):
        elves.append({
          'calories_held': [],
          'total': 0
        })
      current_line_calories = int(line)
      elves[current_elf_index]['calories_held'].append(current_line_calories)
      elves[current_elf_index]['total'] = sum(elves[current_elf_index]['calories_held'])

  sorted_elves = sorted(elves, key=lambda elf: elf['total'], reverse=True)
  top_three = sorted_elves[0]['total'] + sorted_elves[1]['total'] + sorted_elves[2]['total']
  print(top_three)

if __name__ == '__main__':
  main()