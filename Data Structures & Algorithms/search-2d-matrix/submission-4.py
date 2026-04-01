class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # brute force, just loop through matrix and find target
        # O(logm * n) this is definitely using binary search.
        # get leading row number (which is the least) and binary search 
        # if target > curr_row but also < next_row, then its in the current row
        # basically binary search which row it is in
        # check if target is the first number too
        l = -1
        r = len(matrix)
        while l < r:
            m = l + (r-l) // 2
            m_len = len(matrix[m])
            least = matrix[m][0]
            greatest = matrix[m][m_len-1]

            if target > greatest:
                l = m+1
            elif target < least:
                r = m
            else:
                # has to be in here!
                for n in matrix[m]:
                    if n == target: return True
                break

            

        return False





        