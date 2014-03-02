#!/usr/bin/env python
"""
Maximum path sum - 
    The module calculates the maximum path value 
    for a triangular structure.

    The algorithm takes advantage of the recursive 
    structure of the problem and uses a dynamic
    programming algorithm to calculate
    the maximum path value for each subtree.
"""
import sys

def read_input( filename ):
    nodes = []
    f = open( filename, 'r' )
    for line in f:
        nodes_string = line.split()
        nodes_integer = [int(x) for x in nodes_string]
        nodes.append( nodes_integer )
    f.close()
    return nodes

def find_maximum_path( nodes ):
    # The maximum path in an empty triangle is 0
    if len(nodes) == 0:
        return 0

    level = len( nodes )
    current_index = level - 1
    maximum_path = nodes[current_index]
    level -= 1

    while level > 0:
        current_index =  level - 1
        number_of_elements = level
        new_maximum_path = [0] * number_of_elements
        values_level = nodes[current_index]

        for i in range(0, number_of_elements):
            left_subtree_max = maximum_path[i] 
            right_subtree_max = maximum_path[i + 1] 
            node_value = values_level[i]
            left_subtree_max += node_value
            right_subtree_max += node_value
            new_maximum_path[ i ] = max( left_subtree_max, right_subtree_max )
        maximum_path = new_maximum_path 
        level -= 1

    return maximum_path.pop()


def solve_maximum_path( file_name ):
    nodes = read_input( file_name )
    return find_maximum_path( nodes )

if __name__ == '__main__':
    if len( sys.argv ) == 1:
        raise Exception('Please provide input file for problem..')

    file_path = sys.argv[1]
    print solve_maximum_path(file_path)
