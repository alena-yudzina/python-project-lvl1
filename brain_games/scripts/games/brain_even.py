from ..game_logic import start_game
import random
import prompt


def randomize():
    random_number_1 = random.randint(0, 100)
    params = {
        'num_1': random_number_1,
    }
    return params


def game_task():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def ask(params):
    return prompt.string(f"Question: {params['num_1']}\nYour answer: ")


def correct_answer(params):
    if params['num_1'] % 2 != 0:
        return 'no'
    return 'yes'


def main():
    start_game(randomize, game_task, ask, correct_answer)


if __name__ == "__main__":
    main()
