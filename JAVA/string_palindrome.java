package myfirstjava;


public class Main {

	public static void main(String[] args) {
		// check if string is a palindrome
		String name = "rar";
		String backward_name = "";
		
		for(int i=name.length() - 1;i>=0;--i)
		{
			char letter = name.charAt(i);
			backward_name += letter;
		}
		System.out.println(name);
		System.out.println(backward_name);
		
		if(name.equals(backward_name))
		{
			System.out.print("IT IS A PALINDROME");
		}
		else
		{
		    System.out.print("NOT A PALINDROME");	
		}
	}
	}



