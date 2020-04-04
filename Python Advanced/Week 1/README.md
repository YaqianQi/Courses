# Variable, reference, mutability 
1. **Basic** 
   - Python store objects in reference 
   - **Immutable**:
     - varaibles point to object
     - int, boolean, float, string, tuple
   - **mutable**:
     - list, set, dictionary
     - container stores reference 
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
   - Operation: 
     - Within set 
         - len(s)	Return the number of elements in set s (cardinality of s)
         - x in s	Test x for membership in s
         - x not in s	Test x for non-membership in s
         - s.add(x)	Add element x to the set
         - s.remove(x)	Remove element x from the set. Raises KeyError if x is not contained in the set
         - s.discard(x)	Remove element x from the set if it is present
         - s.pop()	Remove and return an arbitrary element from the set. Raises KeyError if the set is empty
         - s.copy()	Return a new set with a shallow copy of s
         - s.clear()	Remove all elements from the set
      - Two set 
        - s == t		Test sets to equality
        - s <= t	s.issubset(t)	Test whether every element in s is in t
        - s < t	s <= t and s != t	Test whether s is a proper subset of ​t
        - s >= t	s.issuperset(t)	Test whether every element in t is in s
        - s > t	s >= t and s != t	Test whether s is a proper superset of t
        - s | t	s.union(t)	Return a new set with elements from s and t
        - s & t	s.intersection(t)	Return a new set with elements common to s and t
        - s - t	s.difference(t)	Return a new set with elements in s that are not in t
        - s ^ t	s.symmetric_difference(t)	Return a new set with elements in either s or t but not both
        - s |= t	s.update(t)	Update s, adding elements from t
        - s &= t	s.intersection_update(t)	Update s, keeping only elements found in it and t
        - s -= t	s.difference_update(t)	Update s, removing elements found in t
        - s ^= t	s.symmetric_difference_update(t)	Update s, keeping only elements found in either set, but not in both
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
  
   # set and other type of container.Below special methods can use to deal with all kinds of container in very fast way 
   daily_users = [0,2,5,0,5,7]
   all_users = {0,1,2,3,4}
   
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
   - Print Items 
     - In some tasks, the answer must be output in ascending order
     ```
     container = {7, 1, 4, 3, 2}
     print(*sorted(container), sep=' ')  # '1 2 3 4 7'
     ```
  3. **Dictionary**
    - **Introduction** 
      - Initialize dictionary 
         - curly braces
            ```
            {'USA':2, 'France':2, "Germany":1}
            ```
         - function dict()
           ```
           dict([('USA',2),('France',2),('France',5),("Germany",1)])
           dict(USA= 2, France = 2, Germany = 1)
           ```
         - the comprehension 
            ```
            {x:0 for x in 'hello!!!!!!!!' if x.isalpha()}
            
            countries = ['USA', 'France', 'Germany']
            counts = [2, 2, 1]
            dict_5 = {
            countries[i]: counts[i]
            for i in range(len(cuntries))
            if counts[i] > 1
            }
            ```
       - Iterate items
         ```
         for x in dictionary // key loop
         for x in dictionary.values() // value loop 
         for k,v in dictionary.items() // value, key pair loop 
         ```
       - Access item: nested dictionary is allowed.  
         ```
         dictionary[ley1][key2]
         ```
       - remove items 
            ``` 
            del dictionary[key]
            dictionary.pop(key)
            dictionary.pop(key,0) # pop value, if not exist return default value 
            dictionary.clear() remove all 

            ``` 
  
