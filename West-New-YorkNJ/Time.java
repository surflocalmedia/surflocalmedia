//////////////////////////////////////////////////
//
//   Time Display Applet V1.00
//
//   KAC Website Design - http://www.kacweb.com
//
//   Created 4/4/97 by Kenny A. Chaffin
//
//   Last Updated 4/8/97 by Kenny A. Chaffin
//
/////////////////////////////////////////////////


// Standard Java Imports

import java.applet.*;
import java.awt.*;
import java.net.*;
import java.util.*;
import java.io.*;

 
class TimeAndDateFormatter {

    String formattedDate;

    String  daysOfWeek[]   = { "Sunday",
                               "Monday",
                               "Tuesday",
                               "Wednesday",
                               "Thursday",
                               "Friday",
                               "Saturday" };

    String  monthsOfYear[] = { "January",
                               "February",
                               "March",
                               "April",
                               "May",
                               "June",
                               "July",
                               "August",
                               "September",
                               "October",
                               "November",
                               "December"  };

    TimeAndDateFormatter( Date date, String title ) {

        int h = date.getHours();
        int m = date.getMinutes();
        int s = date.getSeconds();

        int dy = date.getDay();
        int dt = date.getDate();
        int mn = date.getMonth();
        int yr = date.getYear();

        String hours, minutes, seconds, am_pm;
        String day, numericalDate, month, year;

        if( h == 0 ) {
            hours = new String( "12"  );
            am_pm = new String( "am" );
        } else if( h > 12 ) {
            hours = new String( "" + (h-12) );
            am_pm = new String( "pm"     );
        } else if( h == 12 ) {
            hours = new String( "12" );
            am_pm = new String( "pm"  );
         } else {
            hours = new String( "" + h );
            am_pm = new String( "am"  );
        }

        if( m < 10 ) {
            minutes = new String( "0" + m );
        } else {
            minutes = new String( ""  + m );
        }

        if( s < 10 ) {
            seconds = new String( "0" + s );
        } else {
            seconds = new String( ""  + s );
        }

        day = daysOfWeek[ dy ];
        
        numericalDate = new String( "" + dt );

        month = monthsOfYear[ mn ];

        year  = new String( "" + (1900 + yr) );

        formattedDate = new String( day + ", " +
                                    month + " " +
                                    numericalDate + ", " +                                    
                                    year + "  " + title + "  " +
                                    hours   + ":" +
                                    minutes + ":" +
                                    seconds + " " + am_pm
                                    );
    }

    public String toString() {
        return formattedDate;
    }
}



public class Time extends java.applet.Applet implements Runnable 
  {

    private Thread clock;
    private String font_name, title, datestring;			// name of the font
    private int height, width, font_size;			// font size (points)
    private Font wordFont;
    private FontMetrics wordMetrics;
    private int textcolor, backcolor, bordercolor;
    private int stringx, stringy;
    private int delay, s_width;
    TimeAndDateFormatter formattedTimeAndDate;
        
 public void init() 
    {
      String temp;


      height = size().height;		//set the size
      width = size().width;
           						// get the name and size of the font
     temp = getParameter("delay");
     delay= (temp==null) ? 5000 : Integer.parseInt( temp );
     temp=getParameter("title");
     title = (temp==null) ? " " : temp;
     temp=getParameter("font");
     font_name= (temp==null) ? "TimesRoman" : temp;
     temp = getParameter("fontsize");
     font_size= (temp==null) ? 12 : Integer.parseInt( temp );

     						// initialise the font
     wordFont = new Font(font_name, Font.BOLD, font_size);
     if (wordFont == null)
       wordFont = getFont();
     wordMetrics = getFontMetrics (wordFont);

    temp = getParameter("textcolor");
    textcolor = (temp==null) ? 0x000000 : Integer.parseInt(temp, 16);
    temp = getParameter("backcolor");
    backcolor= (temp==null) ? 0xffffff : Integer.parseInt(temp, 16);
    temp = getParameter("bordercolor");
    bordercolor = (temp==null) ? backcolor : Integer.parseInt(temp, 16);

 }


  public void start() 
     {
       clock = new Thread(this); 	// start the thread
       clock.start();	
     }
	
  public void stop() 
    {
      clock.stop();
    }


    public void run() 
      {
       Thread.currentThread().setPriority(Thread.MIN_PRIORITY);	
      while(true) 
       {
         Date date = new Date();

          formattedTimeAndDate =
            new TimeAndDateFormatter( date, title );

          datestring = formattedTimeAndDate.toString();
          
//          System.out.println( "Current Time and Date: " + formattedTimeAndDate );

          repaint();

          try {
                Thread.sleep(delay);
              } 
          catch( InterruptedException e ) 
            {}
        }    
    }


  public void update (Graphics g) 
    {
      paint(g);
    }

  public synchronized void paint(Graphics g) 
    {
      g.setFont(wordFont);			// set the font in the graphics context
      g.setColor(new Color(backcolor));		// fill area with the background color
      g.fillRect(0,0,width,height);
      g.setColor(new Color(textcolor));
      s_width = wordMetrics.stringWidth(datestring);
      stringy = (height - (wordMetrics.getHeight()-wordMetrics.getLeading()))/2 + (wordMetrics.getHeight()-wordMetrics.getLeading()-wordMetrics.getDescent());		 
      stringx = (width - s_width)/2;

      g.drawString (datestring, stringx, stringy);
      g.setColor(new Color(bordercolor));
      g.drawRect(0, 0, width-1, height-1);	

    }
	
	
  public void paintApplet(Graphics g) 
    {				
	}


}
