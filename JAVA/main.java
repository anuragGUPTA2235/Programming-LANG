package myfirstjava;


public class Main {

	public static void main(String[] args) {
		// learn java in minutes 
		
		System.out.print("anurag shekhar\n");
		
		int a = 78;
		char b = 'k';
		long c = 900;
		double d = 45.7;
		String e = "anurag shekhar";
		
		System.out.println(a);
		System.out.println(b);
		System.out.println(c);
		System.out.println(d);
		System.out.println(e);
		
		// the blue color denotes object which are instance of class
		// they have many methods
		
		String f = e.toUpperCase();
		System.out.println(f);
		
		String g = firstfunction("hotdogs and pizza");
		System.out.println(g);
		
		animal t = new animal();
		String res = t.iamDog("sagar");
		System.out.println(res);
		
		int[] arr = new int[5];
		
		for(int i = 0;i<arr.length;++i)
		{
			arr[i] = i + 1;
		}
		
		for(int i = 0;i<arr.length;++i)
		{
			System.out.print(arr[i]);
		}
		
		System.out.println();
		
		int r = 7;
		if(r == 7)
		{
			System.out.println("i am walter white");
		}
		else if(r < 7)
		{
			System.out.println("breaking bad new series is a must");
		}
		else
		{
			System.out.println("gus fring is a legend");
		}
		
		int counter = 0;
		while(counter < 7)
		{
			System.out.println("Burn the world down");
			counter += 1;
		}
			
		// looping through a string
		String fu = "NAZISM";
		for(int i = 0;i < fu.length();++i)
		{
			char letter = fu.charAt(i); 
			System.out.print(letter+" ");
		}
		
		
	}

	public static String firstfunction(String s)
	{
		return s + "!";
	}
}
