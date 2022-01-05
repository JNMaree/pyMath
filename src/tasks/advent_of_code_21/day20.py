def main():

    algorithm = ''
    input_image = []
    line_break = False

    filepath = 'src/tasks/advent_of_code_21/day20_input.txt'
    with open(filepath, 'r') as f:
        for line in f:
            if not line_break:
                if line == "\n":
                    line_break = True
                else:
                    algorithm = line.strip()
            else:
                input_image.append(line.strip())
    print(f'Image enhancement algorithm:\n{algorithm}\nInput_image\n{input_image}')

if __name__ == "__main__":
    main()