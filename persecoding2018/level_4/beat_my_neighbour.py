x, y = input().split(' ')
x_hand = [a for a in x]
y_hand = [b for b in y]
pile = []
stop = int(input())
pile_collection = 0
x_deals = True
y_deals = True
y_pay = -1
x_pay = -1
x_no_pay = True
y_no_pay = True
turn = 0
def return_pay(c):
    if c == 'A':
        return 4
    elif c == 'K':
        return 3
    elif c == 'Q':
        return 2
    elif c == 'J':
        return 1
    else:
        return 0

def default():
    global x_deals
    x_deals = True
    global y_deals
    y_deals = True
    global x_no_pay
    x_no_pay = True
    global y_no_pay
    y_no_pay = True
    global y_pay
    y_pay = -1
    global x_pay
    x_pay = -1

while True:
    if pile_collection == stop:
        print(''.join(x_hand)) #may change
        break
    
    if turn == 0:
        if x_deals:
            if x_no_pay:
                card = x_hand.pop(0)
                pile.append(card)
                if return_pay(card) > 0:
                    x_deals = False
                    y_deals = True 
                    y_pay = return_pay(card)
                    y_no_pay = False
            if x_pay > 0:
                card = x_hand.pop(0)
                pile.append(card)
                if return_pay(card) > 0:
                    x_deals = False
                    y_deals = True
                    y_pay = return_pay(card)
                    y_no_pay = False
                    x_pay = -1
                    x_no_pay = True
                    continue
                x_pay -= 1
            elif x_pay == 0:
                pile_collection += 1
                y_hand.extend(pile) #check
                default()
                turn = 1
                pile = []
                x_pay = -1
                continue
        turn = 1
    if turn == 1:
        if y_deals:
            if y_no_pay:
                card = y_hand.pop(0)
                pile.append(card)
                if return_pay(card) > 0:
                    x_deals = True
                    y_deals = False
                    x_pay = return_pay(card)
                    x_no_pay = False
            if y_pay > 0:
                card = y_hand.pop(0)
                pile.append(card)
                if return_pay(card) > 0:
                    x_deals = True
                    y_deals = False
                    x_pay = return_pay(card)
                    x_no_pay = False
                    y_pay = -1
                    y_no_pay = True
                    continue
                y_pay -= 1
            elif y_pay == 0:
                pile_collection += 1
                x_hand.extend(pile) #check later
                default()
                pile = []
                turn = 0
                y_pay = -1
                continue
        turn = 0