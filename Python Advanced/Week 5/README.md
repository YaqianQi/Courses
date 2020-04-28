# Week 4
## Advanced Python Features 
1. **Magic Methods**: can directly apply to object 
   - __init__
   - __len__
   - __getitem__
   - __contains__
   - __call__
2. **Inheritance** 
   - attributes 
   ```
   class B(A):
      def __init__(self):
          super().__init__()
   ```
   - methods 
   ```
   class B(A):
     super().function()
   ```
3. **isinstance, object-oriented programming**
   - **isintance()**: take inheritance into count type 
     - type() is good, but it doesn't put inheritance as count 
   - **Polymorphism**: make the object more concise and easy to understand 
   - **encapsulation**: create methods to access the attributes  
4. **Exceptions and inheritance** 
   - issubclass(ValueError, Exception)
   ```
   class NetworkError(Exception):
          pass
   raise NetworkError("Connection is lost")
   ```
5. **Decorators** 
   - **How to use it** 
   ```
   def decorater_func(func):
       def new_func(x):
           print("add something")
           return x
       return new_func
   @decorater_func 
   func(arg1, arg2)
   
   ```
   - **Common decorator**
     - @x.setter: set the attribute without call function 
     - @property: return property 
  ```
   @property
    def name(self):
        print("Access Name")
        return self._name
    @name.setter
    def name(self, new_name):
        print("Change Name")
        if not isinstance(new_name, str):
            raise TypeError("New name must be a string")
        self._name = new_name 
  class_name().name #return self._name
  class_name().name = 'Gorge' #change self._name = "Gorge"
  ```
6. **Functions with variable number of arguments**
   - args,
     - pass everything in tuple 
     - *args: iterable 
     - args: tuple 
  ```
  def my_print(x, y, *args):
      # all other documents are packed in tuple 
      print(type(args))
      print(*args)
      print("MY_PRINT", x, y, args)
  ```
   - kwargs
     - dictionary 
     - pass unknown numbers of keywords 
     ```
       def my_print(*args, **kwargs):
          # all other documents are packed in tuple 
          print(type(kwargs)) #<class 'dict'>
          print("MY_PRINT", args, kwargs) # MY_PRINT (1, 2, 3) {'c': 3, 'd': 4}
          print("MY_PRINT", *args, sep=" $$$ ") # MY_PRINT $$$ 1 $$$ 2 $$$ 3
          
       def deprecated(func):
          def new_func(*args, **kwargs):
              print("The function is deprecated")
              return func(*args, **kwargs)
          return new_func
     ```


   
   
   
