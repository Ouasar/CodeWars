/* Instructions
 * Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
 * 
 * Examples:
 * 
 * Kata.PigIt("Pig latin is cool"); // igPay atinlay siay oolcay
 * Kata.PigIt("Hello world !");     // elloHay orldway !
 */

using System.Linq;

public class Kata
{
    public static void Main(string[] args)
    {
    }

    public static string PigItBestPractices(string str)
    {
        return string.Join(" ",
            str.Split(' ').Select(w => w.Any(char.IsPunctuation) ? w : w.Substring(1) + w[0] + "ay"));
    }

    public static string PigIt(string str)
    {
        var pigLatinsLine = string.Empty;
        var pigLatinWords = str.Split(' ');

        foreach (var word in pigLatinWords)
        {
            pigLatinsLine += (word + word.First()).Remove(0, 1);

            if (word.Length > 1)
            {
                pigLatinsLine += "ay ";
            }
        }

        return pigLatinsLine.TrimEnd(' ');
    }
}