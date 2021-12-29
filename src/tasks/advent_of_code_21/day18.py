

def main():
    
    numbers = []

    relative_path = 'src/tasks/advent_of_code_21/day18_input.txt'
    with open(relative_path, 'r') as f:
        for line in f:
            numbers.append(line.strip())
    print(f'{numbers}')

    


if __name__ == '__main__':
    main()