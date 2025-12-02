from math import floor

# from copy import deepcopy


# # %% Part 1

with open("advent_2024/17.txt", "r") as file:
    registers = {x[9]: int(x[12:-1]) for x in file if x.startswith("Register")}

with open("advent_2024/17.txt", "r") as file:
    instructions = [x[9:].split(",") for x in file if x.startswith("Program:")]

instructions = [int(x) for x in instructions[0]]

print(registers)
print(instructions)

output = []


def combo_operand(operand: int) -> int:
    global registers
    if operand <= 3:
        return operand
    elif operand == 4:
        return registers["A"]
    elif operand == 5:
        return registers["B"]
    elif operand == 6:
        return registers["C"]
    else:
        raise ValueError(f"Invalid operand {operand} provided")


# Combo operands 0 through 3 represent literal values 0 through 3.
# Combo operand 4 represents the value of register A.
# Combo operand 5 represents the value of register B.
# Combo operand 6 represents the value of register C.
# Combo operand 7 is reserved and will not appear in valid programs.


def adv(opcode: int, operand: int, pointer: int) -> int:
    global registers
    registers["A"] = int(floor(registers["A"] / (2 ** combo_operand(operand))))
    return pointer + 2


def bxl(opcode: int, operand: int, pointer: int) -> int:
    global registers
    b = bin(registers["B"])[2:]
    o = bin(operand)[2:]
    if len(b) > len(o):
        o = o.zfill(len(b))
    elif len(b) < len(o):
        b = b.zfill(len(o))
    registers["B"] = int("".join([str(int(b[i] != o[i])) for i in range(len(b))]), 2)
    return pointer + 2


def bst(opcode: int, operand: int, pointer: int) -> int:
    global registers
    registers["B"] = combo_operand(operand) % 8
    return pointer + 2


def jnz(opcode: int, operand: int, pointer: int) -> int:
    global registers
    if registers["A"] == 0:
        return pointer + 2
    else:
        return operand


def bxc(opcode: int, operand: int, pointer: int) -> int:
    global registers
    b = bin(registers["B"])[2:]
    c = bin(registers["C"])[2:]
    if len(b) > len(c):
        c = c.zfill(len(b))
    elif len(b) < len(c):
        b = b.zfill(len(c))
    registers["B"] = int("".join([str(int(b[i] != c[i])) for i in range(len(b))]), 2)
    return pointer + 2


def out(opcode: int, operand: int, pointer: int) -> int:
    global registers
    global output
    output += [combo_operand(operand) % 8]
    return pointer + 2


def bdv(opcode: int, operand: int, pointer: int) -> int:
    global registers
    registers["B"] = int(floor(registers["A"] / (2 ** combo_operand(operand))))
    return pointer + 2


def cdv(opcode: int, operand: int, pointer: int) -> int:
    global registers
    registers["C"] = int(floor(registers["A"] / (2 ** combo_operand(operand))))
    return pointer + 2


def router(opcode: int, operand: int, pointer: int) -> int:
    if opcode == 0:
        # print("running adv")
        return adv(opcode, operand, pointer)
    if opcode == 1:
        # print("running bxl")
        return bxl(opcode, operand, pointer)
    if opcode == 2:
        # print("running bst")
        return bst(opcode, operand, pointer)
    if opcode == 3:
        # print("running jnz")
        return jnz(opcode, operand, pointer)
    if opcode == 4:
        # print("running bxc")
        return bxc(opcode, operand, pointer)
    if opcode == 5:
        # print("running out")
        return out(opcode, operand, pointer)
    if opcode == 6:
        # print("running bdv")
        return bdv(opcode, operand, pointer)
    if opcode == 7:
        # print("running cdv")
        return cdv(opcode, operand, pointer)


# instructions = [4, 0]
# registers = {"A": 0, "B": 2024, "C": 43690}
pointer = 0

while pointer < len(instructions) - 1:
    pointer = router(instructions[pointer], instructions[pointer + 1], pointer)

print(pointer, output, registers)
print(",".join([str(x) for x in output]))


# %% Part 2

# with open("advent_2024/17.txt", "r") as file:
#     registers = {x[9]: int(x[12:-1]) for x in file if x.startswith("Register")}

# with open("advent_2024/17.txt", "r") as file:
#     instructions = [x[9:].split(",") for x in file if x.startswith("Program:")]

# instructions = [int(x) for x in instructions[0]]

# print(registers)
# print(instructions)
# orig_registers = deepcopy(registers)

# output = []


# def combo_operand(operand: int) -> int:
#     global registers
#     if operand <= 3:
#         return operand
#     elif operand == 4:
#         return registers["A"]
#     elif operand == 5:
#         return registers["B"]
#     elif operand == 6:
#         return registers["C"]
#     else:
#         raise ValueError(f"Invalid operand {operand} provided")


# def adv(opcode: int, operand: int, pointer: int) -> int:
#     global registers
#     registers["A"] = int(floor(registers["A"] / (2 ** combo_operand(operand))))
#     return pointer + 2


# def bxl(opcode: int, operand: int, pointer: int) -> int:
#     global registers
#     registers["B"] = registers["B"] ^ operand
#     return pointer + 2


# def bst(opcode: int, operand: int, pointer: int) -> int:
#     global registers
#     registers["B"] = combo_operand(operand) % 8
#     return pointer + 2


# def jnz(opcode: int, operand: int, pointer: int) -> int:
#     global registers
#     if registers["A"] == 0:
#         return pointer + 2
#     else:
#         return operand


# def bxc(opcode: int, operand: int, pointer: int) -> int:
#     global registers
#     registers["B"] = registers["B"] ^ registers["C"]
#     return pointer + 2


# def out(opcode: int, operand: int, pointer: int) -> int:
#     global registers
#     global output
#     output += [combo_operand(operand) % 8]
#     return pointer + 2


# def bdv(opcode: int, operand: int, pointer: int) -> int:
#     global registers
#     registers["B"] = int(floor(registers["A"] / (2 ** combo_operand(operand))))
#     return pointer + 2


# def cdv(opcode: int, operand: int, pointer: int) -> int:
#     global registers
#     registers["C"] = int(floor(registers["A"] / (2 ** combo_operand(operand))))
#     return pointer + 2


# def router(opcode: int, operand: int, pointer: int) -> int:
#     if opcode == 0:
#         # print("running adv")
#         return adv(opcode, operand, pointer)
#     if opcode == 1:
#         # print("running bxl")
#         return bxl(opcode, operand, pointer)
#     if opcode == 2:
#         # print("running bst")
#         return bst(opcode, operand, pointer)
#     if opcode == 3:
#         # print("running jnz")
#         return jnz(opcode, operand, pointer)
#     if opcode == 4:
#         # print("running bxc")
#         return bxc(opcode, operand, pointer)
#     if opcode == 5:
#         # print("running out")
#         return out(opcode, operand, pointer)
#     if opcode == 6:
#         # print("running bdv")
#         return bdv(opcode, operand, pointer)
#     if opcode == 7:
#         # print("running cdv")
#         return cdv(opcode, operand, pointer)


# # instructions = [4, 0]
# # registers = {"A": 0, "B": 2024, "C": 43690}
# # a_val = 2814749767100656
# # a_val = 267265166212235
# a_val = 0

# while True:
#     registers = deepcopy(orig_registers)
#     registers["A"] = a_val
#     # print(registers)
#     output = []
#     pointer = 0
#     while pointer < len(instructions) - 1:
#         pointer = router(instructions[pointer], instructions[pointer + 1], pointer)
#         if output != instructions[: len(output)]:
#             break
#         # if len(output) == 7 and output == instructions[: len(output)]:
#         #     break

#     # if len(output) == 7 and output == instructions[: len(output)]:
#     #     print(output, a_val)
#     #     quit()

#     # print(pointer, output, registers)
#     # print(",".join([str(x) for x in output]))
#     if output == instructions:
#         print(a_val)
#         break
#     else:
#         a_val += 1

#     # if a_val % 500000 == 0:
#     #     print(a_val)

# print(pointer, output, registers)
# print(",".join([str(x) for x in output]))

# quit()
