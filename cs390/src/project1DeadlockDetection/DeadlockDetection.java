package project1DeadlockDetection;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.Scanner;

/**
 * A class to simulate deadlock detection based on the given values of a
 * formatted file. This program uses Dijkstra's algorithm for deadlock
 * detection, using five arrays.
 * 
 * @author Jacob Overton
 * @version last modified October 15, 2018
 */
public class DeadlockDetection {
	private int processes, resources;
	private int[] avail;
	private int[][] alloc, req;

	/**
	 * Constructor for DeadlockDetection.
	 * @param filename
	 * 			Name of the formatted file to read.
	 * @throws FileNotFoundException
	 * 			If file was unable to be located or opened.
	 */
	public DeadlockDetection(String filename) throws FileNotFoundException {
		Scanner in = new Scanner(new File(filename));
		this.processes = in.nextInt();
		this.resources = in.nextInt();
		this.avail = new int[resources];
		this.alloc = new int[processes][resources];
		this.req = new int[processes][resources];

		for (int resource = 0; resource < avail.length; resource++) {
			avail[resource] = in.nextInt();
		}

		for (int process = 0; process < processes; process++) {
			for (int resource = 0; resource < resources; resource++) {
				alloc[process][resource] = in.nextInt();
			}
		}
		
		for (int process = 0; process < processes; process++) {
			for (int resource = 0; resource < resources; resource++) {
				req[process][resource] = in.nextInt();
			}
		}

		in.close();
	}
	
	public boolean isDeadlocked() {
		int[] work = Arrays.copyOf(avail, avail.length);
		boolean[] finish = new boolean[processes];
		
		for(int process = 0; process < processes; process++) {
			finish[process] = hasAllZeroes(alloc[process]);
		}
		
		
		
		return false;
	}
	
	private boolean hasAllZeroes(int[] array) {
		for(int integer : array) {
			if(integer != 0) {
				return false;
			}
		}
		return true;
	}
	
	@Override
	public String toString() {
		String string = "Avail: \n" + avail[0] + " " + avail[1] + " " + avail[2] + "\n\nAlloc: \n";
		for(int[] i : alloc) {
			string += i[0] + " " + i[1] + " " + i[2] + "\n";
		}
		
		string += "\nReq: \n";
		for(int[] i : req) {
			string += i[0] + " " + i[1] + " " + i[2] + "\n";
		}
		
		return string;
	}
}
