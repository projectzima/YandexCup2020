win_numbers = input()
win_numbers = win_numbers.split()
players = input()

for player in range(int(players)):
    counter = 0
    ticket = input()
    ticket = ticket.split()
    for number in ticket:
        if number in win_numbers:
            counter += 1
    if counter >= 3:
        print("Lucky")
    else:
        print("Unlucky")
