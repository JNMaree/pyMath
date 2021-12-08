from numpy import zeros
from numpy.core.fromnumeric import sort


class Signal:

    pattern = []

    output = []

    seg7seq = []

    def __init__(self, entry) -> None:
        signal = entry.strip().split(' | ')
        self.pattern = signal[0].split()
        self.output = signal[1].split()
        self.seg7seq = [''] * 10

    def __str__(self) -> str:
        sret = format(self.pattern) + " | "
        sret += format(self.output)
        return sret

    def count_output_digit_sequences(self, n_digits):
        ct = 0
        for i in self.output:
            if len(i) == n_digits:
                ct += 1
        return ct

    def set_display_correlation(self):
        seq069 = []
        seq235 = []
        # Set sequences based on length
        for i in self.pattern:
            seg = len(i)
            seq = ''.join(sorted(i))
            if seg == 2:                    # set 1
                self.seg7seq[1] = seq
            elif seg == 4:                  # set 4
                self.seg7seq[4] = seq
            elif seg == 3:                  # set 7
                self.seg7seq[7] = seq
            elif seg == 7:                  # set 8
                self.seg7seq[8] = seq
            elif seg == 6:
                seq069.append(seq)
            else:
                seq235.append(seq)

        # Isolate left-upper and middle segments
        lup_mid = self.seg7seq[4]
        for i in self.seg7seq[1]:
            lup_mid = lup_mid.replace(i, '')

        # Set 0 6 9
        for i in seq069: # 6 char length
            ct = 0
            for s in self.seg7seq[1]:
                if s in i:
                    ct += 1
            if ct == 2: # 0 or 9
                ctn = 0
                for s in lup_mid:
                    if s in i:
                        ctn += 1
                if ctn == 2:
                    self.seg7seq[9] = i     # set 9
                else:
                    self.seg7seq[0] = i     # set 0

            else:
                self.seg7seq[6] = i         # set 6

        # Set 2 3 5
        for i in seq235: # 5 char length
            ct = 0
            for s in lup_mid:
                if s in i:
                    ct += 1
            if ct == 2:
                self.seg7seq[5] = i         # set 5
            else:
                ctn = 0
                for s in self.seg7seq[1]:
                    if s in i:
                        ctn += 1
                if ctn == 2:
                    self.seg7seq[3] = i     # set 3
                else:
                    self.seg7seq[2] = i     # set 2

        #Print correlations 
        #for i in range(10):
        #    print(f"{i} seg:{self.seg7seq[i]}")


    def get_output(self):
        self.set_display_correlation()
        sret = ''
        for i in self.output:
            seq = ''.join(sorted(i))
            for s in range(10):
                if seq == self.seg7seq[s]:
                    sret += format(s)
        return int(sret)


def main():

    signal_entry = []

    relative_path = 'src/tasks/advent_of_code_21/day8_input.txt'
    with open(relative_path, 'r') as f:
        signal_entry = f.readlines()
    #print(f"signal_entry: {signal_entry}")
    
    signals = []

    for i in signal_entry:
        signals.append(Signal(i))

    ct = 0
    for i in signals:
        ct += i.count_output_digit_sequences(2) #1
        ct += i.count_output_digit_sequences(4) #4
        ct += i.count_output_digit_sequences(3) #7
        ct += i.count_output_digit_sequences(7) #8
    print(f"[1,4,7,8]'s in output:{ct}")

    # Part 2 --------------------------------------------------------

    osum = 0
    for i in range(len(signals)):
        out = signals[i].get_output()
        osum += out
        print(f"{i}|{signals[i]} :{out}")
    print(f"Sum of Outputs:{osum}")

if __name__ == "__main__":
    main()