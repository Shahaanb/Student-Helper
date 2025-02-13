import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-bd", "--binarytodec", help="8 digit binary to decimal", type=str)
    parser.add_argument("-db", "--dectobinary", help="decimal(upto 255) to binary", type=str)
    parser.add_argument("-dh", "--dectohexa", help="decimal to HexaDecimal", type=str)
    parser.add_argument("-hd", "--hexatodec", help="HexaDecimal to decimal", type=str)
    args = parser.parse_args()
    if args.binarytodec:
        print(format_bd(args.binarytodec))
    elif args.dectobinary:
        print(format_db(args.dectobinary))
    elif args.dectohexa:
        print(format_dh(args.dectohexa))
    elif args.hexatodec:
        print(format_hd(args.hexatodec))
    else:
        print("Argument Required, use -h or --help for more")

def binary_to_dec(binary: str)-> int:
    if set(binary) == {"0", "1"} or set(binary) == {"0"} or set(binary) == {"1"}:
        pass
    else:
        raise ValueError("Must be Binary")
    lbinary = list(binary)
    total = 0
    if len(lbinary) < 1:
        raise ValueError("binary must be atleast 1 digit")
    lbinary.reverse()
    print("-------------------------------------------------------------------------")
    print("Reverse the Binary and multiply by 2 raised to the power of the current n")
    print("and add all the values obtained")
    print("-------------------------------------------------------------------------")
    for i in range(len(lbinary)):
        total += int(lbinary[i]) * 2**i
        print(f"{lbinary[i]} * 2^{i} = {int(lbinary[i]) * 2 ** i} +")
    print("-------------")
    print(f"        {total}")
    return total


def format_bd(binary: int) -> str:
    return f"Binary: ({binary}) Base = 2 --> Decimal: ({binary_to_dec(binary)}) Base = 10"


def dec_to_binary(num: str) -> str:
    num = int(num)
    if num < 0:
        raise ValueError("Must Be Positive")
    current = int(num)
    binary = []
    print("------------------------------------------")
    print("Divide by 2 till 0 and note the remainders")
    print("------------------------------------------")
    while True:
        rem = current % 2
        print(f"{current} / 2 | {rem}")
        current = int(current / 2)
        binary.append(rem)
        if current == 0:
            break
    print("<-------   reverse the remainders")
    print(*binary, "   to get the final answer", sep="")
    binary.reverse()
    final = int("".join([str(e) for e in binary]))
    return f"{final:04}"


def format_db(num: int) -> str:
    return f"Decimal: ({num}) Base = 10 --> Binary: ({dec_to_binary(num)}) Base = 2"


def dec_to_hexa(num: str) -> str:
    num = int(num)
    if num < 0:
        raise ValueError
    current = int(num)
    hexa = [
        "0", "1", "2", "3", "4", "5", "6",
        "7", "8", "9", "A", "B", "C", "D",
        "E", "F",
    ]
    final = []
    print("-----------------------------------------------------------------------")
    print("Divide by 16 till it reached 0, and take note of the remainders")
    print("Convert any remainders over 9 into their letters[A-F] eg 10 = A, 15 = F")
    print("-----------------------------------------------------------------------")
    while True:
        rem = current % 16
        print(f"{current} / 16 | {rem}")
        current = int(current / 16)
        final.append(hexa[rem])
        if current == 0:
            break
    print("<------ reverse the remainders")
    print(*final, sep="")
    final.reverse()
    final = "".join(str(i) for i in final)
    return final


def format_dh(num: int) -> str:
    return f"Decimal: ({num}) Base = 10 --> Hexadecimal: ({dec_to_hexa(num)}) Base = 16"


def hexa_to_dec(string: str):
    if "-" in string:
        raise ValueError("Only Positive Values Accepted")
    hexa = {
        "0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
        "9": 9, "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15,
    }
    lhexa = list(string.upper())
    print("--------------------------------------------------------------------")
    print("Reverse the HexaDecimal Value then convert each digit to decimal and")
    print("multiply by 16 raised to n, and all the values obtained")
    print("--------------------------------------------------------------------")
    lhexa.reverse()
    total = 0
    for i in range(len(lhexa)):
        total += int(hexa[lhexa[i]]) * 16**i
        print(
            f"{lhexa[i]}: {hexa[lhexa[i]]} * 16^{i} = {int(hexa[lhexa[i]]) * 16 ** i} +"
        )
    print("---------------------")
    print(f"          {total}")
    return total


def format_hd(string: str) -> str:
    return f"Hexadecimal: ({string}) Base = 16 --> Decimal: ({hexa_to_dec(string)}) Base = 2"


if __name__ == "__main__":
    main()