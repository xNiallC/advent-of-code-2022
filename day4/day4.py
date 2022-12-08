from boilerplate import InitialiseInput

def main():
  initialised_input = InitialiseInput()
  content = initialised_input.get_text_content()

  covered_pairs = 0

  def pair_contained(pair_1, pair_2):
    # If a pair contains another pair
    # The lower bound of pair_1 is greater than or equal to the lower bound of pair_2
    # The upper bound of pair_1 is lower than or equal too the upper bound of pair_2
    pair_1_numbers = [num for num in range(pair_1[0], pair_1[1] + 1)]
    pair_2_numbers = [num for num in range(pair_2[0], pair_2[1] + 1)]
    return bool(set(pair_1_numbers) & set(pair_2_numbers))

  for pair in content:
    split_pair = pair.split(',')
    pair_1 = split_pair[0].split('-')
    pair_2 = split_pair[1].split('-')

    pair_1 = [int(pair_1[0]), int(pair_1[1])]
    pair_2 = [int(pair_2[0]), int(pair_2[1])]
    print(pair_1)
    print(pair_2)

    if pair_contained(pair_1, pair_2) or pair_contained(pair_2, pair_1):
      covered_pairs += 1
      print('Covered')
    print('---')

  print(covered_pairs)

if __name__ == '__main__':
  main()