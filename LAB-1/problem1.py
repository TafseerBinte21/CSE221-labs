def palindrome(word):
    if word == "":
        return -1

    n = len(word)

    for i in range(int(n/2)):
        if word[i] != word[n-i-1]:
            return 0
    return 1

def parity(word):
    if "." in word:
        return 0
    else:
        num = int(word)
        if num % 2 == 0:
            return 1
        else:
            return 2

with open('input.txt') as inFile:
    evenCount = 0
    oddCount = 0
    notParity = 0
    palCount = 0
    notpalCount = 0
    totalLine = 0
    with open("output.txt", "w") as outFile:
        while True:
            aline = inFile.readline()
            totalLine += 1
            if not aline:
                totalLine -= 1
                break

            word = aline.split()

            par = parity(word[0])
            if par == 1:
                evenCount += 1
                print(word[0], "is Even parity and", end=" ", file = outFile)
            elif par == 2:
                oddCount += 1
                print(word[0], "is Odd parity and", end=" ", file = outFile)
            elif par == 0:
                notParity += 1
                print(word[0], "cannot have parity and", end=" ", file = outFile)

            pal = palindrome(word[1])
            if pal == 0:
                notpalCount += 1
                print(word[1], 'is not a palindrome', file = outFile)
            elif pal == 1:
                palCount += 1
                print(word[1], 'is a palindrome', file = outFile)

    oddCount = int(oddCount*100/(totalLine))
    oddCount = str(oddCount)+"%"
    evenCount = int(evenCount*100/(totalLine))
    evenCount = str(evenCount)+"%"
    notParity = int(notParity*100/(totalLine))
    notParity = str(notParity)+"%"
    palCount = int(palCount*100/(totalLine))
    palCount = str(palCount)+"%"
    notpalCount = int(notpalCount*100/(totalLine))
    notpalCount = str(notpalCount)+"%"

    with open("record.txt", "w") as recFile:
        print("Percentage of odd parity: " + oddCount, file = recFile)
        print("Percentage of even parity: " + evenCount, file = recFile)
        print("Percentage of no parity: " + notParity, file = recFile)
        print("Percentage of palindrome: " + palCount, file = recFile)
        print("Percentage of non-palindrome: " + notpalCount, file = recFile)
