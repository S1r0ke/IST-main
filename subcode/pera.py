d1 = (6 ,7 , 8, 9, 10, 11, 12 , 14, 16, 18, 20, 22, 25, 28, 30, 32, 35, 40, 45, 50 ,55, 60, 63 ,70, 71, 80, 90 ,100, 110)
d2 = (19, 24, 38, 42, 48, 53, 56, 65 ,75, 85, 95, 105)
parm = {
    (6,   8):  (2, 2, 0.2,   (8, 20), 1.1, None, 0.9, 0.2, 0.2),
    (8,  10):  (3, 3, 0.2,   (8, 36), 1.7, 0.1, 1.3, 0.1, 0.2),
    (10,  12): (4, 4, 0.4,   (10, 45), 2.4, 0.0, 1.6, None, 0.4),
    (12,  17): (5, 5, 0.4,   (12, 55), 2.9, None, 2.1, 0.2, 0.4),
    (17,  22): (6, 6, 0.4,   (16, 70), 3.5, 0.2, 2.5, 0.1, 0.4),
    (22,  30): (8, 7, 0.4,   (20, 90), 4.1, 0.0, 2.9, None, 0.4),
    (30,  38): (10, 8, 0.6,  (25, 110), 4.7, None, 3.3, None, 0.6),
    (38,  44): (12, 8, 0.6,  (32, 110), 4.9, 0.2, 3.1, 0.4, 0.6),
    (44,  50): (14, 9, 0.6,  (40, 140), 5.5, 0.0, 3.5, 0.2, 0.6),
    (50,  58): (16, 10, 0.6, (45, 180), 6.2, None, 3.8, None, 0.6),
    (58,  65): (18, 11, 0.6, (50, 200), 6.8, 0.2, 4.2, 0.4, 0.6),
    (65,  75): (20, 12, 0.6, (56, 220), 7.4, 0, 4.6, 0.2, 0.6),
    (75,  85): (22, 14, 0.6, (63, 250), 8.5, None, 5.3, None, 0.6),
    (85,  95): (25, 14, 0.6, (70, 280), 8.7, 0.2, 5.5, 0.4, 0.6),
    (95, 110): (28, 16, 1.0, (30, 315), 9.9, 0, 6.1, 0.2, 1),
}

#---------------------------------

def find_parm(prumer):
    keys = parm.keys()
    if prumer in d1 or prumer in d2:
            for key in keys:
                if prumer >= key[0] and prumer < key[1]:
                    if prumer in d2:
                        return (f"d = {prumer}mm\nb = {parm[key][0]}mm\nh = {parm[key][1]}mm\nf = {parm[key][2]}mm\nl = {parm[key][3][0]} až {parm[key][3][1]}mm\nt = {parm[key][4]}mm\nt1 = {parm[key][6]}mm\nRt = {parm[key][-1]}mm\nŘada 2")
                    else:
                        return (f"d = {prumer}mm\nb = {parm[key][0]}mm\nh = {parm[key][1]}mm\nf = {parm[key][2]}mm\nl = {parm[key][3][0]} až {parm[key][3][1]}mm\nt = {parm[key][4]}mm\nt1 = {parm[key][6]}mm\nRt = {parm[key][-1]}mm\nŘada 1")
    else:
        return "Neplatný průměr"