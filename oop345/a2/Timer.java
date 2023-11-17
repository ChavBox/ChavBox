/*
# Name: Charlie Havener
# Date: 11/16/2023
# Description: 
*/

public class Timer extends Notifier{

    //Fields

    private int timerPeriod;

    //Methods

    public void activate(){
        System.out.println("Activating the timer. . .");
        Thread.sleep(timerPeriod * 1000);
        TimerListener.notify("Wake up!");
    }

    public void setTimePeriod(int period){
        timerPeriod = period;
    }
}