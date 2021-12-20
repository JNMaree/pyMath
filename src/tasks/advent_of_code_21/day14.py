class Polymer:
    def __init__(self, template, insertions) -> None:
        self.template = template
        self.insertion_rules = []
        self.elements = []
        self.quantities = []
        for i in insertions:
            rule = i.split(' -> ')
            self.insertion_rules.append(rule)
            self.add_element(rule[1])
        self.step = 0
        self.chains = [self.template]
    def __str__(self) -> str:
        sret = f'{self.step}\n'
        for i in range(len(self.elements)):
            sret += f'{self.elements[i]}:{self.quantities[i]}\n'
        return sret

    def add_element(self, char):
        if char not in self.elements:
            self.elements.append(char)
            self.quantities.append(0)

    def step_through(self) -> str:
        poly_chain = self.chains[self.step]
        new_chain = poly_chain[0]
        self.quantities = [0 for i in range(len(self.elements))]
        for i in range(len(poly_chain) - 1):
            pair = poly_chain[i] + poly_chain[i + 1]
            self.quantities[self.elements.index(poly_chain[i])] += 1
            
            rule = self.get_rule(pair)
            if rule is not None:
                new_chain += f'{rule}{poly_chain[i+1]}'
                self.quantities[self.elements.index(rule)] += 1
            else:
                new_chain += f'{pair}'
        self.quantities[self.elements.index(poly_chain[len(poly_chain)-1])] += 1
        self.chains.append(new_chain)
        self.step += 1
        return f'{len(new_chain)}\n{new_chain}'

    def get_rule(self, pair) -> str:
        for i in self.insertion_rules:
            if i[0] == pair:
                return i[1]
        return None

    def get_sorted_quantities(self) -> list:
        return sorted(self.quantities) 
        

def main():

    template = ''
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
                insertions.append(line.strip())
    #print(f"template:{template}\npair_insertion_rules:\n{insertions}")
    #"""
    template = 'NNCB'
    insertions = ['CH -> B',
                'HH -> N',
                'CB -> H',
                'NH -> C',
                'HB -> C',
                'HC -> B',
                'HN -> C',
                'NN -> C',
                'BH -> H',
                'NC -> B',
                'NB -> B',
                'BN -> B',
                'BB -> N',
                'BC -> B',
                'CC -> N',
                'CN -> C']
    #"""
    poly = Polymer(template, insertions)

    for i in range(1,11):
        print(f'step:{i}|{poly.step_through()}')
    print(poly)
    q = poly.get_sorted_quantities()
    mc_minus_lc = q[len(q) - 1] - q[0]
    print(f"MostCommon - LeastCommon:{mc_minus_lc}")
    
    # Part 2 -----------------------------------------------

if __name__ == "__main__":
    main()