class Polymer:
    def __init__(self, template, insertions) -> None:
        self.insertion_rules = []
        self.elements = []
        self.quantities = []
        self.count_pair = {}
        self.first_char = template[0]
        
        for i in insertions:
            rule = i.split(' -> ')
            self.insertion_rules.append(rule)
            if rule[1] not in self.elements:
                self.elements.append(rule[1])
                self.quantities.append(0)
            self.count_pair[rule[0]] = 0
        # Set template to init pair count
        for i in range(len(template) - 1):
            key = f'{template[i]}{template[i+1]}'
            self.count_pair[key] += 1
        print(self.count_pair)
    
    def __str__(self) -> str:
        sret = f'{sum(self.quantities)}\n'
        for i in range(len(self.elements)):
            sret += f'{self.elements[i]}:{self.quantities[i]}\n'
        sret = sret.rstrip()
        return sret

    def get_rule(self, key) -> str:
        for i in self.insertion_rules:
            if i[0] == key:
                return i[1]
        raise ProcessLookupError(f'Unknown Key:{key}')

    def step(self):
        count = self.count_pair.copy()
        for key in count:
            rule_char = self.get_rule(key)
            key_l = f'{key[0]}{rule_char}'  # left key
            key_r = f'{rule_char}{key[1]}'  # right key
            self.count_pair[key_l] += count[key]
            self.count_pair[key_r] += count[key]
            self.count_pair[key] -= count[key]
            #print(f'{key} -> {key_l}:{key_r}')
        self.set_quantities()
        print(self.count_pair)

    def set_quantities(self):
        self.quantities.clear()
        self.quantities = [0 for i in range(len(self.elements))]
        for key in self.count_pair:
            self.quantities[self.elements.index(key[1])] += self.count_pair[key]
        self.quantities[self.elements.index(self.first_char)] += 1

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
    """
    template = 'NNCB'
    insertions =   ['CH -> B',  # 6x B rules
                    'HH -> N',  # 3x N rules
                    'CB -> H',  # 2x H rules
                    'NH -> C',  # 5x C rules
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
        poly.step()
        print(f'>> step:{i}\n{poly}\n')
    q = poly.get_sorted_quantities()
    mc_minus_lc = q[len(q) - 1] - q[0]
    print(f"\tM_Common - L_Common:{mc_minus_lc}\n")
    
    # Part 2 -----------------------------------------------
    
    for i in range(11,41):
        poly.step()
        print(f'>> step:{i}\n{poly}\n')
    q = poly.get_sorted_quantities()
    mc_minus_lc = q[len(q) - 1] - q[0]
    print(f"\tM_Common - L_Common:{mc_minus_lc}\n")

if __name__ == "__main__":
    main()