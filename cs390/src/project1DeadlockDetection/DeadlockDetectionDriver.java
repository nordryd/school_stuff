package project1DeadlockDetection;

import java.io.FileNotFoundException;

public class DeadlockDetectionDriver {
	public static void main(String[] args) {
		if (args.length != 1) {
			System.err.println(DeadlockDetectionValues.USAGE_STRING);
			System.exit(DeadlockDetectionValues.INPUT_ERROR);
		}

		try {
			DeadlockDetection deadlockDetection = new DeadlockDetection(args[0]);

			if (deadlockDetection.isDeadlocked()) {
				String string = DeadlockDetectionValues.DEADLOCK;
				boolean[] deadlockedProcesses = deadlockDetection.getDeadlockedProcesses();
				for(int process = 0; process < deadlockedProcesses.length; process++) {
					string += deadlockedProcesses[process] ? "" : process + " ";
				}
				
				System.out.println(string);
			}
			else {
				System.out.println(DeadlockDetectionValues.NO_DEADLOCK);
			}
		} catch (FileNotFoundException exception) {
			System.err.println(args[0] + " was not found.");
			System.err.println(DeadlockDetectionValues.USAGE_STRING);
			System.exit(DeadlockDetectionValues.INPUT_ERROR);
		}
	}
}
