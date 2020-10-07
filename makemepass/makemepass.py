#!/usr/bin/env python3
import random, string, sys
def main(lenght=16):
    counter = 0
    passwd = ""
    proto_passwd = ""
    while lenght != counter:
        proto_passwd += random.choice(string.ascii_letters)
        counter += 1

    pass2list = list(proto_passwd)
    for i in range(lenght//4):
        pass2list[random.randint(1,(lenght-1))] = random.choice(string.digits)

    passwd = "".join(pass2list)
    return passwd

if __name__ == "__main__":
    main()


if len(sys.argv) < 2 or len(sys.argv) > 2:
    print("""
          Usage: python makemepass.py <number>
            example: python makemepass.py 12
         """)

try:
    print(main(int(sys.argv[1])))
except:
    exit()


