public class Program
{
    public static void main(String[] args)
    {
    	Timer timer = new Timer();
		
		IListener mickey = new TimerListener("Mickey");
		IListener donald = new TimerListener("Donald");

		timer.registerListener(mickey);
		timer.registerListener(donald);

		AlarmClock alarmClock = new AlarmClock(timer);

		alarmClock.setAlarm(2);
    }
}
