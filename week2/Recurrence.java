import edu.princeton.cs.algs4.StdDraw;

public class Recurrence {
    public static void main(String[] args) {
        int N = 972;
        StdDraw.setXscale(0, N);
        StdDraw.setYscale(0, N*Math.log(N)/Math.log(2));
        StdDraw.setPenRadius(.01);

        int[] An = new int[N + 1];
        An[1] = An[2] = An[3] = 1;
        for (int i = 4; i <= N; i++) {
            An[i] = 3 * An[i/3] + i;
            StdDraw.point(i,An[i]);
            StdDraw.point(i,i * Math.log(i)/Math.log(3));
        }
    }
}
