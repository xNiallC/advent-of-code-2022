from boilerplate import InitialiseInput

opponent_guide = {
  'A': { 'type': 'rock' },
  'B': { 'type': 'paper' },
  'C': { 'type': 'scissors' },
}

your_guide = {
  'X': { 'result': 'lose' },
  'Y': { 'result': 'draw' },
  'Z': { 'result': 'win' },
}

rules = {
  'rock': { 'rock': 'draw', 'paper': 'win', 'scissors': 'lose', 'extraPoints': 1 },
  'paper': { 'rock': 'lose', 'paper': 'draw', 'scissors': 'win', 'extraPoints': 2 },
  'scissors': { 'rock': 'win', 'paper': 'lose', 'scissors': 'draw', 'extraPoints': 3 },
}

points = {
  'lose': 0,
  'draw': 3,
  'win': 6,
}

def main():
  initialised_input = InitialiseInput()
  content = initialised_input.get_text_content()

  round_scores = []
  for round in content:
    plays = round.split(' ')
    opp_play = opponent_guide[plays[0]]

    your_required_result = your_guide[plays[1]]['result']
    print(opp_play['type'])
    print(your_required_result)

    new_points = 0
    for item, gameplay in rules.items():
      if item == opp_play['type']:
        for key, value in gameplay.items():
          if value == your_required_result:
            print(key)
            new_points += rules[key]['extraPoints']
            new_points += points[your_required_result]

    round_scores.append(new_points)
    print('----')
  print(round_scores)
  print(sum(round_scores))


if __name__ == '__main__':
  main()