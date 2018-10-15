package project1DeadlockDetection;

import java.io.FileNotFoundException;

public class DeadlockDetectionDriver
{													 
	public static void main(String[] args){
		if(args.length < 1 || args.length >= 2) {
			System.err.println(DeadlockDetectionValues.USAGE_STRING);
			System.exit(DeadlockDetectionValues.INPUT_ERROR);
		}
		
		try {
			DeadlockDetection deadlockDetection = new DeadlockDetection(args[0]);
			
			System.out.println(deadlockDetection.isDeadlocked() ? "DEADLOCK" : "NO_DEADLOCK");
		}
		catch(FileNotFoundException exception) {
			System.err.println(args[0] + " was not found.");
			System.err.println(DeadlockDetectionValues.USAGE_STRING);
			System.exit(DeadlockDetectionValues.INPUT_ERROR);
		}
	}
}
