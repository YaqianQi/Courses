# Variable, reference, mutability 
1. Basic 
   - Python store objects in reference 
   - **Immutable**:
     - int, boolean, float, string, tuple
   - **mutable**:
     - list, set, dictionary
     - When the variable changed, it assigned other reference to the variable, it doens't change the original reference number
     - when you pass the value to other variable, you pass reference
     - **Deep copy** if you want to modified value without affacting original value in mutable variables. 
     ```import copy; copy.deepcopy();````
2. **Sets**
   - A set is an unordered container of hashable objects.
      - Ordered container like list, tuple can get access to the value by index
      - Set can not get access to by the index. Hashtable under the hood.
   - Store unique value 
     - Index is number/list/object.., value is True or False
     - add: change value to True; remove change value to False
      - Collison: append to the list of chain whose index = value % size_len (hash function: transform values in non-negative integer)
   - Pros:
     - fast search
     - remove duplicates 
   - Cons:
     - unordered container 
     - no mutable object: because the set stores in linkedlist(can not store list, dictionary, tuple)    
    ```
   daily_log = [
       '[time1] 2 add_to_wish_list',
       '[time2] 1 buy',
       '[time3] 2 setting',
       '[time1] 0 setting',
   ]

   uids = [int(x.split()[1])for x in daily_log]
   unique_ids = set()

   # initialize by {} but no empty 
   set2 = {x for x in range(2)}
   for uid in uids:
       # add method
       unique_ids.add(uid)
       print(f'user id: {uid}; unique ids: {unique_ids}')
   # size of the set 
   len(unique_ids)

   unique_ids.remove(2)

   # dont delete one by one 
   unique_ids.clear()
    ```
   - Search performance: set vs list
      - set is much faster than list 
      - use "in" to check something instead of loop
   - Arithmetic operations over sets  
   ```
   daily_users = {0,2,5}
   all_users = {0,1,2,3,4}
   # find users does not in all users 
   daily_users - all_users
   # user appears in two set 
   daily_users & all_users
   # set union 
   all_users | daily_users
   # update set 
   all_users |= daily_users
   # inplace |=, &=,-=
   # set and other type of container 

   daily_users = [0,2,5,0,5,7]
   all_users = {0,1,2,3,4}
   # Below special methods can use to deal with all kinds of container in very fast way
   # union 
   all_users.union(daily_users)
   # | update
   all_users.update(daily_users)
   # & intersection 
   all_users.intersection(daily_users)
   # &= intersection update 
   all_users.intersection_update(daily_users)
   # -= difference 
   # -= difference update 
   ```
