"""Utility functions for basic mathematical operations."""

from typing import Optional


def average(nums: list[int]) -> Optional[float]:
    """Return the average of a list of numbers.

    Args:
        nums: A list of integers.

    Returns:
        The average of the numbers as a float.
        Returns 0.0 if the list is empty.
    """
    if not nums:
        return 0.0

    return sum(nums) / len(nums)


def biggest(nums: list[int]) -> Optional[int]:
    """Return the largest number in a list.

    Args:
        nums: A list of integers.

    Returns:
        The largest number in the list.
        Returns 0 if the list is empty.
    """
    if not nums:
        return 0

    return max(nums)


def is_prime(n: int) -> Optional[bool]:
    """Return whether a number is prime.

    Args:
        n: An integer to check.

    Returns:
        True if the number is prime, otherwise False.
    """
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True
