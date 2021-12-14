def main():

    template = []
    insertions = []
    line_break = False

    filepath = 'src/tasks/advent_of_code_21/day14_input.txt'
    with open(filepath, 'r') as f:
        for line in f:
            if not line_break:
                if line == "\n":
                    line_break = True
                else:
                    template = line.strip()
            else:
                insertions.append(line.strip().split(' -> '))
    
    print(f"template:{template}\npair_insertion_rules:\n{insertions}")

if __name__ == "__main__":
    main()