def int_rom(num: int):
    roma = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
    "IV": 4,
    "IX": 9,
    "XL": 40,
    "XC": 90,
    "CD": 400,
    "CM": 900,
    }
    syms = ["I", "IV", "V", "IX", "X", "XL","L", "XC", "C", "CD", "D", "CM", "M"]
    syms.reverse()
    r = []
    while num != 0:
        for sym in syms:
            if num >= roma[sym]:
                num -= roma[sym]
                r.append(sym)
                break
    return "".join(r)


def rom_int(num: str):
    romanvalues = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    num = list(num)
    value = 0
    for i in range(len(num)):
        if i == len(num) - 1:
            value += romanvalues[num[i]]
            return value
        try:
            s1 = romanvalues[num[i]]
            s2 = romanvalues[num[i + 1]]
        except KeyError:
            raise ValueError("That is Not A Roman Number")
        if s1 >= s2:
            value += romanvalues[num[i]]
        else:
            value -= romanvalues[num[i]]
    return value


roma = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
    "IV": 4,
    "IX": 9,
    "XL": 40,
    "XC": 90,
    "CD": 400,
    "CM": 900,
}
num = 3549  # input("Roman: ")
print(int_rom(num))
