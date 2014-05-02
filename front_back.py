def front_back(str):
  
   str_list = list(str)
   str_list[0], str_list[-1] = str_list[-1], str_list[0]
   return ''.join(str_list)
