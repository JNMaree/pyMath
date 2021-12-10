class Line:

    openers = '([{<'

    closers = ')]}>'

    chunks = []

    n = 0

    is_corrupt = False
    corruptions = []

    incompletes = []

    def __init__(self, strinput) -> None:
        ct = 0
        while ct < len(strinput) and not self.is_corrupt:
            i = strinput[ct]                # Read line to chunk array
            o = self.openers.find(i)
            c = -1
            if o > -1:  # If char is opener
                self.chunks.append([self.openers[o], None])
                self.n += 1
            else:       # If char is closer
                c = self.closers.find(i) 
                pos = self.n - 1 
                while pos >= 0:     # Check in reverse for first open pair
                    if self.chunks[pos][0] == self.openers[c]:
                        # Set closer for most recent opener of same type
                        self.chunks[pos][1] = self.closers[c]
                        pos = -2
                    else:
                        pos -= 1    # decrement pos to check
                # If corruption
                if pos == -1: 
                    print(f"Corrupted[{ct}]! i:{i}, c:{c}, pos:{pos} chunks:{self.chunks[0]}")
                    self.is_corrupt = True
                    self.corruptions.append(i)
            #print(f"{ct}| i:{i}, o:{o}, c:{c}")
            ct += 1

        # Check if chunks incomplete
        #   - Check if opener-closer pair exists with closer = 'None'
        if not self.is_corrupt:
            for chunk in self.chunks:
                if chunk[1] is None:                                # If any chunks opened but not closed (yet),
                    cindex = self.openers.find(chunk[0])
                    self.incompletes.append(self.closers[cindex])   #   - add corresponding closure bracket

    def __str__(self) -> str:
        sret = format(self.n)
        if self.is_corrupt:
            sret += f" CORRUPTED[{len(self.corruptions)}]:{self.corruptions}\n"
        elif len(self.incompletes) > 0:
            sret += f" INCOMPLETE[{len(self.incompletes)}]:{self.incompletes}\n"
        else:
            sret += "\n"
        for i in range(self.n):
            sret += f"{i}| {self.chunks[i][0]},{self.chunks[i][1]} "
        return sret

    def calc_syntax_error(self):
        if not self.is_corrupt:
            return None
        elif self.corruptions[0] == ')':
            return 3
        elif self.corruptions[0] == ']':
            return 57
        elif self.corruptions[0] == '}':
            return 1197
        elif self.corruptions[0] == '>':
            return 25137
        else:
            raise TypeError(f"Incorrect Type caused corruption:{self.corrupted}")

def main():

    rlines = []

    relative_path = 'src/tasks/advent_of_code_21/day10_input.txt'
    with open(relative_path, 'r') as f:
        rlines = f.readlines()

    #"""
    test_lines = ['[({(<(())[]>[[{[]{<()<>>',
        '[(()[<>])]({[<{<<[]>>(',
        '{([(<{}[<>[]}>{[]{[(<()>',
        '(((({<>}<{<{<>}{[]{[]{}',
        '[[<[([]))<([[{}[[()]]]',
        '[{[{({}]{}}([{[{{{}}([]',
        '{<[[]]>}<{[{[{[]{()[[[]',
        '[<(<(<(<{}))><([]([]()',
        '<{([([[(<>()){}]>(<<{{',
        '<{([{{}}[<[[[<>{}]]]>[]]']
    
    linejects = []
    tot_error = 0

    for i in range(len(test_lines)):
        line_instance = Line(test_lines[i].strip())
        print(f"{i}|{line_instance}")
        if line_instance.is_corrupt:
            tot_error += line_instance.calc_syntax_error()
        linejects.append(line_instance)
 
    print(f"Total Syntax Error:{tot_error}")
    

if __name__ == "__main__":
    main()