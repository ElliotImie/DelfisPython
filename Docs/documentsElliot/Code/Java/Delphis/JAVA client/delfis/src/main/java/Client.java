import com.google.gson.Gson;

import java.io.*;
import java.net.InetAddress;
import java.net.Socket;

public class Client{

   public static void main(String[] args) throws IOException, InterruptedException {
        Socket socketClient = new Socket("10.2.6.32", 3507);

        DataOutputStream out = new DataOutputStream(socketClient.getOutputStream());
        //out.flush();
        Gson gson = new Gson();
        int test= 0;
        String id ="";
        while(test<50)    {
            test +=1;
            id = String.valueOf(test);
            Message message = new Message(id, "50.487", "12.223232");

            if(test == 25){
                message.setId_user("0");
            }
            String json = gson.toJson(message);
            System.out.println(json);
            System.out.println(test);

            out.writeUTF(json);
            Thread.sleep(1000);
        }
    }
}