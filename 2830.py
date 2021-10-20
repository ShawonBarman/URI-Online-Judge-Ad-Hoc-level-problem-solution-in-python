l = int(input())
k = int(input())
if l > k:
    tmp = l
    l = k
    k = tmp
if (l >= 1 and l <= 8) and (k >= 9 and k <= 16):
    print("final")
elif ((l >= 1 and l <= 4) and (k >= 5 and k <= 8)) or ((l >= 9 and l <= 12) and (k >= 13 and k <= 16)):
    print("semifinal")
elif ((l==1 or l==2) and (k==3 or k==4)) or ((l==5 or l==6) and (k==7 or k==8)) or ((l==9 or l==10) and (k==11 or k==12)) or ((l==13 or l==14) and (k==15 or k==16)):
    print("quartas")
else:
    print("oitavas")