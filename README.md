# Student-Helper
Code made to assist students with scheduling as well as practice


#### Video Demo:  https://youtu.be/YFO3g3qUHRQ
#### Description: My code is a student helper, I made it with the intension of helping students. When I was doing my A-levels one year ago, I remember often switching between multiple apps and websites for different subjects, for example when I had first started computer science I often Had trouble with converting decimal to binary( and hexa) and vice versa this meant that I was often looking through many websites and notes just to check that the number I found was correct and sometimes when I looked back at those notes I had no idea how I even got the answer. I also remember during my English Language I was often looking for new synonyms and words to make my essays better. at home I would spend 10, maybe 15 minutes just making my own version of a pomodoro timer and writing it all down in a notebook. looking back now these things used to waste a lot of my time, that could have been used in a better way, I present to you the "Student Helper" This Program allows you to do every one of those things, and more! When planning out what I was going to do for this project I had a lot of small ideas, and in order to make this project useful I chose to combine them all (after each file was individually made, I pasted all the functions into project.py). I started off by planning out what I would do and when. so, I first made convert.py, which you will find in the source_files folder, convert.py allowed you to Convert Decimal to Binary, Binary to Decimal, Decimal to Hexadecimal, and finally Hexadecimal to decimal. I then moved each of the functions into project.py and added argparse so the user could easily access them (Please Read the How to Use ____ below to see the how to access these features.). I then did a lot of research and wrote eng_dict.py (can be found in source_files folder), this feature would take a word in the English Oxford Dictionary and give the definition, an example, some synonyms, and even some antonyms, I then moved all the functions into the project.py file and added them to the argparse. That same day I also created test_project.py which would test all the functions I've Made so far (and any I make in the future). As I didn’t have much time left in that day, I choose to also make a game of Rock Paper Scissors as an easter egg (not as hidden anymore) that anyone could use to play a simple 1 round game. The next day I decided to finish off all the coding of this project, so I made the final Pomodoro Planner, This function took in the start time as the arg and then also asked for a couple more details(written in the How to Use ___ for the pomodoro planner), it would then print the start and stop times of your breaks which you could use as you please. and finally, I wrote a roman number converter. now I know that this function is not really useful to students, but I wrote this in more of a sentimental manner or to be a test for myself. The whole reason I started CS50P was because I one day choose to open leet code and saw a question asking for a roman number convertor, and despite learning the basics of python in the past I just couldn't do it, that’s when I realised, I needed change, I also felt like this would be a meaningful end to the journey this very function put me on.

#### TLDR: Please Read the below how to use --- for the function or do "python project.py -h(/--help)" for a short guide on how each function works. If needed All the source files, the functions were originally written in are in source_files.

##### How To Use Decimal to Binary: In order to use the "Decimal to Binary" use "python project.py -db int (base 10 value), and it will return to you A step by step process showing how they got that binary number. it will also raise a ValueError if the inputted number is negative (non- two's complement), and if the inputted argument is not an int, a short usage explanation will appear, the binary number can be up to any number of digits. This feature has 2 functions, for testing, one that simply returns the value ("dec_to_binary (num: int)"), and another(format_db) that takes the number and prints out an explanation.

##### How To Use Binary to Decimal: In order to use "Binary to Decimal" use "python project.py -bd str (a single string of binary digits)", it will return a short explanation at the start followed by the working used to find the decimal value. If a char other then 0 and 1 are inputted a ValueError will be raised, if multiple strings are inputted argparse will return an error. if less than 1 char is inputted or value is negative (program does not support two's compliment binary numbers) a ValueError will be raised. The number inputted has no upper limit. This feature has 2 functions, for testing, one that simply returns the value ("binary_to_dec (binary: str)"), and another(format_bd) that takes the number and prints out an explanation.

##### How To Use Decimal to Hexadecimal: In order to use "Decimal to Hexadecimal" use "python project.py -dh int (Base 10 Value)', it will return a short explanation at the start followed by the step by step working used to find the Hexadecimal value. If something other than an integer is inputted a ValueError will be raised, if a negative value is inputted an error will be raised by argparse. There is no Upper limit to the value Inputted. This feature has 2 functions, for testing, one that simply returns the value ("dec_to_hexa (num: int)"), and another(format_dh) that takes the number and prints out an explanation.

##### How To Use Hexadecimal to Decimal:  In order to use "Hexadecimal to Decimal" use "python project.py -hd str (Base 16 Hexadecimal Value)', it will return a short explanation at the start followed by the step by step working used to find the decimal value. If something other than hexadecimal chars(0-9A-F) are inputted (e.g., G) a ValueError will be raised. if a negative Value or multiple values are inputted an error will be raised by argparse. There is no upper limit to the Hexadecimal Value Inputted. This feature has 2 functions, for testing, one that simply returns the value ("hexa_to_dec (string: str)"), and another(format_hd) that takes the number and prints out an explanation.

#### English dictionary, that takes an input word (via -dict word) and prints the definition, example synonyms and antonyms of that word, all of which are taken from the official Oxford Dictionary API. please look at the How to use below which will explain how to use this feature

##### How To Use the Inbuilt English Dictionary: "python project.py -dict str (word to search)". If the inputted word exists and is a part of the oxford dictionary, a definition followed by an example of the word used in a sentence, some synonyms (if there are any), and finally some antonyms (if there are any). The word searched must be a part of the Oxford dictionary, if the word is not found, or does not have a definition a ValueError will be raised. If the word has no synonyms and Antonyms (e.g., hello), A ValueError will be raised (by internal function get_json) and will be handled by the function. if the function has synonyms but no antonyms (e.g., "example") it will be handled by the function and the user will be told by an output. Technical: This Function("dictionary(word_id: str)") has 4 internal functions("get_json(word_id: str)","get_definition(word_id: str)","get_synonyms(jres: dict)","get_antonyms(jres: dict)") each of these functions do something and the main function handles the outputs, The main function tends to take 10 seconds for the output, mainly due to the API taking time to process requests(sadly) and because of this you might see the definition appear first and then the rest.

#### Pomodoro Planner, this is something I felt would be useful to a student as I often used to plan out Pomodoro's manually in a notebook, and I felt like it used to waste a lot of time

##### How to Use the Pomodoro Planner: "python project.py -pomo str (24hour start time, HH:MM)", it then asks for number of Pomodoro’s till long break along How long each pomodoro be, short and long break should be (all in min). It then outputs when each break starts at and ends from the start time you inputted, till the end of the long break. if the start time inputted is not in the correct format or a valid time, a ValueError will be raised. if any of the other inputs (no. of Pomodoro’s, long, short, length) are not int's a ValueError will be raised. Technical: This feature consists of 2 functions (get_times (current: str, pom: int), and format_time (argtimes: list)) get_times simply finds the times at which each break starts and ends, while format_time is responsible for printing(returning) the statements.

#### Roman Number converter's, these are written as a personal test and may not be as useful to students, but I felt like it should be included in this project.

##### How to Use Roman Number to int Converter: “python project.py -ri str (Roman Number)", and it will output a phrase with a translation of that roman number. If the inputted Value isn't a roman number, a ValueError will be raised. There is no upper limit. Technical: There is only 1 function (rom_int(num: str)) to collect the value, and the printing is managed by the main function.

##### How to use Int to Roman Number Converter: “python project.py -ir int (Number to convert)", it will return a roman number and a short explanation, if something other than an int is inputted an error will be raised. There is no upper limit, and any positive integer number can be used. If multiple arguments are inputted an error will be raised. Technical: There is only 1 function (int_rom(num: int)) to collect the value, the printing is managed entirely by the main function.


