import re


def main(s: str):
    option = re.compile('"\w*"')
    parametr = re.compile('#\d+')
    optList = re.findall(option, s)
    parList = re.findall(parametr, s)
    d = {}
    for i in range(len(optList)):
        d[optList[i][1:-2]] = int(parList[i][1:])

    return d
