from ..game_logic import start_game
import random
import prompt


def randomize():
    random_start = random.randint(0, 20)
    random_step = random.randint(1, 7)
    random_pos_hide = random.randint(0, 9)
    params = {
        'start_num': random_start,
        'step': random_step,
        'hide_pos': random_pos_hide
    }
    return params


def game_task():
    return 'What number is missing in the progression?'


def ask(params):
    last_num = params['start_num'] + 10 * params['step']
    progression = [str(x) for x in range(params['start_num'],
                   last_num, params['step'])]
    progression[params['hide_pos']] = '..'
    return prompt.string(f"Question: {' '.join(progression)}"
                         f"\nYour answer: ")


def correct_answer(params):
    correct = params['start_num'] + params['hide_pos'] * params['step']
    return str(correct)


def main():
    start_game(randomize, game_task, ask, correct_answer)


if __name__ == "__main__":
    main()
