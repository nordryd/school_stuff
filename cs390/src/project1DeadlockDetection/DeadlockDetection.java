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

	private boolean[] finish;

	/**
	 * Constructor for DeadlockDetection.
	 * 
	 * @param filename Name of the formatted file to read.
	 * @throws FileNotFoundException If file was unable to be located or opened.
	 */
	public DeadlockDetection(String filename) throws FileNotFoundException {
		Scanner in = new Scanner(new File(filename));
		this.processes = in.nextInt();
		this.resources = in.nextInt();
		this.avail = new int[resources];
		this.alloc = new int[processes][resources];
		this.req = new int[processes][resources];
		this.finish = new boolean[processes];

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

	/**
	 * @return If the system is currently deadlocked.
	 */
	public boolean isDeadlocked() {
		int[] work = Arrays.copyOf(avail, avail.length);

		for (int process = 0; process < processes; process++) {
			finish[process] = hasAllZeroes(alloc[process]);
		}

		boolean validProcessFound;
		do {
			validProcessFound = false;
			int process = 0;
			while (!validProcessFound && (process < processes)) {
				if (!finish[process] && compareArraysLessThanOrEqual(req[process], work)) {
					validProcessFound = true;
					finish[process] = true;

					work = addArrays(work, alloc[process]);
				}
				process++;
			}

		} while (validProcessFound && !hasAllTrue(finish));

		return !hasAllTrue(finish);
	}

	/**
	 * @return all processes that are currently deadlocked.<br/>
	 *         <b>NOTE</b>: {@code DeadlockDetection.isDeadlocked()} must be
	 *         executed beforehand, otherwise the returned results will be
	 *         meaningless.
	 */
	public boolean[] getDeadlockedProcesses() {
		return finish;
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
		String string = "Avail: \n" + avail[0] + " " + avail[1] + " " + avail[2] + "\n\nAlloc: \n";
		for (int[] i : alloc) {
			string += i[0] + " " + i[1] + " " + i[2] + "\n";
		}

		string += "\nReq: \n";
		for (int[] i : req) {
			string += i[0] + " " + i[1] + " " + i[2] + "\n";
		}

		return string;
	}
}
