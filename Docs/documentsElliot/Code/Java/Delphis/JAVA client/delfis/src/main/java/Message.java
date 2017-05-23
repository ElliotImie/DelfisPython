/**
 * Created by ferron.cdi04 on 23/02/2017.
 */
public class Message {
    private String latitude;
    private String longitude;
    private String type_vehicule;
    private String id_user;
    private String mode;
    private String dept;

    public Message(String id_user, String latitude, String longitude){
        this.id_user = id_user;
        this.latitude = latitude;
        this.longitude = longitude;

    }
    public Message(String id_user, String latitude, String longitude, String mode, String type_vehicule, String dept){
        this(id_user,latitude, longitude);
        this.mode = mode;
        this.type_vehicule = type_vehicule;
        this.dept = dept;
    }

    public String getLatitude() {
        return latitude;
    }

    public void setLatitude(String latitude) {
        this.latitude = latitude;
    }

    public String getLongitude() {
        return longitude;
    }

    public void setLongitude(String longitude) {
        this.longitude = longitude;
    }

    public String getType_vehicule() {
        return type_vehicule;
    }

    public void setType_vehicule(String type_vehicule) {
        this.type_vehicule = type_vehicule;
    }

    public String getId_user() {
        return id_user;
    }

    public void setId_user(String id_user) {
        this.id_user = id_user;
    }

    public String getMode() {
        return mode;
    }

    public void setMode(String mode) {
        this.mode = mode;
    }

    public String getDept() {
        return dept;
    }

    public void setDept(String dept) {
        this.dept = dept;
    }
}
