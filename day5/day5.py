from boilerplate import InitialiseInput

def main():
  initialised_input = InitialiseInput(no_strip=True)
  content = initialised_input.get_text_content()
  
  split_part = content.index('')
  crane_state = [item for item in content[:split_part] if '[' in item]
  actions = content[(split_part + 1):]

  updated_crane_state = []
  for line in crane_state:
    updated_line = ''
    for index, character in enumerate(line):
      if (index == 0 or index % 4 == 0) and character == ' ':
        updated_line += '['
      elif (index == 1 or index % 4 == 1) and character == ' ':
        updated_line += '*'
      elif (index == 2 or index % 4 == 2) and character == ' ':
        updated_line += ']'
      else:
        updated_line += character
    updated_crane_state.append(updated_line)

  print(updated_crane_state)

if __name__ == '__main__':
  main()