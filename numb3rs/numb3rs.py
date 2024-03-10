import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    matches = re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip)
    if matches:
        for group in matches.groups():
            if int(group) <= 255:
                pass
            else:
                return False
        return True
    else:
        return False



if __name__ == "__main__":
    main()


