from ..game_logic import start_game
import random
import prompt


def randomize():
    random_number_1 = random.randint(2, 100)
    params = {
        'num': random_number_1,
    }
    return params


def game_task():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def ask(params):
    return prompt.string(f"Question: {params['num']}\nYour answer: ")


def correct_answer(params):
    for i in range(2, int(params['num'] ** 0.5) + 1):
        if params['num'] % i == 0:
            return 'no'
    return 'yes'


def main():
    start_game(randomize, game_task, ask, correct_answer)


if __name__ == "__main__":
    main()
