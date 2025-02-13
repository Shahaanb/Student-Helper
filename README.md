# Student Helper
Student Helper is a program designed to assist students with various tasks. 
## Video Demo
[Watch Here](https://youtu.be/YFO3g3qUHRQ)

## History
When I was doing my A-levels some time ago, I often had to switch between multiple apps and websites for different subjects. For example, when I first started Computer Science, I struggled with converting decimal to binary (and hexadecimal) and vice versa. This meant constantly looking through multiple websites and notes just to verify my answers. Sometimes, when I looked back at those notes, I had no idea how I even got the answer.

Similarly, during my English Language studies, I frequently searched for new synonyms and words to improve my essays. At home, I would spend 10 to 15 minutes manually planning out a Pomodoro timer and writing it all down in a notebook. Looking back, these small inefficiencies wasted a lot of time that could have been better utilized.

To solve these problems, I created "Student Helper," a program that consolidates all these tools into one. Each feature was initially developed in a separate file before being integrated into `project.py` with argparse for easy access.

## Features

### 1. **Number Conversions**
#### Decimal to Binary
```
python project.py -db <integer>
```
- Converts a decimal number to binary with a step-by-step explanation.
- Raises a `ValueError` if a negative number is inputted.

#### Binary to Decimal
```
python project.py -bd <binary_string>
```
- Converts a binary number to decimal with a step-by-step breakdown.
- Raises a `ValueError` if input contains characters other than `0` or `1`.

#### Decimal to Hexadecimal
```
python project.py -dh <integer>
```
- Converts a decimal number to hexadecimal with a detailed explanation.
- Raises a `ValueError` for non-integer or negative inputs.

#### Hexadecimal to Decimal
```
python project.py -hd <hex_string>
```
- Converts a hexadecimal number to decimal with a step-by-step breakdown.
- Raises a `ValueError` if invalid hexadecimal characters are used.

### 2. **English Dictionary**
```
python project.py -dict <word>
```
- Fetches the definition, example sentence, synonyms, and antonyms from the Oxford Dictionary API.
- Raises a `ValueError` if the word is not found.

### 3. **Pomodoro Planner**
```
python project.py -pomo <HH:MM>
```
- Generates a Pomodoro schedule based on user input.
- Asks for:
  - Number of Pomodoros before a long break
  - Duration of each Pomodoro (in minutes)
  - Short break duration
  - Long break duration
- Outputs start and stop times for each break.
- Raises a `ValueError` for incorrect time formats or invalid inputs.

### 4. **Roman Numeral Converters**
#### Roman to Integer
```
python project.py -ri <roman_numeral>
```
- Converts a Roman numeral to an integer.
- Raises a `ValueError` if input is not a valid Roman numeral.

#### Integer to Roman
```
python project.py -ir <integer>
```
- Converts an integer to a Roman numeral with an explanation.
- Only accepts positive integers.

### 5. **Rock Paper Scissors (Easter Egg)**
- A simple one-round game for fun.

## Testing
- `test_project.py` contains tests for all functions.

## Installation
1. Clone the repository:
   ```
   git clone <repository_url>
   cd student-helper
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the program:
   ```
   python project.py -h
   ```

## Notes
- All original source files (`convert.py`, `eng_dict.py`, etc.) are in the `source_files` folder.
- The program uses `argparse` for command-line arguments.
- The dictionary feature relies on the Oxford Dictionary API and may have a delay in response.


## Source Files  

The `Initial_Scripts` folder contains the original scripts used to develop **Student Helper**. Each feature was initially implemented and tested in separate files before being combined into `helper.py`. These files serve as a reference for understanding the core functionality of each feature.  

For a detailed breakdown of the files in this folder, refer to the [Source Files README](Initial_Scripts/README.md).  

---
This project was inspired by my personal struggles during A-levels. I created it to make student life easier by consolidating essential tools into one program.

