#THE STUDENT HELPER
import argparse
import random
import requests


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-bd", "--binarytodec", help="8 digit Binary to Decimal", type=str
    )
    parser.add_argument(
        "-db", "--dectobinary", help="Decimal(upto 255) to Binary", type=int
    )
    parser.add_argument("-dh", "--dectohexa", help="Decimal to HexaDecimal", type=int)
    parser.add_argument("-hd", "--hexatodec", help="HexaDecimal to decimal", type=str)
    parser.add_argument(
        "-dict",
        "--englishDictionary",
        help="Define, examples and synonyms for a word",
        type=str,
    )
    parser.add_argument(
        "-rps", "--rockpapersissors", help="Play Rock Paper Sissors", type=str
    )
    parser.add_argument(
        "-pomo",
        "--pomodoro",
        help="Pomodoro Planner From 24-Hour start time: HH:MM",
        type=str,
    )
    parser.add_argument(
        "-ri", "--Romantoint", help="Roman Number To Integer upto 3999", type=str
    )
    parser.add_argument("-ir", "--InttoRoman", help="IntegerToRoman", type=int)

    args = parser.parse_args()
    if args.binarytodec:
        print(format_bd(args.binarytodec))
    elif args.dectobinary:
        print(format_db(args.dectobinary))
    elif args.dectohexa:
        print(format_dh(args.dectohexa))
    elif args.hexatodec:
        print(format_hd(args.hexatodec))
    elif args.rockpapersissors:
        RockPaperSissors(args.rockpapersissors)
    elif args.englishDictionary:
        dictionary(args.englishDictionary)
    elif args.pomodoro:
        print(*format_time(args.pomodoro), sep="\n")
    elif args.Romantoint:
        print(
            f"Roman Number {args.Romantoint.upper()} is used to show: {rom_int(args.Romantoint)}"
        )
    elif args.InttoRoman:
        print(f"Integer: {args.InttoRoman} becomes Roman: {int_rom(args.InttoRoman)}")
    else:
        print("Argument Required, use -h or --help for more")


# converts (posative) binary Number to A Decimal
def binary_to_dec(binary: str) -> int:
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


# make it look nice for the final output
def format_bd(binary: int) -> str:
    return (
        f"Binary: ({binary}) Base = 2 --> Decimal: ({binary_to_dec(binary)}) Base = 10"
    )


# converts dec to binary
def dec_to_binary(num: int) -> str:
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


# makes that number look fine
def format_db(num: int) -> str:
    return f"Decimal: ({num}) Base = 10 --> Binary: ({dec_to_binary(num)}) Base = 2"


# returns a string that is pleasant to look at
def dec_to_hexa(num: int) -> str:
    if num < 0:
        raise ValueError
    current = int(num)
    hexa = [
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
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


# make it look nice cause testing needs a easy return
def format_dh(num: int) -> str:
    return f"Decimal: ({num}) Base = 10 --> Hexadecimal: ({dec_to_hexa(num)}) Base = 16"


# converts Hexa to Decimal
def hexa_to_dec(string: str) -> int:
    if "-" in string:
        raise ValueError("Only Positive Values Accepted")
    hexa = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15,
    }
    lhexa = list(string.upper())
    print("--------------------------------------------------------------------")
    print("Reverse the HexaDecimal Value then convert each digit to decimal and")
    print("multiply by 16 raised to n, and all the values obtained")
    print("--------------------------------------------------------------------")
    lhexa.reverse()
    total = 0
    for i in range(len(lhexa)):
        try:
            total += int(hexa[lhexa[i]]) * 16**i
        except KeyError:
            raise ValueError("Invalid Char")
        print(
            f"{lhexa[i]}: {hexa[lhexa[i]]} * 16^{i} = {int(hexa[lhexa[i]]) * 16 ** i} +"
        )
    print("---------------------")
    print(f"          {total}")
    return total


# Makes hd look nice for the print
def format_hd(string: str) -> str:
    return f"Hexadecimal: ({string}) Base = 16 --> Decimal: ({hexa_to_dec(string)}) Base = 2"


# Rock OR Paper OR Sissors
def RockPaperSissors(choosen: str):
    choosen = choosen.title().strip()
    options = ["Rock", "Paper", "Sissors"]
    comp = random.choice(options)
    if choosen not in options:
        print("Ah Ha. No cheating, thats not an option")
    elif choosen == comp:
        print("OOO we think the same")
    elif choosen == "Rock":
        if comp == "Sissors":
            print("Oh No, You Won")
        else:
            print("WHOO!! I WON")
    elif choosen == "Sissors":
        if comp == "Rock":
            print("Oh No, You Won")
        else:
            print("WHOO!! I WON")
    elif choosen == "Paper":
        if comp == "Sissors":
            print("Oh No, You Won")
        else:
            print("WHOO!! I WON")


# Calls All the functions that each find a different thing, and prints them all
def dictionary(word_id: str):
    word_id = word_id.replace(" ", "%20")
    define = str(get_definition(word_id))
    print("------------------------------------------")
    print(f'\nThe Definition: "{define}"', end="\n\n")
    try:
        jres = get_json(word_id)
        print(f'Word Used in a sentence: "{get_example(jres)}"', end="\n\n")
    except ValueError:
        print("This Word Has No Example,Synonyms,Antonyms")
    else:
        try:
            get_synonyms(jres)
            print(f"Some synonyms for {word_id} are:", end=' "')
            print(*get_synonyms(jres), sep='" , "', end='" \n\n')
        except ValueError:
            print("This Word Has No Synonyms")
        try:
            get_antonyms(jres)
            print(f"Some antonyms for {word_id} are: ", end='"')
            print(*get_antonyms(jres), sep='" , "', end='" \n\n')
        except ValueError:
            print("This Word Has No Antonyms\n")
        print("------------------------------------------")


# gets a json that contains the synonyms and antonyms from oxford dictionaries website
def get_json(word_id: str):
    # app id and key gotten from making an account on their website(pls act like you dont see it)
    app_id = "39dd753f"
    app_key = "e6ed01b484b0e689fd973232a092da75"
    url = (
        "https://od-api.oxforddictionaries.com/api/v2/thesaurus/en-gb/"
        + word_id.lower().strip()
    )
    responce = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
    jres = responce.json()
    if responce.status_code != 200:
        raise ValueError("This word has no synonyms or antonyms")
    return jres


# gets a second JSON that contains the definition of the word(wasnt in the original one cause
# oxford dictionaries weird)
def get_definition(word_id: str):
    app_id = "39dd753f"
    app_key = "e6ed01b484b0e689fd973232a092da75"
    responce = requests.get(
        "https://od-api.oxforddictionaries.com/api/v2/words/en-gb?q="
        + word_id
        + "&fields=definitions",
        headers={"app_id": app_id, "app_key": app_key},
    )
    if responce.status_code != 200:
        raise ValueError("Word not found")
    jres = responce.json()["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]
    return jres["definitions"][0]


# uses first JSON to find all the synonyms and add them to a list
def get_synonyms(jres: dict) -> list:
    s = jres["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]
    synonyms = []
    try:
        s["synonyms"]
    except KeyError:
        raise ValueError("This Word Has No Synonyms")
    for result in s["synonyms"]:
        synonyms.append(result["text"])
    return synonyms


# uses the first JSON to find antonyms and add them a list
def get_antonyms(jres: dict) -> list:
    s = jres["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]
    antonyms = []
    try:
        s["antonyms"]
    except KeyError:
        raise ValueError("There are no antonyms for this word")
    for result in s["antonyms"]:
        antonyms.append(result["text"])
    return antonyms


# uses the first JSON to get a example use of the word
def get_example(jres: dict) -> str:
    s = jres["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]
    example = s["examples"][0]["text"]
    return example


def format_time(argtimes: list) -> list:
    i = int(input("Number of Pomodoro's Till Long Break: "))
    times = get_times(argtimes, i)
    tm = []
    tm.append(f"Your Work Starts at {argtimes}")
    for time in times:
        if i != 0:
            tm.append(
                f"Your Break Starts at {time['break']} and ends at {time['restart']}"
            )
            i -= 1
        else:
            tm.append(
                f"Your Long Break starts at {time['break']} and ends at {time['restart']}"
            )
    return tm


def get_times(current: str, pom: int) -> list:
    hour, min = current.strip().split(":")
    min = int(min)
    hour = int(hour)
    if hour >= 24 or min >= 60:
        raise ValueError("INVALID Time")
    work = int(input("Work For: "))
    srt_break = int(input("Short Break: "))
    lng_break = int(input("Long Break: "))
    brktme = []
    restarttm = []
    for _ in range(pom):
        if (work + min) >= 60:
            min = (work + min) - 60
            hour += 1
            if hour == 24:
                hour = 00
            brktme.append(f"{hour:02}:{min:02}")
        else:
            min = work + min
            brktme.append(f"{hour:02}:{min:02}")
        if (min + srt_break) >= 60:
            min = (min + srt_break) - 60
            hour += 1
            if hour == 24:
                hour = 0
            restarttm.append(f"{hour:02}:{min:02}")
        else:
            min = min + srt_break
            restarttm.append(f"{hour:02}:{min:02}")

    if (work + min) >= 60:
        min = (work + min) - 60
        hour += 1
        if hour == 24:
            hour = 00
        brktme.append(f"{hour:02}:{min:02}")
    else:
        min = work + min
        brktme.append(f"{hour:02}:{min:02}")

    if (min + lng_break) >= 60:
        min = (min + lng_break) - 60
        hour += 1
        if hour == 24:
            hour = 0
        restarttm.append(f"{hour:02}:{min:02}")
    else:
        min = min + lng_break
        restarttm.append(f"{hour:02}:{min:02}")
    times = [{"break": brktme[i], "restart": restarttm[i]} for i in range(len(brktme))]
    return times


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
    num = list(num.upper())
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


def int_rom(num: int):
    int(num)
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
    syms = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
    syms.reverse()
    r = []
    while num != 0:
        for sym in syms:
            if num >= roma[sym]:
                num -= roma[sym]
                r.append(sym)
                break
    return "".join(r)


if __name__ == "__main__":
    main()
