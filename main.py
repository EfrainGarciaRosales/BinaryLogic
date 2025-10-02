# Helper functions for boolean logic
def implies(a, b):
    """Computes the logical implication 'a implies b'."""
    return not a or b


def implied_by(a, b):
    """Computes the logical reverse implication 'a is implied by b'."""
    return a or not b


def xor(a, b):
    """Computes the logical exclusive OR."""
    return a != b


# --- The 16 Binary Logic Operations Reference Table ---
# The key (0-15) is the unique integer calculated from an expression's truth table.
# The value is a tuple containing the final answer (Number 1-16) and the operation's name.
LOGIC_OPERATIONS = {
    0: (1, "FALSE"),
    1: (2, "A NOR B"),
    2: (3, "NOT A AND B"),
    3: (4, "NOT A"),
    4: (5, "A AND NOT B"),
    5: (6, "NOT B"),
    6: (7, "A XOR B"),
    7: (8, "A NAND B"),
    8: (9, "A AND B"),
    9: (10, "A XNOR B (Equivalence)"),
    10: (11, "B"),
    11: (12, "A IMPLIES B"),
    12: (13, "A"),
    13: (14, "B IMPLIES A"),
    14: (15, "A OR B"),
    15: (16, "TRUE"),
}


def evaluate_expression(expression_func):
    """
    Evaluates a logic function for all 4 (A, B) inputs to get a unique ID.
    The binary ID is formed from the outputs of (A=T,B=T), (T,F), (F,T), (F,F).
    """
    # Define the four possible input pairs for A and B
    inputs = [(True, True), (True, False), (False, True), (False, False)]

    # Calculate the result for each pair and build a binary string
    binary_string = ""
    for a, b in inputs:
        binary_string += "1" if expression_func(a, b) else "0"

    # Convert the binary string to its integer equivalent (0-15)
    return int(binary_string, 2)


# --- Define the logic expressions from the problem ---
expressions = {
    "(a)": lambda a, b: implied_by(implies(a, b), b or b),
    "(b)": lambda a, b: implied_by(not a and not b, a or (b and not a)),
    "(c)": lambda a, b: implies(a, implies(b, implies(a, implied_by(implied_by(b, a), b)))),
    "(d)": lambda a, b: implies(a, b) and implies(b, a),
    "(e)": lambda a, b: implies(a, b) or implies(not b, not a),
    "(f)": lambda a, b: not a or b and b and a and not b or not b or not a and b,
    "(g)": lambda a, b: xor(a, not b and not implies(b, not (a or b))),
    "(h)": lambda a, b: xor(implies(a, b), implies(not a, b)),
    "(i)": lambda a, b: xor(implies(a, b), not implies(not a, b)),
    "(j)": lambda a, b: implies(xor(a, b), b) or not implies(not a, b),
    "(k)": lambda a, b: implies(a, b) and implied_by(a, b) and (a and b),
}


def solve_and_print_results():
    """
    Solves each expression and prints the result in a formatted way.
    """
    print("--- Logic Expression Solutions ---")
    for label, func in expressions.items():
        # Get the unique ID (0-15) for the expression
        operation_id = evaluate_expression(func)

        # Look up the final answer (1-16) and name from the table
        result_number, result_name = LOGIC_OPERATIONS[operation_id]

        print(f"{label} is equivalent to operation #{result_number} ({result_name})")
    print("--------------------------------")


# Run the solver
if __name__ == "__main__":
    solve_and_print_results()