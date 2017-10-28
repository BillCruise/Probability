# State names letter frequency

def state_names():
    # load names from file
    with open("../data/state_names.txt", "r") as file:
        lines = file.readlines()

    # convert to lower case and strip \n
    lines = [x.lower().strip() for x in lines]
    print(lines)

    # initialize a frequency list
    alpha = "abcdefghijklmnopqrstuvwxyz "
    freq = dict()
    for c in alpha:
        freq[c] = 0

    # count letter frequency
    for word in lines:
        for char in word:
            freq[char] += 1

    # sort letters by frequency
    s_freq = sorted(freq.items(), key=lambda x: x[1])
    print(s_freq)


if __name__ == '__main__':
    state_names()
