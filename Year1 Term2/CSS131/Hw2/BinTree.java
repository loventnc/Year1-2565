import java.util.Stack;
import java.util.Iterator;
import java.util.NoSuchElementException;

class BinTree<T> implements Iterable<T> {
    BinTree<T> left;
    BinTree<T> right;
    T val;
    
    public Iterator<T> iterator() {
        return new TreeIterator(this);
    }
    private class TreeIterator implements Iterator<T> {
        private Stack<BinTree<T>> s = new Stack<BinTree<T>>();
        TreeIterator(BinTree<T> n) {
            if (n.val != null) s.push(n);
        }
        public boolean hasNext() {
            return !s.empty();
        }
        public T next() {
            if (!hasNext()) throw new NoSuchElementException();
            BinTree<T> n = s.pop();
            if (n.right != null) s.push(n.right);
            if (n.left != null) s.push(n.left);
            return n.val;
        }
        public void remove() {
            throw new UnsupportedOperationException();
        }
    }
    public static void main(String[] args) 
    {
        BinTree<Integer> binaryTree = new BinTree<Integer>();

        binaryTree.val = 1;
        binaryTree.left = new BinTree<Integer>();
        binaryTree.left.val = 2;
        binaryTree.right = new BinTree<Integer>();
        binaryTree.right.val = 3;
        binaryTree.left.left = new BinTree<Integer>();
        binaryTree.left.left.val = 4;
        binaryTree.left.right = new BinTree<Integer>();
        binaryTree.left.right.val = 5;

        for (Integer j : binaryTree) {
            System.out.println(j);
        }
    }
}