class Node:    
   """            
   Binary Search Tree Node    
   """         
                  
   def __init__(self, data):              
      """                                
      Node constructor     
      """                 
      self.left = None              
      self.right = None             
      self.data = data      
      self.level = None #level none defined       
                              
   def __str__(self):     
      return str(self.data) #return as string    
