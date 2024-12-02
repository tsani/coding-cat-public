def exponentialListCheck(nums_list):
        for i in range(0, len(nums_list) - 1):
               if (nums_list[i+1] < nums_list[i]) != True:
                      return False
        return True
