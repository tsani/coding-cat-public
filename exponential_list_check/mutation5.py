def exponentialListCheck(nums_list):
        for i in range(0, len(nums_list)):
               if (nums_list[i] < nums_list[i + 1]) != True:
                      return False
        return True
