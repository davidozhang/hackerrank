class Solution:
	# @param a : list of list of integers
	# @return a list of list of integers
	def diagonal(self, a):
	    result = []
	    column = 0
	    row =0
	    n = len(a[0])
	    while column <= n-1 and row <= n-1:
	        temp = []
	        traverse_column, traverse_row = column, row
	        while traverse_column >=0 and traverse_row <= n-1:
	            temp.append(a[traverse_row][traverse_column])
	            traverse_column -= 1
	            traverse_row += 1
	        result.append(temp)
	        if column < n-1:
	            column += 1
	        elif column == n-1:
	            row += 1
	    return result
