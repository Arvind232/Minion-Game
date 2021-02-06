def minion_game(string):
    player_1 = 0
    player_2 = 0
    String_Len = len(string)
    for i in range(String_Len):
        if string[i] in "AEIOU":
            player_1 += (String_Len) - i
        else :
            player_2 += (String_Len) - i
    if player_1 > player_2:
        print("Kevin", player_1)
    elif player_1 < player_2:
        print("Stuart",player_2)
    elif player_1 == player_2:
        print("Draw")
    else :
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)