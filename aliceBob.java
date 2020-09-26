


public class aliceBob{

  public static void main(String... args)
     Scanner sc = new Scanner(System.in);
     int t= sc.nextInt();
     while(t-->0){
	  String s = sc.nextInt();
	  System.out.println(solve(s));
     }
  }

  public int solve(String s){
     List<Integer> dp = new ArrayList<>();
     for(int i=0 ; i<s.size() ; ++i){
	 dp[i].add(0);
     }
     dp[0]=1;
     for(int i=1 ; i<dp.size() ; ++i){
           String s= d[i] + dp[i-1];
	   int value = Integer.valueOf(s);
	   if(value < 26){
	     dp[i] = dp[i-1] + 2;
	   }else{
	     dp[i] = dp[i-1];
	   }
     }
     return d[s.size()-1];
  }
}
