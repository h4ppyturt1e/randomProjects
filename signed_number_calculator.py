from base_converter import manual_convert_to_base_n as convert_base
from base_converter import num_to_dec as to_dec


def binary_addition():
    num1 = input("Enter first binary number: ")
    num2 = input("Enter second binary number: ")
    bits = len(num1)
    largest_bit = 2 ** (bits-1)
    try:
        if num1[0] == "1":
            num1 = to_dec(num1[1:], 2) - largest_bit
        else:
            num1 = to_dec(num1[1:], 2)
        if num2[0] == "1":
            num2 = to_dec(num2[1:], 2) - largest_bit
        else:
            num2 = to_dec(num2[1:], 2)
    except IndexError:
        print("Invalid input, try again.\n")
        binary_addition()
    total = num1 + num2
    print(num1, num2, total)
    if int(total) >= largest_bit:
        print(total, "is greater than", largest_bit, ", Incorrect sum.")
    else:
        new_total = convert_base(str(abs(total)), 10, 2)
        while len(new_total) != bits:
            new_total = "0" + new_total
        print(new_total)
        if new_total[0] == "1":
            new_new_total = []
            for i in range(bits):
                if new_total[i] == "1":
                    new_new_total.append("0")
                else:
                    new_new_total.append("1")
            total_cache = convert_base(str(to_dec(''.join(new_new_total), 2) + 1), 10, 2)
        else:
            total_cache = new_total
        print("Answer:", total_cache)


if __name__ == "__main__":
    print()
    while True:
        binary_addition()
