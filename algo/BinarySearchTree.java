/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package algodatastructs;

/**
 *
 * @author varun
 */
class BinaryNode {
  
  Comparable element;
  BinaryNode left;
  BinaryNode right;
    
  BinaryNode (Comparable element)
  {      
    this.element = element;
    left = right = null;  
  }
    
    
}

public class BinarySearchTree {
    
  protected BinaryNode root;
  
  public BinarySearchTree()
  { root = null; }
  
  /**
   * 
   * @param n1 - Root node of tree 1 to compare elements from
   * @param n2 - Root node of tree 2 to compare elements from
   * @return - True if both trees contain exact same elements.
   *           Assumes no duplicates
   */
  public boolean compareElements(BinarySearchTree t1, BinarySearchTree t2)
  {
      return getSize(t1.root) == getSize(t2.root) && 
              compareElementsHelper(t1.root, t2.root);
  }
  
  
  private int getSize(BinaryNode n1)
  {      
    if (n1 == null) 
        return(0);  
    return getSize(n1.left) + getSize(n1.right) + 1 ;       
  }
  
  private boolean compareElementsHelper(BinaryNode n1, BinaryNode n2)
  {
    if(n1 == null)
        return true;
    else if(findElement(n1.element, n2) == null)
        return false;
    else    
        return compareElementsHelper(n1.left, n2) && 
                compareElementsHelper(n1.right, n2);                      
  }
  

  private BinaryNode findElement(Comparable element, BinaryNode t)
  {
      while (t!= null)
      {
          if(element.compareTo(t.element) < 0)
              t = t.left;
          else if(element.compareTo(t.element) > 0)
              t = t.right;
          else
              return t;                //Found
      }
      return null;                   //Not Found
  }
    
}
