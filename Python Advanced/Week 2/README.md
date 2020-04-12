# Week 2
## Dictionary - Extra Methods 
1. dict.get
   - return None for non-existent key 
     ```
     # set priority to default if not existed  
     priority = rubric_info.get('priority', DEFAULT_PRIORITY)
     ````
2. dict.update, dict.setdefault 
```
d1 = {10:{'name': 'stadium', 'priority': 8}}
d2 = {20:{'name': 'stadium', 'priority': 9,'cafe':110},
      30:{'name': 'stadium', 'priority': 120},
     }
for k, v in d2.items():
    d1.setdefault(k,{}).update(v)
```
## Sorting 
1. tuple sort: sort first item, if equal then second..
   - Inplace: return the same list 
   - out-of-place: create a new list 
    ```
    purchase_count = [
        (5,'b'),
        (9,'j'),
        (9,'a')
    ]
    sorted(purchase_count)
    sorted(purchase_count,reverse=True)

    purchase_count.sort()
    purchase_count.sort(reverse=True)
    ```
    - sort based on value 
    ```
    def get_count(item):
        return items[item]

    sorted(items, key=get_count, reverse=True)
    ```
    - sort and return sorted index 
    
    ```
    def priority(idx):
        return purchase_count[idx]
    sorted(range(len(purchase_count)), key=priority, reverse=True)
    ```
    - Operation
    ```
    max(items, key=get_count)
    min(items, key=get_count)
    ```
2. Lambda Function: one line function
 ```
  sorted(items, key=lambda x:items[x], reverse=True)
 
  lambda_add = lambda a,b: a+b
  lambda_add(3,4)
 ```
3. Sort Summary 
  - Basic sort
    ```
    sorted([5, 2, 3, 1, 4])  # [1, 2, 3, 4, 5]
    a.sort()
    ```
  - Key Function 
    ``` 
    sorted("This is a test string from Andrew".split(), key=str.lower)
    
    student_tuples = [
    # (name, grade, age)
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
  ]
    sorted(student_tuples, key=lambda student: student[2])   # sort by age
    # [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
    ```
  - Operator Module Function
  ```
  from operator import itemgetter
  # sort based on 2 pos 
  sorted(student_tuples, key=itemgetter(2))
  # [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
  
  # sort based on grade and age 
  sorted(student_tuples, key=itemgetter(1, 2))
  # [('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]
  ```
  - Ascending and Descending
  ```
  sorted(student_tuples, key=itemgetter(2), reverse=True)
  # [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
  ```
  - Sort Stability: when multiple records have the same key, their original order is preserved.
  ```data = [('red', 1), ('blue', 2), ('red', 2), ('blue', 1)]
  sorted(data, key=itemgetter(0))
  # [('blue', 2), ('blue', 1), ('red', 1), ('red', 2)]
  ```
  

