import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		int n = scan.nextInt();
		int[] arr = new int[n];
		int tmp;
		
		for(int i=0;i<n;i++)
			arr[i] = i + 1;
		
		while(arr.length>1) {
			System.out.printf("%d ", arr[0]);
			arr = removeElement(arr, 0);
			

			
			
			tmp = arr[0];
			for(int i=0;i <= arr.length - 2;i++) {
				arr[i] = arr[i + 1];
			}
			arr[arr.length - 1] = tmp;
		}
		System.out.printf("%d", arr[0]);
	}
	public static int[] removeElement(int[] arr, int index) {
		int[] result = new int[arr.length - 1];
		System.arraycopy(arr, 0, result, 0, index);
		if (arr.length != index) {
			System.arraycopy(arr, index + 1, result, index, arr.length -  index - 1);
		}
		return result;
	}
}