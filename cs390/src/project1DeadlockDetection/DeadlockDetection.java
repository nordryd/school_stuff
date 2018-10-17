package project1DeadlockDetection;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

/**
 * A class to simulate deadlock detection based on a system given by values of a
 * formatted file. This program uses Dijkstra's algorithm for deadlock
 * detection, using five arrays.
 * 
 * The aforementioned algorithm is executed straight away in the constructor in
 * order to allow for better design choices. This includes being able to
 * retrieve {@code isDeadlocked} without a class-level value being dependent on
 * a method within to give it a meaningful value.
 * 
 * @author Jacob Overton
 * @version last modified October 17, 2018
 */
public class DeadlockDetection {
	private final boolean isDeadlocked;
	private final boolean[] isProcessFinished;

	/**
	 * Constructor for DeadlockDetection. Checks the given system for deadlock.
	 * 
	 * @param filename Name of the formatted file to read.
	 * @throws FileNotFoundException If file was unable to be located or opened.
	 */
	public DeadlockDetection(String filename) throws FileNotFoundException {
		// Variable preparation
		Scanner in = new Scanner(new File(filename));
		int processes = in.nextInt();
		int resources = in.nextInt();
		// work is set to avail straight away
		int[] work = new int[resources];
		int[][] alloc = new int[processes][resources];
		int[][] req = new int[processes][resources];
		// finish array is named something more clear
		this.isProcessFinished = new boolean[processes];

		for (int resource = 0; resource < work.length; resource++) {
			work[resource] = in.nextInt();
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

		// Deadlock Detection Algorithm execution starts here
		for (int process = 0; process < processes; process++) {
			isProcessFinished[process] = hasAllZeroes(alloc[process]);
		}

		boolean validProcessFound;
		do {
			validProcessFound = false;
			int process = 0;
			while (!validProcessFound && (process < processes)) {
				if (!isProcessFinished[process] && compareArraysLessThanOrEqual(req[process], work)) {
					validProcessFound = true;
					isProcessFinished[process] = true;

					work = addArrays(work, alloc[process]);
				}
				process++;
			}

		} while (validProcessFound && !hasAllTrue(isProcessFinished));

		this.isDeadlocked = !hasAllTrue(isProcessFinished);
	}

	/**
	 * @return If the system is currently deadlocked.
	 */
	public boolean isDeadlocked() {
		return isDeadlocked;
	}
	
	/**
	 * @return Array of processes with booleans representing if their process has finished executing successfully.
	 * <p>
	 * <b>T</b> = Process has successfully finished and is NOT DEADLOCKED.<br/>
	 * <b>F</b> = Process has not finished and is DEADLOCKED.
	 * </p>
	 */
	public boolean[] getAllProcesses() {
		return isProcessFinished;
	}

	private int[] addArrays(int[] array1, int[] array2) {
		int[] returnArray = new int[array1.length];

		for (int index = 0; index < array1.length; index++) {
			returnArray[index] = array1[index] + array2[index];
		}

		return returnArray;
	}

	private boolean compareArraysLessThanOrEqual(int[] array1, int[] array2) {
		if (array1.length != array2.length) {
			return false;
		}

		for (int index = 0; index < array1.length; index++) {
			if (array1[index] > array2[index]) {
				return false;
			}
		}

		return true;
	}

	private boolean hasAllZeroes(int[] array) {
		for (int integer : array) {
			if (integer != 0) {
				return false;
			}
		}
		return true;
	}

	private boolean hasAllTrue(boolean[] array) {
		for (boolean bool : array) {
			if (!bool) {
				return false;
			}
		}
		return true;
	}

	@Override
	public String toString() {
		if (isDeadlocked) {
			String string = DeadlockDetectionValues.DEADLOCK;
			for (int process = 0; process < isProcessFinished.length; process++) {
				string += isProcessFinished[process] ? "" : process + " ";
			}

			return string;
		}

		return DeadlockDetectionValues.NO_DEADLOCK;
	}
}
