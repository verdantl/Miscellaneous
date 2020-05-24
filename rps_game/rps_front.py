from tkinter import *

import rps_background

window = Tk()

window.title("Rock Paper Scissors!")

window.geometry('1000x1000')

choice = Label(window, text="Welcome to Rock Paper Scissors!",
               font=('Garamond', 20))

choice.grid(column=100, row=10, padx=350, pady=20)

game = rps_background.Game()

game_one = Button(window)
game_three = Button(window)
game_five = Button(window)

games = [game_one, game_three, game_five]
txt_to_id = {'Rock': 0, 'Paper': 1, 'Scissors': 2}
images = [None, None, None]


def procession():
    for i in range(len(game.buttons)):
        if images[i] is not None:
            games[i].configure(text=game.buttons[i].text, font='Garamond',
                               command=proceed,
                               height=200,
                               width=200,
                               image=images[i], compound=TOP)
            games[i].grid(column=game.buttons[i].location[0],
                          row=game.buttons[i].location[1])

        else:
            games[i].configure(text=game.buttons[i].text, font='Garamond',
                               command=proceed,
                               height=game.buttons[i].size,
                               width=(game.buttons[i].size * 2))
            games[i].grid(column=game.buttons[i].location[0],
                          row=game.buttons[i].location[1],
                          padx=game.buttons[i].size,
                          pady=game.buttons[i].size)


your_choice = Label(window)
computer_choice = Label(window)


def move_selection(move: str):
    human_move = rps_background.Move('Human', move)
    comp_move = rps_background.random_computer_move()
    game.empty()
    procession()
    winner = rps_background.evaluate_winner(human_move, comp_move)

    your_choice.grid(column=100, row=10, padx=350, pady=20)
    computer_choice.grid(column=100, row=100, padx=350, pady=20)

    your_choice.configure(text=f'You chose {human_move.name}.',
                          font=('Garamond', 20), image=images[txt_to_id[move]],
                          compound=BOTTOM)
    computer_choice.configure(text=f'The computer chose {comp_move.name}.',
                              font=('Garamond', 20),
                              image=images[txt_to_id[comp_move.name]],
                              compound=TOP)
    choice.configure(text=f'{winner}')
    choice.grid(row=1000)


def proceed():
    if game.state == 0:
        game.beginning()

        procession()

    elif game.state == 1:

        game.moves_creator(1)
        choice.configure(text='Please choose a move!')

        images[0] = PhotoImage(file='rock.png').subsample(2, 2)
        images[1] = PhotoImage(file='paper.png').subsample(3, 3)
        images[2] = PhotoImage(file='scissors.png').subsample(3, 3)
        procession()
        games[0].configure(command=lambda: move_selection('Rock'))
        games[1].configure(command=lambda: move_selection('Paper'))
        games[2].configure(command=lambda: move_selection('Scissors'))

    else:
        game.empty()
        procession()


proceed()

window.mainloop()
