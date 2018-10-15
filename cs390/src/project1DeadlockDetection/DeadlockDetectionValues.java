package project1DeadlockDetection;

public class DeadlockDetectionValues {
	public static final String USAGE_STRING = "Usage: java -jar DeadlockDetection.jar <input file name>\nFile must be formatted:\n\n"
			+ "Line 1: Number of processes N, N > 0\n" + "Line 2: Number of resource types M, M > 0\n"
			+ "Line 3: Contents of the array Avail, separated by a whitespace\n"
			+ "Next N Lines: Contents of the array Alloc, separated by a whitespace.\n"
			+ "Next N Lines: Contents of the array Req, separated by a whitespace.";
	public static final String DEADLOCK = "These processes are deadlocked: ";
	public static final String NO_DEADLOCK = "The system is not deadlocked.";

	public static final int INPUT_ERROR = -1;
}
