def init():
    num_str = input("Number of strings: ")
    try:
        num_str = int(num_str)
    except Exception as e:
        print(e, "\nYou can't do that!!")
        return

    if num_str == 0:
        print("You can't do that!!")
        return

    str_list = []
    for i in range(num_str):
        input_str = input(f"Enter string {i + 1}: ")
        str_list.append(input_str)

    g_max = max(g.count("G") for g in str_list)
    maxg_list = []
    if g_max != 0:
        maxg_list = [g for g in str_list if g.count("G") == g_max]

    final = []
    if maxg_list:
        s_max = max(s.count("S") for s in maxg_list)
        if s_max != 0:
            final = [s for s in maxg_list if s.count("S") == s_max]
        else:
            final = maxg_list

    print(final)


if __name__ == '__main__':
    init()
