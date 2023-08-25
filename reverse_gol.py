from z3 import *

def reverse_gol(input_array, output_variables, k_range, n, m, k):


    def generate_neighboring_cells(k, o, ca_b_c, n, m):
        """
        Generate neighboring cells in previous generation based on given parameters.

        Args:
            k (int): Index of the element.
            o (int): Offset value.
            ca_b_c (str): Input element string.
            n (int): Number of rows.
            m (int): Number of columns.

        Returns:
            tuple: Tuple containing the generated expressions.
        """
        e = get_kth_element(k, o, n, m)
        a, b, c = map(int, e[1:].split('_'))
        p = f'c{a - 1}_{b - 1}_{c - 1}' if a - 1 != 0 and b - 1 != 0 and c - 1 >= 0 else 'h'
        q = f'c{a - 1}_{b}_{c - 1}' if a - 1 != 0 and c - 1 >= 0 else 'h'
        r = f'c{a - 1}_{b + 1}_{c - 1}' if a - 1 != 0 and b + 1 <= m and c - 1 >= 0 else 'h'
        s = f'c{a}_{b + 1}_{c - 1}' if b + 1 <= m and c - 1 >= 0 else 'h'
        t = f'c{a + 1}_{b + 1}_{c - 1}' if a + 1 <= n and b + 1 <= m and c - 1 >= 0 else 'h'
        u = f'c{a + 1}_{b}_{c - 1}' if a + 1 <= n and c - 1 >= 0 else 'h'
        v = f'c{a + 1}_{b - 1}_{c - 1}' if a + 1 <= n and b - 1 != 0 and c - 1 >= 0 else 'h'
        w = f'c{a}_{b - 1}_{c - 1}' if b - 1 != 0 and c - 1 >= 0 else 'h'
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
        p = f'Not({p})'
        q = f'Not({q})'
        r = f'Not({r})'
        s = f'Not({s})'
        t = f'Not({t})'
        u = f'Not({u})'
        v = f'Not({v})'
        w = f'Not({w})'

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
                element = f"c{i + 1}_{j + 1}_{c - 1}"
                row.append(element)
            matrix.append(row)
        # Flatten the matrix into a single list
        flattened_matrix = [element for row in matrix for element in row]

        # Check if k is a valid index
        if k < 1 or k > len(flattened_matrix):
            return "Invalid index"

        # Return the k-th element (index k-1) from the flattened matrix
        return flattened_matrix[k - 1]


    def smt_expression(arr, n, m, k):
        """
        Generate a satisfiability (SAT) expression string based on the given parameters.

        Args:
            k (int): The value of 'o' used in the expression generation.
            arr (list): A list of elements used in the expression generation.
            n (int): Parameter 'n' used in the 'generate_neighboring_cells' function.
            m (int): Parameter 'm' used in the 'generate_neighboring_cells' function.

        Returns:
            str: The generated SAT expression string in the format 'And(clause1,clause2,...)'.
        """

        clauses = []  # List to store generated clauses
        k += 1  # Increment the value of 'o' by 1

        while k > 1:
            for index, element in enumerate(arr):
                # Generate neighboring cells and convert to a clause
                a, b, c, p, q, r, s, t, u, v, w = generate_neighboring_cells(index + 1, k, element, n, m)
                clause = to_clause(a, b, c, p, q, r, s, t, u, v, w)
                clauses.append(clause)  # Add the clause to the list of clauses

            k -= 1  # Decrement the value of 'o' by 1

        # Join all clauses with commas and wrap with 'And()' to create the final expression
        return 'And(' + ','.join(map(str, clauses)) + ')'


    def generate_output_constraints(variables, k_range):
        """
        Generate the output constraints for the SAT solver based on the given variables and k range.

        Args:
            variables (dict): A dictionary containing variable names as keys and their truth values as values.
            k_range (range): The range of k values for which constraints need to be generated.

        Returns:
            str: The generated SAT constraints as a string in the format 'Or(And(constraint1), And(constraint2), ...)'

        """
        s = Solver()

        # Iterate through the specified k range
        for k in range(k_range.start, k_range.stop):
            conjunction = []
            for var_name, var_value in variables.items():
                var = Bool(f"{var_name}_{k}")  # Create a boolean variable with the current k value
                if var_value:
                    conjunction.append(var)  # Add the variable if its truth value is True
                else:
                    conjunction.append(Not(var))  # Add the negation of the variable if its truth value is False
            s.add(And(conjunction))  # Add the conjunction of variables for the current k to the solver

        output_constraints = f'{s}'  # Convert the solver's constraints to a string
        output_constraints = output_constraints[1:-1]  # Remove the outermost parentheses
        output_constraints = f'Or({output_constraints})'  # Wrap the constraints with 'Or()' for SAT solving
        return output_constraints


    smt_expr = smt_expression(input_array, n, m, k)  # Generate the SMT expression based on input parameters
    out = f'And({smt_expr}, {generate_output_constraints(output_variables, k_range)})'  # Combine SMT expression and output constraints
    return out


def generate_combinations(a, b, c):
    """
    Generate a list of formatted combinations based on the given parameters.

    Args:
        a (int): The maximum value for the first index.
        b (int): The maximum value for the second index.
        c (int): The maximum value for the third index.

    Returns:
        str: A comma-separated string containing the formatted combinations.

    """
    combinations = []
    for i in range(1, a + 1):
        for j in range(1, b + 1):
            for k in range(0, c + 1):
                combinations.append(f'c{i}_{j}_{k}')  # Create a formatted combination and add to the list
    return ', '.join(combinations)  # Join the list of combinations into a comma-separated string