from state import State


all_node = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'I1', 'I11',
            'I12', 'I2', 'I21', 'I22', 'G1', 'G11', 'G111', 'G112', 'G12', 'G121', 'G122', 'G2', 'G21', 'G211', 'G212',
            'G22', 'G221', 'G222','H1', 'H11', 'H111', 'H112', 'H12', 'H121', 'H122', 'H2', 'H21', 'H211', 'H212', 'H22',
            'H221', 'H222','M1', 'M2', 'N1', 'N2', 'O1', 'O2']

def build_graph(filename):
    node_data = filename
    init_node = State(node_data[0], None, "MAX")
    construct_nodes(init_node, node_data, "MAX")
    return init_node


def construct_nodes(node, node_data, node_type):
    node_type = "MIN" if node_type == "MAX" else "MAX"
    for element in node_data:
        if type(element) is str:
            pass
        elif type(element) is list:
            child = State(element[0], None, node_type)
            node.add_child(child)
            construct_nodes(child, element, node_type)
        elif type(element) is tuple:
            leaf = State(element[0], element[1], "NA")
            node.add_child(leaf)
        else:
            print(">>> ERROR: Invalid configuration file <<<")

def alpha_beta_pruning_minimax(node):
    visited = []
    best_val, visited = select_max_ab(node, float('-inf'), float('inf'), visited)
    pruning = list(set(all_node)-set(visited))
    return "\nOptimal Utility Value: " + str(best_val) + "\nVisited: " + str(visited) + "\nPruning Nodes: " + str(pruning) + "\n"


def select_max_ab(node, alpha, beta, visited):
    # Store visited node
    visited.append(node.get_node_id())
    # Base case
    if node.is_leaf():
        return node.get_value()

    # Initialize max val
    max_val = float('-inf')

    # Iterate through children and make mutually recursive call to select_min() for each child
    children = node.get_children()
    for i, child in enumerate(children):
        score = select_min_ab(child, alpha, beta, visited)

        # Save max val
        if score > max_val:
            max_val = score

        # Prune if possible
        if max_val >= beta:
            return max_val, visited

        # Update best alternative for MAX value (Alpha)
        if max_val > alpha:
            alpha = max_val
        print(visited,max_val)

    return max_val, visited

def select_min_ab(node, alpha, beta, visited):
    # Store visited node
    visited.append(node.get_node_id())

    # Base case
    if node.is_leaf():
        return node.get_value()

    # Initialize min val
    min_val = float('inf')

    # Iterate through children and make mutually recursive call to select_max() for each child
    children = node.get_children()
    for i, child in enumerate(children):
        score = select_max_ab(child, alpha, beta, visited)[0]

        # Save min val
        if score < min_val:
            min_val = score

        # Prune if possible
        if min_val <= alpha:
            return min_val

        # Update best alternative for MIN value (Beta)
        if min_val < beta:
            beta = min_val

    return min_val


def main():
    # Read config
    init_node = build_graph(['A', ['B', ['F',['I',['I1',('I11',3),('I12',0)],['I2',('I21',4),('I22',0)]],['J',['J1',('J11',5),('J12',0)],['J2',('J21',2),('J22',1)]]],
                                    ['G',['G1',['G11',('G111',2),('G112',0)],['G12',('G121',3),('G122',0)]],['G2',['G21',('G211',0),('G212',0)],['G22',('G221',0),('G222',0)]]],
                                    ['H',['H1',['H11',('H111',10),('H112',0)],['H12',('H121',11),('H122',0)]],['H2',['H21',('H211',0),('H212',0)],['H22',('H221',0),('H222',0)]]]],
                              ['D',['K',('P',12),('Q',45)],['L',('R',3),('S',-10)],['M',('M1',1),('M2',0)]],
                             ['E',['N',('N1',2),('N2',0)],['O',('O1',2),('O2',2)]],('C',9)])

    print(init_node)
    val = alpha_beta_pruning_minimax(init_node)
    print("\n---Alpha Beta Pruning Minimax---" + val)

main()