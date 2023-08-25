from reverse_gol import reverse_gol, generate_combinations
from z3 import *

if __name__ == "__main__":

    # Declare Boolean variables
    c1_1_0, c1_2_0, c2_1_0, c2_2_0, c1_1_1, c1_2_1, c2_1_1, c2_2_1, c1_1_2, c1_2_2, c2_1_2, c2_2_2, h = Bools(
        'c1_1_0, c1_2_0, c2_1_0, c2_2_0, c1_1_1, c1_2_1, c2_1_1, c2_2_1, c1_1_2, c1_2_2, c2_1_2, c2_2_2, h')

    # Set initial values for some variables(input board values and values for other boards' cells(optional))
    c1_1_2 = True
    c1_2_2 = True
    c2_1_2 = True
    c2_2_2 = True

    # Create a Z3 solver
    solver = Solver()
    reverse_gol_expr = reverse_gol([c1_1_2,c1_2_2,c2_1_2,c2_2_2], {'c1_2': True,'c2_2':True, 'c1_1': True,'c2_1': False},
                                     range(0, 3), 2, 2, 2)
    # Add constraints to the solver
    solver.add(And(eval(reverse_gol_expr) == True))

    # Check satisfiability
    if solver.check() == sat:
        model = solver.model()
        print(model)
        print("Satisfiable!")
    else:
        print("Unsatisfiable!")
