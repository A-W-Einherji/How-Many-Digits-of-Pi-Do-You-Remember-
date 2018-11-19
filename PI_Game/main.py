Digits_Of_Pi = open(r"Digits_Of_Pi.txt", "r+")

str_Digits_of_Pi = Digits_Of_Pi.readline()

index = 0
correct_digits = ''

for i in str_Digits_of_Pi:
    submitted_digit = str(input("Enter the next digit of pi: "))
    if submitted_digit == str_Digits_of_Pi[index]:
        index += 1
        correct_digits += submitted_digit
    else:
        break

next_three_digits = str_Digits_of_Pi[index] + str_Digits_of_Pi[index + 1] + str_Digits_of_Pi[index + 2]

if len(correct_digits) > 1:
    display_digits = correct_digits[0] + '.' + correct_digits[1:]
elif len(correct_digits) == 1:
    display_digits = correct_digits
else:
    display_digits = "NONE"
    next_three_digits = "3.14"

print("")
print("GAME OVER....")
print("The digits you correctly entered were: " + display_digits)
print("The next three digits were: " + next_three_digits)
print("So you entered, " + str(len(correct_digits)) + " correct digit(s)!")

Digits_Of_Pi.close()
