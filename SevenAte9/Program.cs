using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography.X509Certificates;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

/*Description:
  Write a function that removes every lone 9 that is inbetween 7s.
  Kata.SevenAteNine("79712312") => "79712312"
  Kata.SevenAteNine("79797") => "777"
  Input: String Output: String:

  [TestCase("165561786121789797","16556178612178977")]
  [TestCase("797","77")]
  [TestCase("7979797","7777")]
  [TestCase("16797","1677")]
  [TestCase("77","77")]
  [TestCase("7927","7927")]
  [TestCase("1779","1779")]
  [TestCase("a779","a779")]
  [TestCase("17797a","1777a")]
  [TestCase("797 9 7","77 9 7")]
  [TestCase("79799997","7799997")]
 */


namespace SevenAte9
{
    class Program
    {
        static void Main()
        {
            string str = "7979797";

            Console.WriteLine(SevenAteNine(str));
        }

        public static string SevenAteNine(string str)
        {
            for (int i = 0; i < str.Length; i++)
            {
                str = str.Replace("797", "77");
            }

            return str;
        }
    }
}