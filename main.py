import os

def get_list_file():
    file_list = os.listdir('Data')
    general_file = []
    for file in file_list:
        with open(os.path.join('Data', file), 'r', encoding='utf-8') as file_separate:
            general_file.append([file, 0, []])
            for line in file_separate:
                general_file[-1][2].append(line)
                general_file[-1][1] += 1
    sort_general_file = sorted(general_file, key=lambda x: x[1])

    for item in sort_general_file:
        with open('new_file.txt', 'a', encoding='utf-8') as file:
            log_msg = f"{item[0]}\n{item[1]}\n"
            file.write(log_msg)
            file.writelines(item[2])
            file.write("\n")

get_list_file()

