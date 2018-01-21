gt = input()

hh, mm, ss = gt[0:8].split(":")

if gt[8:10] == "AM":
    if hh == "12" and mm == "00" and ss == "00":
        mt = "00:00:00"
    elif hh == "12":
        mt = "00:" + mm + ":" + ss
    else:
        mt = hh + ":" + mm + ":" + ss
else:
    if hh == "12" and mm == "00" and ss == "00":
        mt = "12:00:00"
    elif hh == "12":
        mt = "12:" + mm + ":" + ss
    else:
        hh = int(hh)
        hh += 12
        mt = str(hh) + ":" + mm + ":" + ss

print(mt)


