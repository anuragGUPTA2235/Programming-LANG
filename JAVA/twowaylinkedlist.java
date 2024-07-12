package myfirstjava;


public class Main {

	public static void main(String[] args) {
    // two way linked list
		Node node1 = new Node(1,null,null);
		Node node2 = new Node(2,null,null);
		Node node3 = new Node(3,null,null);
		Node node4 = new Node(4,null,null);
		Node node5 = new Node(5,null,null);
		
		node1.next = node2;
		node2.next = node3;
		node3.next = node4;
		node4.next = node5;
		node5.next = null;
		
		node1.previous = null;
		node2.previous = node1;
		node3.previous = node2;
		node4.previous = node3;
		node5.previous = node4;
		
		Node current = node1;
		while(current!= null) {
			System.out.println(current.data);
			current = current.next;
		}
		
		Node last = node5;
		while(last!= null) {
			System.out.println(last.data);
			last = last.previous;
		} 
	}
	}

class Node
{
	int data;
	Node next;
	Node previous;
	
	public Node(int data,Node next,Node previous)
	{
		this.data = data;
		this.next = next;
		this.previous = previous;
	}
}



