package myfirstjava;


public class Main {

	public static void main(String[] args) {

		// binary search
		int[] arr = {1,1,4,5,7,9};
        // binary search
		int left = 0;
		int right = arr.length-1;
		int key = 9;
		while(left<=right)
		{
			int center = (left + right)/2;
			if(key>arr[center])
			{
				left = center + 1;
			}
			else if(key<arr[center])
			{
				right = center - 1 ;
			}
			else
			{
				System.out.print(center);
				
				break;
			}
			
		}
		
	}
	}


