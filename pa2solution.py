from __future__ import print_function
# in case you wish to use python2, but I strongly prefer that you use python3
import sys
import random

# NAME: Zanqing Feng
# STUDENT ID NUMBER: 102077587
# On my honor as a University of Colorado Boulder student, I have not received any unauthorized help.
# I also realize that plagiarizing code defeats the purpose of an assignment like this and that the
# instructors and TAs have very sophisticated approaches to finding such plagiarism that can defeat
# things like renaming variables or rearranging statements.
#
# Acknowledged By: __ your name here __


def free_time_intervals(interval_lst, T):
    # First design the algorithm on pen/paper before you attempt this
	if not interval_lst:
		return []
	pairs = []
	res = []
	start = 0
	for interval in interval_lst:
		pairs.append((interval[0], 0))
		pairs.append((interval[1], 1))
	pairs.sort(key = lambda v : v[0])
	stack = []
	for key, flag in pairs:
		if flag == 0:
			stack.append(key)
			if len(stack) == 1:
				if start < key:
					if key <= T:
						res.append((start, key))
					else:
						res.append((start, T))
						return res
		else:
			stack.pop()
			if len(stack) == 0:
				start = key
				if start >= T:
					break
	if start < T:
		res.append((start, T))
	return res

def max_logged_in(interval_lst,T):
    # First design the algorithm on pen/paper and solve a few examples.
	if not interval_lst:
		return (0, 0)
	pairs = []
	max_num, max_time = 0, 0
	for interval in interval_lst:
		pairs.append((interval[0], 0))
		pairs.append((interval[1], 1))
	pairs.sort(key = lambda v : v[0])
	stack = []
	for key, flag in pairs:
		if flag == 0:
			if key >= T:
				break
			stack.append(key)
			if max_num < len(stack):
				max_num = len(stack)
				max_time = key
		else:
			stack.pop()
	return (max_num, max_time)



if __name__ == '__main__':
    #Test Cases

    lst1 = [(5,15)]
    print('Input:', lst1)
    print(free_time_intervals(lst1,30))
    print(max_logged_in(lst1,30))

    lst2 = [(1,3), (2,8),(3,6), (2,6), (10,15), (12,17), (19,23), (27,35)]
    print('Input (corner-case):', lst2)
    print(free_time_intervals(lst2,30))
    print(max_logged_in(lst2,30))

    lst3 = [(5,15), (18,25), (3,12), (4, 11), (1,15), (18,19)]
    print('Input:', lst3)
    print(free_time_intervals(lst3,30))
    print(max_logged_in(lst3,30))
