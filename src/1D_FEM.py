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
    node_end = node_array.size - 1
    element_array = numpy.array((node_end, 2))
    for i in range(0, node_end):
        element_array[i, 0] = node_array[i]
        element_array[i, 1] = node_array[i + 1]
    return element_array

def generate_basis_functions(element_array):
    pass

def linear_interpolationY(x_0, x_1, y_0, y_1, X):
    return y_0 + (X - x_0)*(y_1 - y_0)/(x_1 - x_0)

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
    
    nodes = generate_nodes(X_dimension, N_nodes)
    elements = generate_elements(nodes)
    
    
    

if __name__ == "__main__":
    main()