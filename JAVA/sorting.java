package myfirstjava;


public class Main {

	public static void main(String[] args) {

		// binary search
		int[] arr = {2,1,4,5,2,4};
		for(int i = 0;i<arr.length;++i)
		{
			for(int k = 0;k<arr.length - 1;++k)
			{
				if(arr[k]<arr[k + 1])
				{
					int temp;
					temp = arr[k];
					arr[k] = arr[k+1];
					arr[k+1] = temp;
				}
			}
		}
		for(int i = 0;i<arr.length;++i)
		{
			System.out.print(arr[i]);
		}
		
	}
	}


