class Calculation:

    def add(self,x,y):
        if not isinstance(x, int):
          raise TypeError('x must be an integer')

        if not isinstance(y, int):
          raise TypeError('y must be an integer')
          
        return x+y
    
    def minus(self,x,y):
        if x>y:
            return x-y
        else:
            return y-x
    
    def multiply(self,x,y):
        return x*y
    
    def divide(self,x,y):
        if x%y==0:
            return x/y
        
        else:
            return x//y
