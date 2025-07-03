
import java.util.ArrayList;
import java.util.HashMap;

public class ArrayTest {
    
    public static void main(String[] args) {
        int[] odds = {1, 3, 5, 7, 9};

        for (int i = 0; i < odds.length; i++) {
            System.out.println(odds[i]);
        }

        ArrayList<String> al = new ArrayList<>();

        al.add("안녕");

        for (int i = 0; i < 1; i ++){
            System.out.println(al.get(0));
        }

        HashMap<String, String> mymap = new HashMap<>(); 
        mymap.put("안녕", "하세요");

        HashMap<String, Integer> yourmap = new HashMap<>();

        yourmap.put("안녕", 123);

        System.out.println( mymap.get("안녕") );
    }
}
