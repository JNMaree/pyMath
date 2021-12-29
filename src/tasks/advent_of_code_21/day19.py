
def main():
    
    scanners = []

    relative_path = 'src/tasks/advent_of_code_21/day19_input.txt'
    with open(relative_path, 'r') as f:
        scan = []
        for line in f:
            if 'scan' in line:
                scan_id = [int (s) for s in line.split() if s.isdigit()]
                scan.append(scan_id[0])
            elif line.strip():
                scan.append(line.strip())
            else:
                scanners.append(scan)
                scan = []
    print(f'{scanners}')

    


if __name__ == '__main__':
    main()