import numpy

def generate_nodes(dimension_x, num_of_elements):
    node_coordinates = numpy.array((num_of_elements + 1))
    dim_increment = dimension_x/num_of_elements
    node_coordinates[0] = 0;
    for i in range (1, num_of_elements + 1):
        node_coordinates[i] = dim_increment
        dim_increment += dim_increment
    return node_coordinates

def generate_elements(node_array):
    pass

def generate_basis_functions(element_array):
    pass

def linear_interpolation(x_1, x_2, y_1, y_2):
    pass

def solve_PDE(basis_function_array):
    pass

def print_solution(solution_array):
    for i in solution_array:
        for j in i:
            print("node:{}",i)
            print(", f:{}", j)


def main():
    
    #test
    X_dimension = 10    # distance in meters
    N_nodes = 8         # number of nodes in domain
       
    displacement_field = numpy.array((N_nodes, 3))
    generate_nodes(X_dimension, N_nodes)
    
    

if __name__ == "__main__":
    main()