"""
Given n ropes of different lengths represented by an array of integers, connect them all into a single rope in a way that minimizes the cost of connecting them.

The cost of connecting two ropes is equal to sum of their lengths. We want to minimize the cost of connecting all the ropes.

Input: ropes, [Integer]
Output: Integer

EXAMPLE:
In: [4, 3, 2, 6]
Out: 29


1 1 1 1 1 1
2

Explanation:

First we connect 3 + 2 = 5, giving the following ropes: [4,5,6]
Then we connect 5 + 4 = 9, giving the following ropes: [9,6]
Then we connect 9 + 6 = 15, giving the final combination of all ropes: [15]

So in total the cost for the most efficient approach is: 5 + 9 + 15 = 29

A less efficient way would be:

First we connect 4 + 6 = 10, giving the following ropes: [10,3,2]
Then we connect 10 + 3 = 13, giving the following ropes: [13,2]
Then we connect 13 + 2 = 15, giving the final combination of all ropes: [15]

So in total the cost for the less efficient approach is: 10 + 13 + 15 = 38

Although in both cases we need to make the same number of connections, the costs are different


arr = [4, 3, 2, 6]

heapifyed_array = [2, 3, 4, 6] [4, 5, 6] [6, 14]

first = heap.pop() # 6
second = heap.pop() # 14
14
result += first + second #  6 + 14
heap.push(result)
[6, 14]

def
  result = 0
  heapify(arr)

  while len(arr) > 1:
    first = heap.pop()
    second = heap.pop()
    result += first + second
    heap.push(first + second)

  return result

"""
import heapq


def n_ropes(arr):
	heapq.heapify(arr)
	result = 0
	while len(arr) > 1:
		first = heapq.heappop(arr)
		second = heapq.heappop(arr)
		result += first + second
		heapq.heappush(arr, first + second)
	return result

# print(n_ropes([4, 3, 2, 6]))
# print(n_ropes([1, 1, 1, 1]))
