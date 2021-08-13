using NUnit.Framework;

/* Description:
   Given an integer as input, can you round it to the next (meaning, "higher") 5?

   Examples:

   input:    output:
    0    ->   0
    2    ->   5
    3    ->   5
    12   ->   15
    21   ->   25
    30   ->   30
    -2   ->   0
    -5   ->   -5
    etc.
    Input may be any positive or negative integer (including 0).

    You can assume that all inputs are valid integers. 
*/


namespace Round_to_the_next_multiple_of_5
{
    static class Program
    {
        private static void Main(string[] args)
        {
            Assert.AreEqual(5, Method(1));
        }

        static int Method(int n)
        {
            if (n > 0 & n % 5 != 0)
            {
                return 5 - (n % 5) + n;
            }

            if (n < 0)
            {
                return 5 - (n % 5) + n - 5;
            }

            return n;
        }
    }
}