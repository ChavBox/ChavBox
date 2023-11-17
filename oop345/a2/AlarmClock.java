/*
# Name: Charlie Havener
# Date: 11/16/2023
# Description:
*/
public class AlarmClock{
    
    //Fields

    private Timer timer;
    
    //Constructors

    public AlarmClock(Timer timer){
        this.timer = timer;
    }

    //Methods

    /* Set Alarm
    # Description: 
    # 
    # Parameters:
    #   int: the amount of time before the alarm goes off
    # 
    # Returns Value: None
    */
    public void setAlarm(int period){
        timer.setTimePeriod(period);
        timer.activate();
    }
}