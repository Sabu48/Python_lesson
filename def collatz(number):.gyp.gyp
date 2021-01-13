def collatz(number):
    if number % 2 == 0:
        return number / 2
    else:
        return 3 * number + 1

print("整数を入力してください")
input_number = int(input())
while  input_number > 1:
    input_number = collatz(input_number)
    print(input_number)
print("終わり")