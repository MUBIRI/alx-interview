#!/usr/bin/python3


""" In a text file, there is a single character H. Your text editor can execute  two operations in this file: Copy All and Paste. Given a number n, This is  a method that calculates the fewest number of operations needed to result in exactly n H characters in the file."""

def minOperations(n):
    ops_count = 0 
    done = 2

    while n > 1:
        while n % done == 0:
            ops_count += done

            n /= done
        done += 1
    return ops_count
