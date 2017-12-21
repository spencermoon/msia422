package homework4;

/**
 * This is a program that creates a grid of circles with a dimension specified by the user.
 * @author Spencer Moon
 */

import java.awt.Color;
import java.awt.Graphics;
import java.util.Scanner;
import javax.swing.JFrame;
import javax.swing.JComponent;

@SuppressWarnings("serial")

public class exercise2 
{
	public static void draw(Graphics g)
	{  
		Scanner in = new Scanner(System.in);
		System.out.println("Enter grid dimension (even number only):");
		
		int GridDimension = in.nextInt();
	    
		// Upper left quadrant in green
		for (int row = 0; row < GridDimension/2; row++)
		{
			for (int column = 0; column < GridDimension/2; column++)
		    {
				g.setColor(Color.GREEN);
				g.fillOval(row*60 + 50, column*60 + 50, 50, 50);	
		    }
		}
		
		// Lower left quadrant in black
		for (int row = 0; row < GridDimension/2; row++)
		{
			for (int column = GridDimension/2; column < GridDimension; column++)
		    {
				g.setColor(Color.BLACK);
				g.fillOval(row*60 + 50, column*60 + 50, 50, 50);	
		    }
		}
		
		// Upper right quadrant in black
		for (int row = GridDimension/2; row < GridDimension; row++)
		{
			for (int column = 0; column < GridDimension/2; column++)
		    {
				g.setColor(Color.BLACK);
				g.fillOval(row*60 + 50, column*60 + 50, 50, 50);	
		    }
		}
		
		// Lower right quadrant in red
		for (int row = GridDimension/2; row < GridDimension; row++)
		{
			for (int column = GridDimension/2; column < GridDimension; column++)
		    {
				g.setColor(Color.RED);
				g.fillOval(row*60 + 50, column*60 + 50, 50, 50);	
		    }
		
		in.close();
		}
	}
		

	public static void main(String[] args)
	{
		JFrame frame = new JFrame();

		final int width = 800;
		final int height = 800;

		frame.setSize(width, height);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

		JComponent component = new JComponent()
		{
			public void paintComponent(Graphics graph)
			{
				draw(graph);
			}
		};     
		frame.add(component);
		frame.setVisible(true);
   }   
}