///////
///////////////////////////
//     DATA STRUCTURES
//////////////////////////
///////

function BinarySearchTree() {
  this.root = null;
}


//inserting val into BST [note -- inserting using BST rules]
BinarySearchTree.prototype.insertNode = function (val) {
  var node = {
    data : val, 
    left : null, 
    right : null
  };

  var currentNode;
  
  if (!this.root) {
    this.root = node;
  } 
  else {
    currentNode = this.root;
    while (currentNode) {
      if (val < currentNode.data) {
          if (!currentNode.left) {
            currentNode.left = node;
            break;
          } 
          else {
            currentNode = currentNode.left;
          }
      } 
      else if (val > currentNode.data) {
        if (!currentNode.right) {
          currentNode.right = node;
          break;
        } 
        else {
          currentNode = currentNode.right;
        }
      } 
      else {
        console.log('Ignoring this value as the BST should not contain duplicate values');
        break;
      }
    }    
  }
};




var BST = new BinarySearchTree();


BST.insertNode(10);
BST.insertNode(15);
BST.insertNode(5);
BST.insertNode(2);
BST.insertNode(3);
BST.insertNode(12);
BST.insertNode(17);
console.log("\n//////////////");
console.log("\nInitializing BinarySearchTree -- inserting items... \n");
console.log(BST);
console.log("\nEnd... \n");





//PreOrder Traversal -- 10,5,2,3,15,12,17

//              10 
//             /   \ 
//            5    15 
//           /    /  \ 
//          2    12  17
//           \ 
//            3



BinarySearchTree.prototype.preOrderTraversal = function (root) {
  console.log(root.data);

  if (root.left) {
    this.preOrderTraversal(root.left);
  } 
  if (root.right) {
    this.preOrderTraversal(root.right);
  }
};


console.log("\n//////////////");
console.log("\nBinarySearchTree -- PreOrder Traversal: \n");
BST.preOrderTraversal(BST.root);
console.log("\nEnd... \n");




//InOrder Traversal -- 2, 3, 5, 10, 12, 15, 17

//              10 
//             /   \ 
//            5    15 
//           /    /  \ 
//          2    12  17
//           \ 
//            3

BinarySearchTree.prototype.inOrderTraversal = function (root) {

  if (root.left) {
    this.inOrderTraversal(root.left);
  } 
  
  console.log(root.data);
    
  if (root.right) {
    this.inOrderTraversal(root.right);
  }
};


console.log("\n//////////////");
console.log("\nBinarySearchTree -- InOrder Traversal: \n");
BST.inOrderTraversal(BST.root); 
console.log("\nEnd... \n");


///////
///////////////////////////
//     SORTING ALGORITHMS
//////////////////////////
///////

//Bubble Sort
function bubbleSort(arr){
   var len = arr.length;
   for (var i = len-1; i>=0; i--){
     for(var j = 1; j<=i; j++){
       if(arr[j-1]>arr[j]){
           var temp = arr[j-1];
           arr[j-1] = arr[j];
           arr[j] = temp;
        }
     }
   }
   return arr;
}
console.log("\n//////////////");
console.log("\nBubbleSort: \n");
console.log("bubbleSort([7,5,2,4,3,9]):  " + bubbleSort([7,5,2,4,3,9])); //[2, 3, 4, 5, 7, 9]
console.log("bubbleSort([9,7,5,4,3,1]):  " + bubbleSort([9,7,5,4,3,1])); //[1, 3, 4, 5, 7, 9]
console.log("bubbleSort([1,2,3,4,5,6]):  " + bubbleSort([1,2,3,4,5,6])); //[1, 2, 3, 4, 5, 6]
console.log("\nEnd...");




///////
///////////////////////////
//     Computational ALGORITHMS
//////////////////////////
///////

//isPrime
function isPrime(n){
//check if n is a multiple of 2
    if (n%2 == 0) {
      return false;
    }
    //if not, then just check the odds
    for(var i=3;i*i<=n;i+=2) {
        if(n%i==0){
            return false;
    }
  }
    return true;

}
console.log("\n//////////////");
console.log("\nisPrime: \n");
console.log("isPrime(2): " + isPrime(2));
console.log("isPrime(3): " + isPrime(3));
console.log("isPrime(7): " + isPrime(7));
console.log("isPrime(137): " + isPrime(137));
console.log("isPrime(237): " + isPrime(237));
console.log("\nEnd...");




//isOdd
function isOdd(n){
//check if n is a multiple of 2
    if (n%2 == 0) {
      return false;
    }
    return true;
  }


console.log("\n//////////////");
console.log("\nisOdd: \n");
console.log("isOdd(2): " + isOdd(2));
console.log("isOdd(3): " + isOdd(3));
console.log("isOdd(7): " + isOdd(7));
console.log("isOdd(10): " + isOdd(10));
console.log("\nEnd...");




//isEven
function isEven(n){
//check if n is a multiple of 2
    if (n%2 == 0) {
      return true;
    }
    return false;
  }


console.log("\n//////////////");
console.log("\nisEven: \n");
console.log("isEven(2): " + isEven(2));
console.log("isEven(3): " + isEven(3));
console.log("isEven(7): " + isEven(7));
console.log("isEven(10): " + isEven(10));
console.log("\nEnd...");





function findEvensInArray(arr){
  var count = 0;
  for(var i=0; i<arr.length; i++){
    if (isEven(arr[i])){
      count++;
    }
  }
  console.log("\nArray [" +  arr + "] has " + count + " even elements");
}

var array = [1,2,3,4,5,6];
findEvensInArray(array);








