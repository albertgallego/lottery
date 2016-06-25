import os, random

def pick_winner(file):
    lines = []
    with open(file, "r") as f:
        lines = f.readlines();
    random_line_num = random.randrange(0, len(lines))
    return lines[random_line_num]

if __name__ == "__main__":
    print("Route to the file:")
    fil = raw_input()
    print("Number of Winners:")
    numb = int(raw_input())
    llist = []
    while numb!= 0 :
        win = pick_winner(fil)
        if llist.count(win)>=1:
            continue
        elif numb == 3:
            ordinal='rd'
        elif numb == 1:
            ordinal = 'st'
        elif numb == 2:
            ordinal = 'nd'
        elif numb > 3:
            ordinal = 'th'
        print(str(numb) + ordinal + ' place: ' + win)
        llist.append(win)
        numb = numb - 1
    print("End lottery. Enjoy!")
        
