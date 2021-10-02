cv, ce, cs, fv, fe, fs = map(int, input().split())
total_point_C = (cv*3)+(ce*1)
total_point_F = (fv*3)+(fe*1)
if total_point_C == total_point_F and cs == fs:
    print("=")
elif (total_point_C > total_point_F) or (total_point_C == total_point_F and cs > fs):
    print("C")
else:
    print("F")