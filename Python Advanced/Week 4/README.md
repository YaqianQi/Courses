# Week 4 
## Classes 
1. Why we need class 
2. Introduction to classes
3. **__init__, object fields**
   - Attach data field/ Attribute to object:
   ```
    class User:
    # constructor 
    def __init__(self, first_name, second_name, age):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age 
    def greet(self, phrase):
        print(f'{phrase} self:self')
        
    def set_name(self, new_name):
        old_name = self.name
        self.name = new_name
        print(f'User: {old_name} --> {new_name}')
        
    def get_name(self):
        # You can still implement if something changes 
        return f'{self.first_name} {self.second_name}'
   ```
   - emphasis the fields directly (do not change it unless by set method)
     ```
        def __init__(self, first_name, second_name, age):
          self._first_name = first_name
          self._second_name = second_name
          self._age = age 
     ```
4. **Class attributes**
   - class variable: shared between all objects of those classes. 
   - pass function manually: map(func, container) 
   ```
   for x in map(str.rstrip, lines): # == for x in map(lambda x: x.rstrip(), lines):
     print(x)
   ```
5. **Exampe of interaction between classes**
   - Design of social network 
   
