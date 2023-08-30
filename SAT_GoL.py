from reverse_gol import reverse_gol, generate_combinations
from z3 import *
import time

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

    reverse_gol_expr = reverse_gol([c1_1_2,c1_2_2,c2_1_2,c2_2_2],
                                   {'c1_2': True,'c2_2':True, 'c1_1': True,'c2_1': False},2, 2, 2)
    formula = eval(reverse_gol_expr)

    # Apply Tactics
    tseitin_cnf_tactic = Tactic('tseitin-cnf')
    cnf_formula = tseitin_cnf_tactic(formula)

    # Add constraints to the solver
    solver.add(formula)

    # Measure solving time(more accurate than solver statistics) and check satisfiability
    start_time = time.time()
    result = solver.check()
    end_time = time.time()

    if result == sat:
        model = solver.model()
        print(model)
        print("Satisfiable!")
    else:
        print("Unsatisfiable!")

    #Elapsed Time
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time} seconds")

    #Solver Statistics
    print(solver.statistics())


    '''Steps to test:
    Step 1: Declare boolean variables.(Note: The function generate_combinations could be useful)
    Step 2: Set initial values of input variables(input board values and values for other boards' cells(optional))
    Step 3: In the definition of reverse_gol_expr, list all the variables of the input board in an array as first
            argument, constraints on output board(as a dict) as second argument, followed by dimensions of input and 
            output matrices(both must have same dimensions and entered with dimension of rows followed by that of 
            columns(both as Int)) and maximum number of allowed generations(Int) assuming 0 is the lowest possible 
            genration in the respective order
    Step 4: Run.'''
