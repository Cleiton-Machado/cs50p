import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(
        r"^([0-9]+):?([0-5][0-9])? (AM|PM) to ([0-9]+):?([0-5][0-9])? (AM|PM)$", s
    ):
        hour = []
        minutes = []
        for i in [0, 3]:
            if int(matches.group(i + 1)) <= 12:
                if matches.group(i + 3) == "PM":
                    if int(matches.group(i + 1)) <= 11:
                        n_hour = int(matches.group(i + 1)) + 12
                    else:
                        n_hour = int(matches.group(i + 1))
                else:
                    if int(matches.group(i + 1)) == 12:
                        n_hour = int(matches.group(i + 1)) - 12
                    else:
                        n_hour = int(matches.group(i + 1))
                hour.append(n_hour)
                if matches.group(i + 2) == None:
                    n_min = int(0)
                else:
                    n_min = int(matches.group(i + 2))
                minutes.append(n_min)
            else:
                raise ValueError
        texto = f"{hour[0]:02}:{minutes[0]:02} to {hour[1]:02}:{minutes[1]:02}"
        return texto
    else:
        raise ValueError


if __name__ == "__main__":
    main()
