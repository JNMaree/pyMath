class Pair:
    def __init__(self, pstr, depth=0) -> None:
        self.d = depth
        self.xy = []
        self.regular = False
        if pstr.isnumeric():
            self.regular = True
            self.xy.append(int (pstr))
        else:
            pstr_cut = self.trim_brackets(pstr)        
            for i in range(2):
                if pstr_cut[0] == '[':
                    new_pstr = pstr_cut[1:pstr_cut.rfind(']', -1)]
                    self.xy.append( Pair(new_pstr, depth+1) )
                    pstr_cut = pstr_cut.replace(new_pstr, '')
                else:
                    self.xy.append( Pair(pstr_cut[0], depth) )
                    pstr_cut = pstr_cut.replace(f'{self.xy[i]}', '')

    def __str__(self) -> str:
        sret = ''
        if self.regular:
            sret += '-' * self.d
            sret += f'{self.xy[0]}' 
        else:
            sret += f'{self.xy[0]},'
            sret += f'{self.xy[1]}'
        return sret

    # Remove outer brackets
    def trim_brackets(self, pstr) -> str:
        pstr_cut = pstr.removeprefix('[')
        pstr_cut = pstr_cut.removesuffix(']')
        return pstr_cut

    def to_reduced(self):
        pass

    def get_magnitude(self) -> int:
        for xy in self.xy:
            if self.regular:
                return self.xy[0]
            else:
                return xy.get_magnitude()

class PairList:
    def __init__(self, numbers) -> None:
        self.pairs = []
        for n in numbers:
            pair_n = Pair(n)
            self.pairs.append(pair_n)


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