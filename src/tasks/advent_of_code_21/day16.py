class Packet:
    def __init__(self, first_six) -> None:
        self.is_complete = False
        self.version = self.bin_to_int(first_six[0:3])
        self.type_id = self.bin_to_int(first_six[3:])

        # Type 4 counters
        self.t4_last_group = False
        self.t4_pos = 0
        self.t4_literal = ''

        # Type Operator packet
        self.tO_sub_packets = []

    def add_bit(self, bit):
        if self.type_id == 4:           # Define Type 4 - int literal
            if self.t4_last_group:
                if self.t4_pos == 5:
                    self.is_complete = True
                else:
                    self.t4_literal += bit
                    self.t4_pos += 1
            else:
                if self.t4_pos == 5:
                    self.t4_literal += bit
                    self.t4_pos = 0
                elif self.t4_pos == 0:
                    if bit == 0:
                        self.t4_last_group = True
                        self.t4_pos += 1
                    else:
                        self.t4_pos += 1
                else:
                    self.t4_literal += bit
                    self.t4_pos += 1


    def bin_to_int(self, binchars) -> int:
        return int(binchars, 2)

    def __str__(self) -> str:
        sret = f'{self.version}, {self.type_id}: '
        if self.type_id == 4:
            sret += f'[{self.t4_literal}]:{self.bin_to_int(self.t4_literal)}'
        return sret

    def version_sum(self) -> int:
        if self.type_id == 4:
            return self.version
        else:
            iret = 0
            for i in self.tO_sub_packets:
                iret += i.version_sum()
            return iret

class Transmission:
    def __init__(self, hex_input) -> None:
        self.packets = []
         
        bin_input = self.to_binary(hex_input)   # Loop through binary data
        #print(f'hex_input:{hex_input}\nbin_input:{bin_input}')
        ct = 0
        trans_complete = False
        while not trans_complete:
            if ct + 6 > len(bin_input):
                trans_complete = True
            else:
                temp_packet = Packet(bin_input[ct:(ct+6)])
                ct += 6
                while not temp_packet.is_complete:
                    temp_packet.add_bit(bin_input[ct])
                    ct += 1
                self.packets.append(temp_packet)
    
    def __str__(self) -> str:
        sret = f'{len(self.packets)}\n'
        for i in range(len(self.packets)):
            sret += f'{i}|{self.packets[i]}\n'
        return sret
    
    def to_binary(self, hex_seq) -> str:
        sret = ''
        for c in hex_seq:
            sret += bin(int(c,16))[2:]
        return sret
    
    def sum_packet_versions(self) -> int:
        iret = 0
        for i in self.packets:
            iret += i.version_sum()
        return iret
    

def main():
    
    hex_input = ''

    relative_path = 'src/tasks/advent_of_code_21/day16_input.txt'
    with open(relative_path, 'r') as f:
        for line in f:
            hex_input = line.strip()
    #print(f'{len(hex_input)}:{hex_input}')
    
    trans = Transmission(hex_input)
    print(f'{trans}\nSum of Versions:{trans.sum_packet_versions()}')


if __name__ == '__main__':
    main()