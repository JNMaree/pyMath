import numpy

from nodespace_1D import NodeSpace1D
from elementspace_1D import ElementSpace1D 

class Mesh1D:

    def __init__(self, nodes, elements):
        self.node_space = nodes
        self.element_space = elements

    def __str__(self) -> str:
        ret_str = self.node_space.__str__()
        ret_str += self.element_space.__str__()
        return ret_str


def main():
    print("Test Match:")
    narray = numpy.arange(8)
    nspace = NodeSpace1D(narray)
    espace = ElementSpace1D(nspace)

    mesh = Mesh1D(nspace, espace)
    print(mesh)


if __name__ == "__main__":
    main() 