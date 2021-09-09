import numpy

from nodespace_1D import NodeSpace1D
from elementspace_1D import ElementSpace1D 

class Mesh1D:

    # SolutionSpace defines the degree-of-freedom (dof) at each node
    solution_space = []

    def __init__(self, elements):
        if isinstance(elements, ElementSpace1D):
            self.element_space = elements
            self.solution_space = numpy.empty_like(elements.nodes)

    def __str__(self) -> str:
        ret_str = self.element_space.nodeSpace_str()
        ret_str += self.element_space.__str__()
        return ret_str


def main():
    print("Test Mesh:")
    
    n_array = numpy.linspace(6, 16, 21)
    nspace = NodeSpace1D(n_array)
    espace = ElementSpace1D(nspace)
    #print("nspace:", nspace)
    #print("espace:", espace)

    mesh = Mesh1D(espace)
    print(mesh)

if __name__ == "__main__":
    main() 