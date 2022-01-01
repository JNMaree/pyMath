class Pair:
    def __init__(self, pstr: str =None, depth=0) -> None:
        self.d = depth
        self.x = None       # Default x type is Pair type, otherwise int
        self.y = None       # Default y type is Pair type, otherwise int
        self.is_reduced = False

        if pstr is not None:
            pstr_cut = ''
            # Add x value of pair
            if pstr[1] == '[':
                bracketed = self.get_bracketed_substr(pstr[1:])
                self.x = Pair(bracketed, depth + 1)
                pstr_cut = pstr.replace(f'[{bracketed}', '', 1)
            else:
                self.x = int (pstr[1])
                pstr_cut = pstr.replace(f'[{self.x}', '', 1)
            # Add y value of pair
            if pstr_cut[1] == '[':
                bracketed = self.get_bracketed_substr(pstr_cut[1:])
                self.y = Pair(bracketed, depth + 1)
            else:
                self.y = int(pstr_cut[1])

    def __str__(self) -> str:
        sret = f'[{self.x},{self.y}]'
        return sret

    # Overload addition operator
    def __add__(self, other):
        new_pair = Pair()
        new_pair.x = self
        new_pair.y = other
        new_pair.to_reduced()
        return new_pair

    # Return a substring enclosed by the first bracket
    def get_bracketed_substr(self, pstr) -> str:
        bret = []
        open_brackets = 0
        for s in pstr:
            bret.append(s)
            if s == '[':
                open_brackets += 1
            elif s == ']':
                open_brackets -= 1
                if open_brackets == 0:
                    sret = ''.join(bret)
                    #print(f'get_bracketed_of {pstr}  ->  {sret}')
                    return sret
        raise LookupError(f'Str:{pstr} has unclosed brackets')

    def to_reduced(self):
        while not self.is_reduced:
            if isinstance(self.x, Pair):
                if not self.x.is_reduced:
                    self.x.to_reduced()
            else:
                pass
            if isinstance(self.y, Pair):
                if not self.y.is_reduced:
                    self.y.to_reduced()
            else:
                pass

            

    def get_magnitude(self) -> int:
        xm = 0
        if isinstance(self.x, Pair):
            xm = self.x.get_magnitude()
        else:
            xm = self.x
        ym = 0
        if isinstance(self.y, Pair):
            ym = self.y.get_magnitude()
        else:
            ym = self.y
        return (3*xm) + (2*ym)

class PairList:
    def __init__(self, numbers) -> None:
        self.pairs = []
        for n in range(len(numbers)):
            pair_n = Pair(numbers[n])
            self.pairs.append(pair_n)
            print(f'{n}: {pair_n}')

def main():
    
    numbers = []

    relative_path = 'src/tasks/advent_of_code_21/day18_input.txt'
    with open(relative_path, 'r') as f:
        for line in f:
            numbers.append(line.strip())
    #print(f'{numbers}')

    numbers = ['[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]',
            '[[[5,[2,8]],4],[5,[[9,9],0]]]',
            '[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]',
            '[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]',
            '[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]',
            '[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]',
            '[[[[5,4],[7,7]],8],[[8,3],8]]',
            '[[9,3],[[9,9],[6,[4,9]]]]',
            '[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]',
            '[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]']

    plist = PairList(numbers)
    


if __name__ == '__main__':
    main()