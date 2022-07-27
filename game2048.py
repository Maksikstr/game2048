import random
import keyboard
import click
import sys

score = []
best_score = 0


def show_state(state):
    #  TODO параметризируйте эти константы через sys.args (click) в show_state
    w_cell = 3
    h_cell = 1

    matrix = state['matrix']
    hor_line = ('+' + '-' * w_cell) * state['size'] + '+\n'
    line_with_gaps = ('|' + '%s') * state['size'] + '|\n'
    table = (hor_line + line_with_gaps * h_cell) * state['size'] + hor_line

    # TODO добавьте отображение текущего и лучшего score
    print(state)
    print('\n' * 2)
    print(table % tuple((str(cell).center(w_cell, ' ') for row in matrix for cell in row)))
    print("Score:  ", state['score'])
    print("Best score:  ", state['best score'])


def step(state, cmd):
    n_turns = {  # main direction is left
        'w': (4, 4),
        'a': (1, 3),
        's': (2, 2),
        'd': (3, 1),
    }
    before, after = n_turns[cmd]

    # turn - функция поворота матрицы на 90 гр


def turn(matrix):
    matrix_r = [list(reversed(col)) for col in zip(*matrix)]
    return matrix_r


def aggregation(matrix_r, score):
    for row in matrix_r:
        while 0 in row:
            row.remove(0)
        while len(row) != len(matrix_r):
            row.append(0)
    for i in matrix_r:
        for j in range(len(i) - 1):
            if i[j] == i[j + 1]:
                i[j] *= 2
                i.pop(j + 1)
                score.append(i[j])
                while len(i) != len(matrix_r):
                    i.append(0)
    return matrix_r, score


def sum_score(score):
    score = sum(score)
    return score


score = sum_score(score)

def create_matrix(state):
    m = [0 for _ in range(state['size'])]
    pass

def randomize(matrix_r, state):
    coordinates = [(x, y) for x in state['size'] for y in state['size']]
    row = state['size']
    while row > 0:
        x, y = random.choice(coordinates)
        matrix_r[x][y] = random.choice([2, 4])
        row -= 1
    return matrix_r, state
    # randomize - DONE

    # save_state - сохранить state на диск используя pickle/json

    # TODO реализовать псевдокод снизу    
    # repeate turn() `before` times
    # for_each row remove zeros
    # for_each  row aggregation
    # for_each  append zeros at the end
    # randomize()
    # repeate turn() `after` times
    # save_state()


def event(state, cmd):
    # TODO обрабатывать новые команды можно тут
    if cmd == 'exit':
        exit(0)
    elif cmd == 'new':
        pass
    elif cmd in 'wasd':
        step(state, cmd)


# TODO добавьте click-параметры (размер сетки)
def run():
    state = dict()
    state['size'] = 0
    game = input("Начать новую игру - yes,  продолжить старую - no: ")
    game = game.lower().strip()
    if game == "yes":
        state['size'] = int(input("Ведите размер игрового поля: "))
    state['matrix'] = [[0] * state['size'] for _ in range(state['size'])]
    state['score'] = 0
    state['best_score'] = 0
    state['is_finished'] = False

    # TODO сделайте инициализацию через init_state() с возможностью загрузки state с уже сохраненного раннее файла
    # state = init_state() # it's better option

    while True:
        show_state(state)
        ev = keyboard.read_event()
        # handling keys push up
        if ev.event_type != 'up': continue
        cmd = ev.name
        if cmd == "enter":
            continue
        print(event)
        print(cmd)
        state['matrix'] = event(state, cmd)
        if game == "no":
            state['score'] = score
        print(cmd)

        # show_state(state)
        # TODO добавьте операцию выхода из игры


if __name__ == '__main__':
    run()
