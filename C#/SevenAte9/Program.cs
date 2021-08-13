using System;

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
    static class Program
    {
        static void Main()
        {
            Console.WriteLine(SevenAteNine("165561786121789797"));
        }

        private static string SevenAteNine(string str)
        {
            foreach (var _ in str) str = str.Replace("797", "77");

            return str;
        }
    }
}