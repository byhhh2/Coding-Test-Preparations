def solution(ings, menu, sell):
    answer = 0
    dict_ings = {}
    dict_menu = {}
    total_ings_price = 0

    for i in ings:
        name, price = i.split()
        dict_ings[name] = int(price)

    for m in menu:
        total_ings_price = 0
        name, minus, plus = m.split()

        for _ in minus:
            total_ings_price += dict_ings[_]

        dict_menu[name] = int(plus) - total_ings_price


    for s in sell:
        name, cnt = s.split()
        answer += dict_menu[name] * int(cnt)

    return answer


print(solution(["r 10", "a 23", "t 124", "k 9"], ["PIZZA arraak 145", "HAMBURGER tkar 180", "BREAD kkk 30", "ICECREAM rar 50", "SHAVEDICE rar 45", "JUICE rra 55", "WATER a 20"], ["BREAD 5", "ICECREAM 100", "PIZZA 7", "JUICE 10", "WATER 1"]))

print(solution())