"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    ### TODO
  if x <= 1:
    return x
  else:
    ra = foo(x-1)
    rb = foo(x-2)
    return ra + rb
    pass

def longest_run(mylist, key):
    ### TODO
  max_run_length = 0
  current_run_length = 0
  for num in mylist:
    if num == key:
      current_run_length += 1
      if current_run_length > max_run_length:
        max_run_length = current_run_length
    else:
      current_run_length = 0
  return max_run_length
    
  



class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    

def to_value(v):
    """
    if it is a Result object, return longest_size.
    else return v
    """
    if type(v) == Result:
        return v.longest_size
    else:
        return int(v)
        
def longest_run_recursive(mylist, key):
    ### TODO
  if len(mylist) == 0:
    return Result(0,0,0,True)
  elif len(mylist) == 1:
    if mylist[0] == key:
      return Result(1,1,1,True)
    else:
      return Result(0,0,0,False)

  mid = len(mylist) // 2
  left_half = mylist[:mid]
  right_half = mylist[mid:]

  left_result = longest_run_recursive(left_half, key)
  right_result = longest_run_recursive(right_half, key)

  is_entire_range = left_result.is_entire_range and right_result.is_entire_range and left_result.right_size + right_result.left_size == len(mylist)

  cross_run = 0
  if left_half[-1] == key and right_half[0] == key:
        cross_run = left_result.right_size + right_result.left_size

  longest_size = max(to_value(left_result.longest_size), to_value(right_result.longest_size), cross_run)

  left_size = left_result.left_size if left_result.is_entire_range else left_result.left_size
  right_size = right_result.right_size if right_result.is_entire_range else right_result.right_size

  if left_half[-1] == key and left_result.is_entire_range:
        left_size += right_result.left_size
  if right_half[0] == key and right_result.is_entire_range:
        right_size += left_result.right_size


  return Result(left_size, right_size, longest_size, is_entire_range)




  
  



