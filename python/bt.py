from node import Node                                                            
                                                                                 
class BinarySearchTree:                                                          
   """                                                                           
   Binary Search Tree: left and right child and data of any object               
   """                                                                           
                                                                                 
   def __init__(self):                                                           
      """                                                                        
      Binary Search Tree constructor                                             
      """                                                                        
      self.root = None                                                           
                                                                                 
   def insert(self, data):                                                                                                                          
      """                                                                        
      Insert new Node with data                                                  
      @param data: object to insert                                              
      """                                                                        
      if self.root is None:                                                      
         self.root = Node(data)                                                  
      else:                                                                      
         node = self.root                                                        
         while True:                                                             
            if data < node.data:                                                 
               if node.left is None:                                             
                  node.left = Node(data)                                         
                  break                                                          
               else:                                                             
                  node = node.left                                               
            elif data > node.data:                                               
               if node.right is None:                                            
                  node.right = Node(data)                                        
                  break                                                          
               else:                                                             
                  node = node.right                                              
            else:                                                                
               break                                                                     
                                                                                 
   def find(self, data):                                                         
      """                                                                        
      Find node containing data                                                  
      @param data: object to find                                                
                                                                                 
      @return node if found, None otherwise                                      
      """                                                                        
      if self.root is None:
         return False
      
      node = self.root

      while True:
         if data == node.data:
            return node
         elif data < node.data:
            if node.left is None:
               return None
            else:
               node = node.left
         else:
            if node.right is None:
               return None
            else:
               node = node.right                                                                     
                                                                                 
   def delete(self, data):                                                       
      """                                                                        
      Delete data                                                                
      @param data: content to delete                                             
      """                                                                        
      pass                                                                       


	#Breadth-First Traversal
   def bft(self): #Breadth-First Traversal

      self.root.level = 0 
      queue = [self.root]
      out = []
      current_level = self.root.level

      while len(queue) > 0:
         current_node = queue.pop(0)
         if current_node.level > current_level:
            current_level += 1
            out.append("\n")
         out.append(str(current_node.data) + " ")

         if current_node.left:
            current_node.left.level = current_level + 1
            queue.append(current_node.left)
              
         if current_node.right:
            current_node.right.level = current_level + 1
            queue.append(current_node.right)
                  
        
      print("".join(out))      


   def inorder(self,node):
      if node is not None:
      	self.inorder(node.left)
      	print(node.data)
      	self.inorder(node.right)


   def preorder(self,node):
      if node is not None:
         print(node.data)
         self.preorder(node.left)
         self.preorder(node.right)


   def postorder(self,node):
      if node is not None:
      	self.postorder(node.left)
      	self.postorder(node.right)
      	print(node.data)















if __name__ == '__main__':
	tree = BinarySearchTree()     
	arr = [8,3,1,6,4,7,10,14,13]
	for i in arr:
	    tree.insert(i)
	print('Breadth-First Traversal:')
	tree.bft()
	print('\n')
	print('Inorder Traversal:')
	tree.inorder(tree.root) 
	print('\n')
	print('Preorder Traversal:')
	tree.preorder(tree.root) 
	print('\n')
	print('Postorder Traversal:')
	tree.postorder(tree.root)
	print('\n')
	print('Return 10 in tree if it exist, else return None:')
	print(tree.find(10))