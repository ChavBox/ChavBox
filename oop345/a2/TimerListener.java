/*
# Name: Charlie Havener
# Date: 11/16/2023
# Description:
*/

public class TimerListener implements IListener{
    
    //Fields
    private String name;

    //Constructors
    public TimerListener(String name){
        this.name = name;
    }

    //Methods
    public void notify(String message){
        System.out.println(name + ": " + message);
    }


}