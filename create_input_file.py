from Diz import diz_qa

input_file = []


if __name__ == '__main__':

    for key in diz_qa.keys():
        input_file.append(f'{key}{diz_qa[key]}')

    print(input_file)