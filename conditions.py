def end_of_string(string,i):
    if (i >= len(string)):
        return True
    else:
        return False


A_id1 = []
A_id2 = []
A_id3 = []
A_id4 = []
A_cel = []
B1 = []
B2 = []
B3 = []

def S0(string, i):
    global A_id1
    global A_id2
    global A_id3
    global A_id4
    global A_cel
    global B1
    global B2
    global B3
    A_id1.clear()
    A_id2.clear()
    A_id3.clear()
    A_id4.clear()
    A_cel.clear()
    B1.clear()
    B2.clear()
    B3.clear()

    if end_of_string(string,i):
        return

    elif string[i].isalpha():
        S1(string, i)

    elif string[i] == '0':
        S9(string, i)

    elif string[i].isdigit():
        S11(string, i)

    else:
        S0(string, i)

def S1(string, i):
    global A_id1
    global A_id2
    global A_id3
    global A_id4
    global A_cel
    global B1
    global B2
    global B3

    A_id1.append(string[i])
    i+=1

    if end_of_string(string,i):
        return

    elif string[i].isalpha():
        S2(string, i)

    elif string[i] == '0':
        S23(string, i)

    elif string[i].isdigit():
        S24(string, i)

    else:
        S0(string, i)

def S2(string, i):
    global A_id1
    global A_id2
    global A_id3
    global A_id4
    global A_cel
    global B1
    global B2
    global B3

    A_id2.append(string[i])
    i+=1

    if end_of_string(string,i):
        return

    elif string[i].isalpha():
        S3(string, i)

    elif string[i] == '0':
        S4(string, i)

    elif string[i].isdigit():
        S5(string, i)

    else:
        S0(string, i)

def S3(string, i):
    global A_id1
    global A_id2
    global A_id3
    global A_id4
    global A_cel
    global B1
    global B2
    global B3

    A_id1 = A_id2.copy()
    A_id2.clear()
    A_id2.append(string[i])
    i+=1

    if end_of_string(string,i):
        return

    elif string[i].isalpha():
        S3(string, i)

    elif string[i] == '0':
        S4(string, i)

    elif string[i].isdigit():
        S5(string, i)

    else:
        S0(string, i)

def S4(string, i):
    global A_id1
    global A_id2
    global A_id3
    global A_id4
    global A_cel
    global B1
    global B2
    global B3

    A_id3.append(string[i])
    A_cel.append(string[i])
    i+=1

    if end_of_string(string,i):
        return

    elif string[i].isalpha():
        S25(string, i)

    elif string[i] == '.':
        S26(string, i)

    elif string[i] == '0':
        S6(string, i)

    elif string[i].isdigit():
        S7(string, i)

    else:
        S0(string, i)

def S5(string, i):
    global A_id1
    global A_id2
    global A_id3
    global A_id4
    global A_cel
    global B1
    global B2
    global B3

    A_id3.append(string[i])
    A_cel.append(string[i])
    i+=1

    if end_of_string(string,i):
        return

    elif string[i].isalpha():
        S25(string, i)

    elif string[i] == '.':
        S26(string, i)

    elif string[i] == '0':
        S8(string, i)

    elif string[i].isdigit():
        S8(string, i)

    else:
        S0(string, i)


def S6(string, i):
    global A_id1
    global A_id2
    global A_id3
    global A_id4
    global A_cel
    global B1
    global B2
    global B3

    A_id4.append(string[i])
    print(''.join(map(str, A_id1)), end='')
    print(''.join(map(str, A_id2)), end='')
    print(''.join(map(str, A_id3)), end='')
    print(''.join(map(str, A_id4)), end=' ')
    A_id1.clear()
    A_id2.clear()
    A_id3.clear()
    A_id4.clear()
    i += 1

    if end_of_string(string, i):
        return

    elif string[i].isalpha():
        S27(string, i)

    elif string[i] == '.':
        S12(string, i)

    elif string[i] == '0':
        S9(string, i)

    elif string[i].isdigit():
        S10(string, i)

    else:
        S0(string, i)

def S7(string, i):
    global A_id1
    global A_id2
    global A_id3
    global A_id4
    global A_cel
    global B1
    global B2
    global B3

    A_id4.append(string[i])
    print(''.join(map(str, A_id1)), end='')
    print(''.join(map(str, A_id2)), end='')
    print(''.join(map(str, A_id3)), end='')
    print(''.join(map(str, A_id4)), end=' ')
    A_id1.clear()
    A_id2.clear()
    A_id3.clear()
    A_id4.clear()

    A_cel.clear()
    A_cel.append(string[i])
    i += 1

    if end_of_string(string, i):
        return

    elif string[i].isalpha():
        S27(string, i)

    elif string[i] == '.':
        S12(string, i)

    elif string[i] == '0':
        S11(string, i)

    elif string[i].isdigit():
        S11(string, i)

    else:
        S0(string, i)


def S8(string, i):
    global A_id1
    global A_id2
    global A_id3
    global A_id4
    global A_cel
    global B1
    global B2
    global B3

    A_id4.append(string[i])
    print(''.join(map(str, A_id1)), end='')
    print(''.join(map(str, A_id2)), end='')
    print(''.join(map(str, A_id3)), end='')
    print(''.join(map(str, A_id4)), end=' ')
    A_id1.clear()
    A_id2.clear()
    A_id3.clear()
    A_id4.clear()

    A_cel.append(string[i])
    i += 1

    if end_of_string(string, i):
        return

    elif string[i].isalpha():
        S27(string, i)

    elif string[i] == '.':
        S12(string, i)

    elif string[i] == '0':
        S11(string, i)

    elif string[i].isdigit():
        S11(string, i)

    else:
        S0(string, i)

def S9(string, i):
    global A_id1
    global A_id2
    global A_id3
    global A_id4
    global A_cel
    global B1
    global B2
    global B3

    A_cel.clear()
    A_cel.append(string[i])
    i += 1

    if end_of_string(string, i):
        return

    elif string[i].isalpha():
        S27(string, i)

    elif string[i] == '.':
        S12(string, i)

    elif string[i] == '0':
        S9(string, i)

    elif string[i].isdigit():
        S10(string, i)

    else:
        S0(string, i)

def S10(string, i):
    global A_id1
    global A_id2
    global A_id3
    global A_id4
    global A_cel
    global B1
    global B2
    global B3

    A_cel.clear()
    A_cel.append(string[i])
    i += 1

    if end_of_string(string, i):
        return

    elif string[i].isalpha():
        S27(string, i)

    elif string[i] == '.':
        S12(string, i)

    elif string[i] == '0':
        S11(string, i)

    elif string[i].isdigit():
        S11(string, i)

    else:
        S0(string, i)

def S11(string, i):
    global A_id1
    global A_id2
    global A_id3
    global A_id4
    global A_cel
    global B1
    global B2
    global B3

    A_cel.append(string[i])
    i += 1

    if end_of_string(string, i):
        return

    elif string[i].isalpha():
        S27(string, i)

    elif string[i] == '.':
        S12(string, i)

    elif string[i] == '0':
        S11(string, i)

    elif string[i].isdigit():
        S11(string, i)

    else:
        S0(string, i)

def S12(string, i):
    global A_id1
    global A_id2
    global A_id3
    global A_id4
    global A_cel
    global B1
    global B2
    global B3

    i += 1

    if end_of_string(string, i):
        return

    elif string[i].isalpha():
        S27(string, i)

    elif string[i] == '0':
        S13(string, i)

    elif string[i].isdigit():
        S14(string, i)

    else:
        S0(string, i)

def S13(string, i):
    global A_id1
    global A_id2
    global A_id3
    global A_id4
    global A_cel
    global B1
    global B2
    global B3

    B1.append(string[i])
    i += 1

    if end_of_string(string, i):
        S19(string,i)
        return

    elif string[i].isalpha():
        S28(string, i)

    elif string[i] == '0':
        S13(string, i)

    elif string[i] == '.':
        S21(string, i)

    elif string[i].isdigit():
        S14(string, i)

    else:
        S17(string, i)

def S14(string, i):
    global A_id1
    global A_id2
    global A_id3
    global A_id4
    global A_cel
    global B1
    global B2
    global B3

    B2.append(string[i])
    i += 1

    if end_of_string(string, i):
        S20(string, i)
        return

    elif string[i].isalpha():
        S29(string, i)

    elif string[i] == '0':
        S15(string, i)

    elif string[i] == '.':
        S22(string, i)

    elif string[i].isdigit():
        S14(string, i)

    else:
        S18(string, i)

def S15(string, i):
    global A_id1
    global A_id2
    global A_id3
    global A_id4
    global A_cel
    global B1
    global B2
    global B3

    B3.append(string[i])
    i += 1

    if end_of_string(string, i):
        S20(string, i)
        return

    elif string[i].isalpha():
        S29(string, i)

    elif string[i] == '0':
        S15(string, i)

    elif string[i] == '.':
        S22(string, i)

    elif string[i].isdigit():
        S16(string, i)

    else:
        S18(string, i)

def S16(string, i):
    global A_id1
    global A_id2
    global A_id3
    global A_id4
    global A_cel
    global B1
    global B2
    global B3

    B2 = (B2 + B3).copy()
    B3.clear()

    S14(string,i)

def S17(string, i):
    global A_id1
    global A_id2
    global A_id3
    global A_id4
    global A_cel
    global B1
    global B2
    global B3

    print(''.join(map(str, A_cel)), end='')
    print(".",end='')
    print("0", end=' ')

    S0(string,i)

def S18(string, i):
    global A_id1
    global A_id2
    global A_id3
    global A_id4
    global A_cel
    global B1
    global B2
    global B3

    print(''.join(map(str, A_cel)), end='')
    print(".",end='')
    print(''.join(map(str, B1)), end='')
    print(''.join(map(str, B2)), end=' ')

    S0(string,i)

def S19(string, i):
    global A_id1
    global A_id2
    global A_id3
    global A_id4
    global A_cel
    global B1
    global B2
    global B3

    print(''.join(map(str, A_cel)), end='')
    print(".",end='')
    print("0", end=' ')

    return

def S20(string, i):
    global A_id1
    global A_id2
    global A_id3
    global A_id4
    global A_cel
    global B1
    global B2
    global B3

    print(''.join(map(str, A_cel)), end='')
    print(".",end='')
    print(''.join(map(str, B1)), end='')
    print(''.join(map(str, B2)), end=' ')

    return

def S21(string, i):
    global A_id1
    global A_id2
    global A_id3
    global A_id4
    global A_cel
    global B1
    global B2
    global B3

    print(''.join(map(str, A_cel)), end='')
    print(".",end='')
    print("0", end=' ')

    A_cel.clear()
    A_cel.append(0)
    B1.clear()

    S12(string,i)

def S22(string, i):
    global A_id1
    global A_id2
    global A_id3
    global A_id4
    global A_cel
    global B1
    global B2
    global B3

    print(''.join(map(str, A_cel)), end='')
    print(".",end='')
    print(''.join(map(str, B1)), end='')
    print(''.join(map(str, B2)), end=' ')

    A_cel.clear()
    A_cel = (B2 + B3).copy()
    B1.clear()
    B2.clear()
    B3.clear()

    S12(string,i)


def S23(string, i):
    global A_id1
    global A_id2
    global A_id3
    global A_id4
    global A_cel
    global B1
    global B2
    global B3

    A_id1.clear()

    S9(string, i)

def S24(string, i):
    global A_id1
    global A_id2
    global A_id3
    global A_id4
    global A_cel
    global B1
    global B2
    global B3

    A_id1.clear()

    S11(string, i)

def S25(string, i):
    global A_id1
    global A_id2
    global A_id3
    global A_id4
    global A_cel
    global B1
    global B2
    global B3

    A_id1.clear()
    A_id2.clear()
    A_id3.clear()
    A_cel.clear()

    S1(string, i)

def S26(string, i):
    global A_id1
    global A_id2
    global A_id3
    global A_id4
    global A_cel
    global B1
    global B2
    global B3

    A_id1.clear()
    A_id2.clear()
    A_id3.clear()

    S12(string, i)

def S27(string, i):
    global A_id1
    global A_id2
    global A_id3
    global A_id4
    global A_cel
    global B1
    global B2
    global B3

    A_cel.clear()

    S1(string, i)

def S28(string, i):
    global A_id1
    global A_id2
    global A_id3
    global A_id4
    global A_cel
    global B1
    global B2
    global B3

    print(''.join(map(str, A_cel)), end='')
    print(".",end='')
    print("0", end=' ')

    A_cel.clear()
    B1.clear()

    S1(string,i)

def S29(string, i):
    global A_id1
    global A_id2
    global A_id3
    global A_id4
    global A_cel
    global B1
    global B2
    global B3

    print(''.join(map(str, A_cel)), end='')
    print(".",end='')
    print(''.join(map(str, B1)), end='')
    print(''.join(map(str, B2)), end=' ')

    A_cel.clear()
    B1.clear()
    B2.clear()
    B3.clear()

    S1(string,i)


