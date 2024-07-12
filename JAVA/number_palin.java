package myfirstjava;


public class Main {

	public static void main(String[] args) {
    // check if a number is a palindrome
	int number = 9991;
	int orig_number = number;
	int new_number = 0;
	int digit;
	while(number!=0)
	{
		digit = number % 10;
		new_number = new_number*10+digit;
		number = number / 10;
	}
	if(orig_number==new_number)
	{
		System.out.println(true);
	}
	else
	{
		System.out.println(false);
	}
	
	// another way
	int num = 9991;
	String str_num = Integer.toString(num);
	String rev_num = "";
	for(int i=str_num.length() - 1;i>=0;--i)
	{
	char lett = str_num.charAt(i);
	rev_num += lett;
	}
	if(str_num.equals(rev_num))
	{
		System.out.print(true);
	}
	else
	{
		System.out.print(false);
	}
	
	}
	}


