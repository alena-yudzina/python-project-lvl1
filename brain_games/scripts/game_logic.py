from ..cli import welcome_user


def start_game(randomize, game_task, ask, correct_answer):
    name = welcome_user()
    print(game_task())
    result = f"Congratulations, {name}!"
    for i in range(3):
        params = randomize()
        answer = ask(params)
        correct = correct_answer(params)
        if answer != correct:
            result = f"Let's try again, {name}!"
            print(f'"{answer}" is wrong answer ;(. Correct answer was '
                  f'"{correct}"')
            break
        else:
            print('Correct!')
    print(result)
