#!/usr/bin/python3
"""The Module for Prime Game"""


def isWinner(x, nums):
    """
    Function Determines the winner of a set of prime number removal games.

    Args:
        x (int variable): The number of rounds.
        nums (list of int): A list of integers where each integer n denotes
        a set of consecutive integers starting from 1 up to and including n.

    Returns:
        str: The name of the player who won the most rounds (either "Ben"
        or "Maria").
        None: If the winner cannot be determined.

    Raises:
        None.
    """
    # This Checks for invalid input
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None
    # This Initializes scores and array of possible prime numbers
    ben = 0
    maria = 0
    # Create a list 'a' of length sorted(nums)[-1] + 1 with all elements
    # initialized to 1
    a = [1 for x in range(sorted(nums)[-1] + 1)]
    # first two elements of the list, a[0] and a[1], are set to 0
    # because 0 and 1 are not prime numbers
    a[0], a[1] = 0, 0

    for i in range(2, len(a)):
        rm_multiples(a, i)
    # Play each round of the game
    for i in nums:
        # If the sum of prime numbers in the set is even, Ben wins
        if sum(a[0:i + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1
    # This Determines the winner of the game
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None


def rm_multiples(ls, x):
    """
    Function
    Removes multiples of a prime number from an array of possible prime
    numbers.

    Args:
        ls (list of int): An array of possible prime numbers.
        x (int variable): The prime number to remove multiples of.

    This Returns:
        None.

    Raises:
        None.
    """
    # loop iterates over multiples of a prime number and marks them as
    # non-prime by setting their corresponding value to 0 in the input
    # Thelist ls. Starting from 2, it sets every multiple of x up to the
    # Thelength of ls to 0.if the index i * x is out of range for the list ls,
    for i in range(2, len(ls)):
        try:
            ls[i * x] = 0
        except (ValueError, IndexError):
            break
