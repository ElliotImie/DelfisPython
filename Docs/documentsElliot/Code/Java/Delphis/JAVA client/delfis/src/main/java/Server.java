import com.google.gson.Gson;

import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.ServerSocket;
import java.net.Socket;

/**
 * Created by louveau.cdi04 on 15/02/2017.
 */
public class Server {

//    public static void main(String[] args) throws IOException {
//
//        Gson gson = new Gson();
//
//        ServerSocket socketServer = new ServerSocket(3001);
//        Socket socketClient = socketServer.accept();
//
//        ObjectOutputStream out = new ObjectOutputStream(socketClient.getOutputStream());
//        out.flush();
//        ObjectInputStream in = new ObjectInputStream(socketClient.getInputStream());
//
//        out.writeUTF("Connection OK");
//        out.flush();
//
//        String coordonneeClient = in.readUTF();
//
//        System.out.println(coordonneeClient);
//
//        System.out.println(gson.fromJson(coordonneeClient, Coordonnee.class).getLatitude());
//
//    }
}
