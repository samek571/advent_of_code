class Solution:
    '''implement mergsort'''
    def sortArray(self, arr: List[int]) -> List[int]:
        
        def merge(left_half, right_half):
            # Initialize the merged array
            merged_arr = []
            
            # Initialize indices for left_half, right_half, and merged_arr
            left_index = 0
            right_index = 0
            
            # Compare the elements at the current indices of left_half and right_half
            # and append the smaller element to merged_arr
            while left_index < len(left_half) and right_index < len(right_half):
                if left_half[left_index] <= right_half[right_index]:
                    merged_arr.append(left_half[left_index])
                    left_index += 1
                else:
                    merged_arr.append(right_half[right_index])
                    right_index += 1
            
            # Append any remaining elements in left_half or right_half to merged_arr
            while left_index < len(left_half):
                merged_arr.append(left_half[left_index])
                left_index += 1
            while right_index < len(right_half):
                merged_arr.append(right_half[right_index])
                right_index += 1
            
            return merged_arr


        # Base case: if the array has only one element, it's already sorted
        if len(arr) <= 1:
            return arr
        
        # Find the midpoint of the array
        mid = len(arr) // 2
        
        # Split the array into two halves
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        # Recursively call merge_sort on each half
        left_half = self.sortArray(left_half)
        right_half = self.sortArray(right_half)
        
        # Merge the sorted halves
        return merge(left_half, right_half)
    
    
