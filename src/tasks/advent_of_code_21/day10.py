class Line:

    openers = '([{<'

    closers = ')]}>'

    chunks = []
    n = 0

    is_corrupt = False
    corruptions = []
    incompletes = []

    def defaults(self):
        self.chunks = []
        self.n = 0
        self.is_corrupt = False
        self.corruptions = []
        self.incompletes = []

    def __init__(self, strinput) -> None:
        self.defaults()
        ct = 0
        while ct < len(strinput) and not self.is_corrupt:
            i = strinput[ct]                # Read line to chunk array
            o = self.openers.find(i)
            c = -1
            if o >= 0:  # If char is opener
                self.chunks.append([self.openers[o], None])
                self.n += 1
            else:       # If char is closer
                c = self.closers.find(i)
                if c == -1:
                    raise ValueError(f"Incorrect Value read:{i}")
                pos = self.n - 1
                while pos >= 0:     # Check in reverse for first open pair
                    if self.chunks[pos][1] is None:
                        if self.chunks[pos][0] == self.openers[c]: # matching pair
                            self.chunks[pos][1] = self.closers[c]
                            pos = -2
                        else:
                            pos = 0
                    pos -= 1    # decrement pos to check
                # If corruption
                if pos == -1: 
                    #print(f"Corrupted[{ct}]! i:{i}, c:{c}, pos:{pos} chunks:{self.chunks[0]}")
                    self.is_corrupt = True
                    self.corruptions.append(i)
            #print(f"{ct}| i:{i}, o:{o}, c:{c}")
            ct += 1
        #   - Check if incomplete by checking if opener-closer pair exists with closer = 'None'
        if not self.is_corrupt:
            for chunk in reversed(self.chunks):
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

    def calc_syntax_error(self) -> int:
        if not self.is_corrupt:
            return None
        else:
            for i in self.corruptions:
                iret = 0
                if i == ')':
                    iret += 3
                elif i == ']':
                    iret += 57
                elif i == '}':
                    iret += 1197
                elif i == '>':
                    iret += 25137
                else:
                    raise TypeError(f"Incorrect Type caused corruption:{self.corrupted}")
            return iret

    def calc_complete_score(self) -> int:
        score = 0
        for i in self.incompletes:
            closer = 0
            if i == ')':
                closer = 1
            elif i == ']':
                closer = 2
            elif i == '}':
                closer = 3
            elif i == '>':
                closer = 4
            score *= 5
            score += closer
        return score

def main():

    rlines = []

    relative_path = 'src/tasks/advent_of_code_21/day10_input.txt'
    with open(relative_path, 'r') as f:
        rlines = f.readlines()

    #"""
    lines =['[({([[{{',                     # 0 - incomplete
            '({[<{(',                       # 1 - incomplete
            '{([(<{}[<>[]}>{[]{[(<()>',     # 2 - corrupt
            '((((<{<{{',                    # 3 - incomplete
            '[[<[([]))<([[{}[[()]]]',       # 4 - corrupt
            '[{[{({}]{}}([{[{{{}}([]',      # 5 - corrupt
            '<{[{[{{[[',                    # 6 - incomplete
            '[<(<(<(<{}))><([]([]()',       # 7 - corrupt
            '<{([([[(<>()){}]>(<<{{',       # 8 - corrupt
            '<{([']                         # 9 - incomplete
    #"""

    line_objects = []
    tot_error = 0

    for i in range(len(rlines)):
        line_instance = Line(rlines[i].strip())
        print(f"{i}|{line_instance}")
        if line_instance.is_corrupt:
            tot_error += line_instance.calc_syntax_error()
        else:
            line_objects.append(line_instance)
    print(f"Total Syntax Error:{tot_error}")

    # Part 2 ---------------------------------------------------------
    
    autocomplete_scores = []
    for i in range(len(line_objects)):
        autocomplete_scores.append(line_objects[i].calc_complete_score())
    autocomplete_scores = sorted(autocomplete_scores)
    print(f"AutoComplete Scores:{autocomplete_scores}")
    print(f"Middle Autocomplete Score:{autocomplete_scores[len(autocomplete_scores)//2]}")

if __name__ == "__main__":
    main()