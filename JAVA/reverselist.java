package myfirstjava;


public class Main {

	public static void main(String[] args) {
		// reverse the list without using any extra memory
		int[] array = {1,2,3,4,5};
		int left = 0;
		int right = array.length - 1;
		while(left != right)
		{
			int temp = array[left];
			array[left] = array[right];
			array[right] = temp;
			right = right - 1;
			left = left + 1;
		}
		for(int i=0;i<array.length;++i)
		{
			System.out.print(array[i]);
		}
		System.out.println();
		//using extra memory
		int[] arr2 = new int[5];
		int counter = 0;
		for(int i = array.length - 1;i >= 0;--i)
		{
		  arr2[counter] = array[i];
		  counter = counter + 1;
		}
		for(int i=0;i<arr2.length;++i)
		{
			System.out.print(arr2[i]);
		}
		
	}
	}


