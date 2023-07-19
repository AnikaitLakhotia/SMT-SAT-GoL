from z3 import *


def generate_neighboring_cells(k, o, ca_b_c, n, m):
    """
    Generate neighboring cells in previous generation based on given parameters.

    Args:
        k (int): Index of the element.
        o (int): Offset value.
        ja_b_c (str): Input element string.
        n (int): Number of rows.
        m (int): Number of columns.

    Returns:
        tuple: Tuple containing the generated expressions.
    """
    e = get_kth_element(k, o, n, m)
    a, b, c = map(int, e[1:].split('_'))
    p = f'c{a-1}_{b-1}_{c-1}' if a-1 != 0 and b-1 != 0 and c-1 >= 0 else 'h'
    q = f'c{a-1}_{b}_{c-1}' if a-1 != 0 and c-1 >= 0 else 'h'
    r = f'c{a-1}_{b+1}_{c-1}' if a-1 != 0 and b+1 <= m and c-1 >= 0 else 'h'
    s = f'c{a}_{b+1}_{c-1}' if b+1 <= m and c-1 >= 0 else 'h'
    t = f'c{a+1}_{b+1}_{c-1}' if a+1 <= n and b+1 <= m and c-1 >= 0 else 'h'
    u = f'c{a+1}_{b}_{c-1}' if a+1 <= n and c-1 >= 0 else 'h'
    v = f'c{a+1}_{b-1}_{c-1}' if a+1 <= n and b-1 != 0 and c-1 >= 0 else 'h'
    w = f'c{a}_{b-1}_{c-1}' if b-1 != 0 and c-1 >= 0 else 'h'
    return a, b, c, p, q, r, s, t, u, v, w


def to_clause(a, b, c, p, q, r, s, t, u, v, w):
    """
    Make a Z3 clause from the given cells(variables).

    Args:
        a, b, c (int): Indices.
        p, q, r, s, t, u, v, w (str): Cells.

    Returns:
        str: Z3 clause as a string.

    """
    # The large clause is constructed here as a multi-line string.
    return f"""
         And(Not(h), c{a}_{b}_{c} == And(Or(And(Not({p}), Not({q}), {r}, {s}, {t}, {u}, {v}, {w}),
            And(Not({p}), {q}, Not({r}), {s}, {t}, {u}, {v}, {w}),
            And(Not({p}), {q}, {r}, Not({s}), {t}, {u}, {v}, {w}),
            And(Not({p}), {q}, {r}, {s}, Not({t}), {u}, {v}, {w}),
            And(Not({p}), {q}, {r}, {s}, {t}, Not({u}), {v}, {w}),
            And(Not({p}), {q}, {r}, {s}, {t}, {u}, Not({v}), {w}),
            And(Not({p}), {q}, {r}, {s}, {t}, {u}, {v}, Not({w})),
            And({p}, Not({q}), Not({r}), {s}, {t}, {u}, {v}, {w}),
            And({p}, Not({q}), {r}, Not({s}), {t}, {u}, {v}, {w}),
            And({p}, Not({q}), {r}, {s}, Not({t}), {u}, {v}, {w}),
            And({p}, Not({q}), {r}, {s}, {t}, Not({u}), {v}, {w}),
            And({p}, Not({q}), {r}, {s}, {t}, {u}, Not({v}), {w}),
            And({p}, Not({q}), {r}, {s}, {t}, {u}, {v}, Not({w})),
            And({p}, {q}, Not({r}), Not({s}), {t}, {u}, {v}, {w}),
            And({p}, {q}, Not({r}), {s}, Not({t}), {u}, {v}, {w}),
            And({p}, {q}, Not({r}), {s}, {t}, Not({u}), {v}, {w}),
            And({p}, {q}, Not({r}), {s}, {t}, {u}, Not({v}), {w}),
            And({p}, {q}, Not({r}), {s}, {t}, {u}, {v}, Not({w})),
            And({p}, {q}, {r}, Not({s}), Not({t}), {u}, {v}, {w}),
            And({p}, {q}, {r}, Not({s}), {t}, Not({u}), {v}, {w}),
            And({p}, {q}, {r}, Not({s}), {t}, {u}, Not({v}), {w}),
            And({p}, {q}, {r}, Not({s}), {t}, {u}, {v}, Not({w})),
            And({p}, {q}, {r}, {s}, Not({t}), Not({u}), {v}, {w}),
            And({p}, {q}, {r}, {s}, Not({t}), {u}, Not({v}), {w}),
            And({p}, {q}, {r}, {s}, Not({t}), {u}, {v}, Not({w})),
            And({p}, {q}, {r}, {s}, {t}, Not({u}), Not({v}), {w}),
            And({p}, {q}, {r}, {s}, {t}, Not({u}), {v}, Not({w})),
            And({p}, {q}, {r}, {s}, {t}, {u}, Not({v}), Not({w})),
            And(Not({p}), Not({q}), Not({r}), {s}, {t}, {u}, {v}, {w}),
            And(Not({p}), Not({q}), {r}, Not({s}), {t}, {u}, {v}, {w}),
            And(Not({p}), Not({q}), {r}, {s}, Not({t}), {u}, {v}, {w}),
            And(Not({p}), Not({q}), {r}, {s}, {t}, Not({u}), {v}, {w}),
            And(Not({p}), Not({q}), {r}, {s}, {t}, {u}, Not({v}), {w}),
            And(Not({p}), Not({q}), {r}, {s}, {t}, {u}, {v}, Not({w})),
            And(Not({p}), {q}, Not({r}), Not({s}), {t}, {u}, {v}, {w}),
            And(Not({p}), {q}, Not({r}), {s}, Not({t}), {u}, {v}, {w}),
            And(Not({p}), {q}, Not({r}), {s}, {t}, Not({u}), {v}, {w}),
            And(Not({p}), {q}, Not({r}), {s}, {t}, {u}, Not({v}), {w}),
            And(Not({p}), {q}, Not({r}), {s}, {t}, {u}, {v}, Not({w})),
            And(Not({p}), {q}, {r}, Not({s}), Not({t}), {u}, {v}, {w}),
            And(Not({p}), {q}, {r}, Not({s}), {t}, Not({u}), {v}, {w}),
            And(Not({p}), {q}, {r}, Not({s}), {t}, {u}, Not({v}), {w}),
            And(Not({p}), {q}, {r}, Not({s}), {t}, {u}, {v}, Not({w})),
            And(Not({p}), {q}, {r}, {s}, Not({t}), Not({u}), {v}, {w}),
            And(Not({p}), {q}, {r}, {s}, Not({t}), {u}, Not({v}), {w}),
            And(Not({p}), {q}, {r}, {s}, Not({t}), {u}, {v}, Not({w})),
            And(Not({p}), {q}, {r}, {s}, {t}, Not({u}), Not({v}), {w}),
            And(Not({p}), {q}, {r}, {s}, {t}, Not({u}), {v}, Not({w})),
            And(Not({p}), {q}, {r}, {s}, {t}, {u}, Not({v}), Not({w})),
            And({p}, Not({q}), Not({r}), Not({s}), {t}, {u}, {v}, {w}),
            And({p}, Not({q}), Not({r}), {s}, Not({t}), {u}, {v}, {w}),
            And({p}, Not({q}), Not({r}), {s}, {t}, Not({u}), {v}, {w}),
            And({p}, Not({q}), Not({r}), {s}, {t}, {u}, Not({v}), {w}),
            And({p}, Not({q}), Not({r}), {s}, {t}, {u}, {v}, Not({w})),
            And({p}, Not({q}), {r}, Not({s}), Not({t}), {u}, {v}, {w}),
            And({p}, Not({q}), {r}, Not({s}), {t}, Not({u}), {v}, {w}),
            And({p}, Not({q}), {r}, Not({s}), {t}, {u}, Not({v}), {w}),
            And({p}, Not({q}), {r}, Not({s}), {t}, {u}, {v}, Not({w})),
            And({p}, Not({q}), {r}, {s}, Not({t}), Not({u}), {v}, {w}),
            And({p}, Not({q}), {r}, {s}, Not({t}), {u}, Not({v}), {w}),
            And({p}, Not({q}), {r}, {s}, Not({t}), {u}, {v}, Not({w})),
            And({p}, Not({q}), {r}, {s}, {t}, Not({u}), Not({v}), {w}),
            And({p}, Not({q}), {r}, {s}, {t}, Not({u}), {v}, Not({w})),
            And({p}, Not({q}), {r}, {s}, {t}, {u}, Not({v}), Not({w})),
            And({p}, {q}, Not({r}), Not({s}), Not({t}), {u}, {v}, {w}),
            And({p}, {q}, Not({r}), Not({s}), {t}, Not({u}), {v}, {w}),
            And({p}, {q}, Not({r}), Not({s}), {t}, {u}, Not({v}), {w}),
            And({p}, {q}, Not({r}), Not({s}), {t}, {u}, {v}, Not({w})),
            And({p}, {q}, Not({r}), {s}, Not({t}), Not({u}), {v}, {w}),
            And({p}, {q}, Not({r}), {s}, Not({t}), {u}, Not({v}), {w}),
            And({p}, {q}, Not({r}), {s}, Not({t}), {u}, {v}, Not({w})),
            And({p}, {q}, Not({r}), {s}, {t}, Not({u}), Not({v}), {w}),
            And({p}, {q}, Not({r}), {s}, {t}, Not({u}), {v}, Not({w})),
            And({p}, {q}, Not({r}), {s}, {t}, {u}, Not({v}), Not({w})),
            And({p}, {q}, {r}, Not({s}), Not({t}), Not({u}), {v}, {w}),
            And({p}, {q}, {r}, Not({s}), Not({t}), {u}, Not({v}), {w}),
            And({p}, {q}, {r}, Not({s}), Not({t}), {u}, {v}, Not({w})),
            And({p}, {q}, {r}, Not({s}), {t}, Not({u}), Not({v}), {w}),
            And({p}, {q}, {r}, Not({s}), {t}, Not({u}), {v}, Not({w})),
            And({p}, {q}, {r}, Not({s}), {t}, {u}, Not({v}), Not({w})),
            And({p}, {q}, {r}, {s}, Not({t}), Not({u}), Not({v}), {w}),
            And({p}, {q}, {r}, {s}, Not({t}), Not({u}), {v}, Not({w})),
            And({p}, {q}, {r}, {s}, Not({t}), {u}, Not({v}), Not({w})),
            And({p}, {q}, {r}, {s}, {t}, Not({u}), Not({v}), Not({w}))
        )))"""


def get_kth_element(k, c, n, m):
    """
    Find the kth element(when matrix is flattened) of a nxm matrix in it's previous generation.

    Args:
        k (int): Element number when matrix is flattened.
        c (int): Current generation.
        n, m (int): Matrix Dimensions.

    Returns:
        int: kth element.

    """
    # Create a matrix with elements in the format "c{i+1}_{j+1}_{c-1}"
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            element = f"c{i+1}_{j+1}_{c-1}"
            row.append(element)
        matrix.append(row)
    # Flatten the matrix into a single list
    flattened_matrix = [element for row in matrix for element in row]

    # Check if k is a valid index
    if k < 1 or k > len(flattened_matrix):
        return "Invalid index"

    # Return the k-th element (index k-1) from the flattened matrix
    return flattened_matrix[k-1]


def smt_expression(o, arr, n, m):
    """
    Generate a satisfiability (SAT) expression string based on the given parameters.

    Args:
        o (int): The value of 'o' used in the expression generation.
        arr (list): A list of elements used in the expression generation.
        n (int): Parameter 'n' used in the 'generate_neighboring_cells' function.
        m (int): Parameter 'm' used in the 'generate_neighboring_cells' function.

    Returns:
        str: The generated SAT expression string in the format 'And(clause1,clause2,...)'.
    """

    clauses = []  # List to store generated clauses
    o += 1  # Increment the value of 'o' by 1

    while o > 1:
        for index, element in enumerate(arr):
            # Generate neighboring cells and convert to a clause
            a, b, c, p, q, r, s, t, u, v, w = generate_neighboring_cells(
                index + 1, o, element, n, m)
            clause = to_clause(a, b, c, p, q, r, s, t, u, v, w)
            clauses.append(clause)  # Add the clause to the list of clauses

        o -= 1  # Decrement the value of 'o' by 1

    # Join all clauses with commas and wrap with 'And()' to create the final expression
    return 'And(' + ','.join(map(str, clauses)) + ')'


if __name__ == "__main__":

    # Declare Boolean variables
    c1_1_0, c1_2_0, c2_1_0, c2_2_0, c1_1_1, c1_2_1, c2_1_1, c2_2_1, c1_1_2, c1_2_2, c2_1_2, c2_2_2, h = Bools(
        'c1_1_0, c1_2_0, c2_1_0, c2_2_0, c1_1_1, c1_2_1, c2_1_1, c2_2_1, c1_1_2, c1_2_2, c2_1_2, c2_2_2, h')

    # Set initial values for some variables
    c1_1_2 = False
    c1_2_2 = False
    c2_1_2 = False
    c2_2_2 = False

    # Generate the SAT expression
    smt_expr = smt_expression(2, [c1_1_2, c1_2_2, c2_1_2, c2_2_2], 2, 2)

    # Create a Z3 solver
    solver = Solver()

    # Add constraints to the solver
    solver.add(
        And(
            eval(smt_expr) == True,
            c2_2_0 == False,
            c1_1_0 == False,
            c1_2_0 == False,
            c2_1_0 == True
        )
    )

    # Check satisfiability
    if solver.check() == sat:
        model = solver.model()
        print(model)
        print("Satisfiable!")
    else:
        print("Unsatisfiable!")
