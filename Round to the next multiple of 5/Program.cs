using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

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
    class Program
    {
        static void Main(string[] args)
        {
            int n = 0;
            Method(n);
        }

        static int Method(int n)
        {
            if (n > 0 & n % 5 != 0)
            {
                int b = 5 - (n % 5) + n;
                return b;
            }

            else if (n < 0)
            {
                int b = 5 - (n % 5) + n - 5;
                return b;
            }
            else
            {
                return n;
            }
        }
    }
}