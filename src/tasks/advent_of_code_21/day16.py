class Packet:
    def __init__(self, binary_seq) -> None:
        pass

class Transmission:
    def __init__(self, hex_input) -> None:
        pass

    def to_binary(self, hex_chars):
        bin(int(hex_chars, 16))[2:]

def main():
    
    hex_input = ''

    relative_path = 'src/tasks/advent_of_code_21/day16_input.txt'
    with open(relative_path, 'r') as f:
        for line in f:
            hex_input = line.strip()
    #print(f'{len(hex_input)}:{hex_input}')
    
    transmission = Transmission(hex_input)


if __name__ == '__main__':
    main()