def exponentialListCheck(nums_list):
        """Solution Code"""
        for i in range(0, len(nums_list) - 1):
               if (nums_list[i] < nums_list[i + 1]) != True:
                      return False
        return True
