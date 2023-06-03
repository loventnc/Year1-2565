message = input()
want = input()
change = input()


def myreplace(message,want,change):
    message = message.split(" ")
    n = 0
    for i in range(len(message)):

        if message[i] == want :
            message[i] = change
            n = n+1
        if want in message[i]:
            q = message[i].find(want)
            message[i] = message[i][:q] + change + message[i][q+len(want):]
            n = n+1

    print(" ".join(message))
    print(n)


myreplace(message,want,change)