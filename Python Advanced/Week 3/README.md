# Week 3
## Error handling 
1. **The importance of error handling**
   - **Value Error** 
   - **Index Error** : the index doesn't exist 
   - **Logic Error**: no error shows up but we know it's error 
2. **Introduction to exceptions**
   - **Raise Error** 
      ```
      raise ValueError("ValueError: invalid literal for int() with base 10: 'I998'")
      ```
   - **try; except; else**: try to do something, if error goes to except, if no error goes to else 
      ```
      try:
           parse("Goolge 1998 yes") # to do something 
      except (ValueError, IndexError):
          print("parsing failed") # if error do something 
      else:
          print("year: ", year) # if no error do something 
      print("Keep going")
      ```
 3. **Exception objects**
    - Error stores in object 
      ```
      err = ValueError("Some message")
      #raise ValueError("The year was spelled incorreclty") from err
      raise ValueError(f'The year was spelled incorreclty. Reason:{err}') from None
      ```
 4. **The "except Exception" pattern**
     - It's good that the function return some statistic with it 
     
      ```
      try:
           record = parse(raw_info)
           #except ValueError:
           # In more general case, we can name it just exception 
           except Exception:
               fail_count += 1
               continue 
           result.append(record)
      ```
5. **Error messge**
   - Data Type not match: `ValueError`
   - Data do not match length: `IndexError`
   - Can not read error in json: `json.JSONDecodeError`
## Advanced for-loop
1. **map**: apply the operation to each items in container  
   - **map(function, container)** #   `map(preprocess, queries)`
   ``` 
      Will be empty after one exucution 
      numbers = map(lambda x: x**2, range(3))
      print(*list(map(lambda x: x**2, numbers)), sep=',', end='|')
      print(*list(map(lambda x: x**2, numbers)), sep=',')
   ```
   - **Lazy evaluation**: an evaluation strategy which holds the evaluation of an expression until its value is needed. The iterator stops when the shortest input iterable is exhausted.
   `map at 0x115fdeef0>`
 2. **enumerate, zip** 
   - When you want to use for loop 
      - **map**: over modified iterms of some iterable 
      - **enumerate**: if you need indices, only values 
      - **zip**: iterate serveral item at once 
      - **generative expression**: if you need lazy version of list comprehensions 
 3. **Iterators**
   - **Definition**: special object let you iterate over the content just once. 
   ```
   it = iter(a) # initialize an iterator will ends until the end 
   x = it.next() # the iterator was pointing to the first item 
   x = it.next() # the iterator 
   ```
   - Iterators are iterable: you can also apply iterator to iterator. No new object was created  

   - application: data is large and hard to fit in memmory. Can ues special lib to return iterator
     - itertools: iterate the table, content instead of download all table  
   - map, enumerate, zip are all iterator. 
```
```
 4. **Functional Programming**
   - zip  `# zip('ABCD', 'xy') --> Ax By`
   - zip_longest `# zip_longest('ABCD', 'xy', fillvalue='-') --> Ax By C- D-`
   - yeild: when an iterator yields (= returns) , you can imagine this item as "consumed". So the next time the iterator is called, it yields the next "unconsumed" item.
   ```
   1st 
   def zip(*iterables):
    # zip('ABCD', 'xy') --> Ax By
    sentinel = object()
    iterators = [iter(it) for it in iterables]
    while iterators:
        result = []
        for it in iterators:
            elem = next(it, sentinel)
            if elem is sentinel:
                return
            result.append(elem) 
        yield tuple(result)
        
   
   2nd
   list(zip(*[iter(s)]*n))
   for start in range(0,len(L),chunk_size): # xrange() in 2.x; range() in 3.x
      end = start + chunk_size
      print (L[start:end]) # three-item chunks
   ```
 ## File
 1. **File Paths** 
   - File are stored in file system `import os`
   - path format 
     - Windows 'C:\\Users\\aliciaqi\\Desktop'
     - linux: '/home/aliciaqi/Desktop'
     - macOs: '/Users/aliciaqi/Desktop'
   - common syntax 
      - current work directory: `os.getcwd()`
      - current work directory file list: `os.listdir()`
      - other file list: `os.listdir('/Users/aliciaqi/Desktop/trepp-ds')`
      - get abs file path: os.path.abspath('Summary .ipynb')
2. **Reading from files, writing to files**
  - **Read File** 
  ```
  with open("words.txt") as f: # default as read 
    print(f.readlines())
  ```
  - **Write file** 
  ```
  with open("words.txt", 'w') as f: 
      for word in word_lst:
         f.write(word)
  ```
3. **JSON** 
   - Json is a very popular textual format. when you dump your data, you get a text, a stream. 
   - Data format: enable devices and programming languages to communicate each other regardless of what programming languages are used. 
   - data type: 
     - int `json.loads(x)`
     - float `json.loads(x)`
     - string: has to be double quotes `json.loads("abc")`
     - boolean:  `json.loads("true")`
     - list: `json.loads('["abc", 1, 3]')`
     - mapping: key has to be string (double quote) `json.loads("{ "a" : 13 }")
     - json.dumps(something) 
  - operation to file 
    - json.load: read  
    - json.dump: download(write) to somewhere  
    
    ```
    with open("request.json" , 'w') as f:
         json.dump(request, f)
         
    with open("request.json") as f:
         x = json.load(f) # only suitable for one line 
         for line in f:
            print(line) # for multiple line 
    ```
## HW Summary 
1. **map**: apply operation to container. `map(function, container)`
2. **filter**: only return match value. `filter(function, container)` 
3. **sorted**: `sorted(container, key=lambda x:x[i], reverse=?)`
4. **zip**: merge 2 list together into lazy entity.`zip(list1, list2)`
5. print list in elegent way: `print(*list, sep="\n")` 
6. **Json** 
   - open jason file and read line 
     ```
     with open("file.json") as f:
          for line in f:
            print(line) 
     ```
   - store the value to json file 
   ````
      with open("file.json", 'w') as f
           json.dump(jason_str, f) 
   ````
7. **Error**:
   - Value doesn't match: `Except ValueError`
   - Can't read: `json.JSONDecodeError`
8. **Functional Programming:**
   - **defaultdict** 
   ```
   from collection import defaultdict
   word_dict = defaultdict(int/dict/[]) 
   word_dict[key] = 1 # automatic set it to the type you want without "if not existed then" initialization 
   ```
   
