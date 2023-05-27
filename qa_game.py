# n值(0~100)，即最多100人，第一個人開始報數
# 如果只有3個人，只會有一個人報到3，會留下的是2個人，最後報數的同事是報2
# 這個問題應該是想要計算最後報數的同事是第幾順位

def game(n):
    if n==0:
        return "Can't Play"
    people = list(range(n))
    yo = 1 #報數
    current =0  #第一個報數的index
    while len(people)>1:
        if yo %3 == 0:
            del people[current]
        else:
            current = (current+1) % len(people)
        yo += 1
    return "第" + str(people[0]+1) + "順位"  #是要順位，不是要編號


#(Test)如果只有3個人
#print(game(3))

#(Test)如果有100個人
print(game(100))




