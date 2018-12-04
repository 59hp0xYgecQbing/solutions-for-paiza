# coding: utf-8

pokers = ['3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2']
rules = {}
for i, _p in enumerate(pokers):
    rules[_p] = i

values = input().strip().split(' ')
players = [x for x in values]
orders = [-1 for _ in range(52)]
field_card = None
cur_ptr = 0
cur_order = 1
while cur_order <= 52:
    for i in range(52):
        if players[i] == None:
            if cur_ptr == i:
                players[i] = None
                field_card = None
        else:
            if field_card == None:
                field_card = players[i]
                players[i] = None
                orders[i] = cur_order
                cur_order += 1
                cur_ptr = i
            else:
                if rules[field_card] < rules[players[i]]:
                    field_card = players[i]
                    players[i] = None
                    orders[i] = cur_order
                    cur_order += 1
                    cur_ptr = i
                else:
                    pass

for i in orders:
    print(i)                

