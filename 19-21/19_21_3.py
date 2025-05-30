# Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежат две кучи камней. 
# Игроки ходят по очереди, первый ход делает Петя. 
# За один ход игрок может добавить в большую кучу любое количество камней от одного до трёх или удвоить количество камней в меньшей куче. 
# Если кучи содержат равное количество камней, можно добавить в любую из них от одного до трёх камней, удвоение в этой ситуации запрещено.
# Игра завершается, когда общее количество камней в кучах становится более 40. 
# Победителем считается игрок, сделавший последний ход, то есть первым получивший 41 или больше камней в двух кучах.

# 1)Известно, что Петя смог выиграть первым ходом. Какое наименьшее число камней могло быть суммарно в двух кучах?

# 2) В начальный момент в первой куче было 5 камней, а во второй  — S камней, 1 ≤ S ≤ 35.
# Укажите минимальное и максимальное из таких значений S, при которых Петя не может выиграть первым ходом, 
# но у Пети есть выигрышная стратегия, позволяющая ему выиграть вторым ходом при любой игре Вани.
# В ответе запишите сначала минимальное значение, затем максимальное.

# 3) В игре, описанной в задании 19, в начальный момент в первой куче было 17 камней, а во второй  — S камней, 1 ≤ S ≤ 23.
# Найдите такое значение S, при котором у Вани есть стратегия, позволяющая ему выиграть вторым ходом при любой игре Пети, 
# но у Вани нет стратегии, которая позволяла бы ему гарантированно выиграть первым ходом.

# 2 кучи в большую +1 +2 +3 в меньшей *2 если кучи равны *2 нельзя 
# победа сум>40 
def w1(a,b):
    if a>b:
        return a+3+b>=41 or b*2+a>=41
    if a<b:
        return a+3+b>=41 or a*2+b>=41
    if a==b:
        return a+3+b>=41

def w2(a,b):
    if a>b:
        return w1(a+1,b) and w1(a+2,b) and w1(a+3,b) and w1(a,2*b) and not(w1(a,b))
    if a<b:
        return w1(a,b+1) and w1(a,b+2) and w1(a,b+3) and w1(a*2,b) and not(w1(a,b))
    if a==b:
        return w1(a+1,b) and w1(a+2,b) and w1(a+3,b) and not(w1(a,b))

def w3(a,b):
    if a>b:
        return w2(a+1,b) or w2(a+2,b) or w2(a+3,b) or w2(a,2*b)
    if a<b:
        return w2(a,b+1) or w2(a,b+2) or w2(a,b+3) or w2(a*2,b)
    if a==b:
        return w2(a+1,b) or w2(a+2,b) or w2(a+3,b)

def w4(a,b):
    if a>b:
        return (w3() or w3()) and (w3(a+1,b) or w1(a+1,b)) and w3(a+2,b) and w3(a+3,b) and w3(a,2*b)
    if a<b:
        return w2(a,b+1) or w2(a,b+2) or w2(a,b+3) or w2(a*2,b)
    if a==b:
        return w2(a+1,b) or w2(a+2,b) or w2(a+3,b)        


c=100000
for a in range(1,41):
    for b in range(1,41):
        if w1(a,b)==1:
            if a+b<c:
                c=a+b
print(c)

for a in range(1,36):
    if w3(a,5)==1:
        print(a)
