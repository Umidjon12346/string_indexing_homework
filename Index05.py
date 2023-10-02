import string
def main(s):
    """
    Given a variable s string of length five. Determine the number of digits involved in this variable.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    digit = string.digits
    return str(s.count(digit))
print(main("12345"))