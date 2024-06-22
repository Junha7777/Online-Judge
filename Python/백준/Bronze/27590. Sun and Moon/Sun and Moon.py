ds, ys = map(int, input().split())
dm, ym = map(int, input().split())
sy = ys - ds
my = ym - dm

while sy != my :
    if sy < my :
        sy += ys
    else : my += ym
print(sy)