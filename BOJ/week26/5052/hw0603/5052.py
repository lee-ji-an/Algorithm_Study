import sys

t = int(sys.stdin.readline())
flag = False

for _ in range(t):
    phonebook = {}

    n = int(sys.stdin.readline())
    numbers = sorted(
        list(
            map(
                int,
                list(
                    sys.stdin.readline().strip()
                )
            )
        ) for _ in range(n)
    )

    for number in numbers:
        phonebookPtr = phonebook
        for digit in number:
            if ((digit in phonebookPtr) and len(phonebookPtr[digit]) == 0):
                print("NO")
                flag = True
                break

            if (digit not in phonebookPtr):
                phonebookPtr[digit] = {}
            phonebookPtr = phonebookPtr[digit]

        if (flag):
            flag = False
            break
    else:
        print("YES")
