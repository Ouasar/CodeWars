using System;
using System.Text;


namespace Remove_anchor_from_URL
{
    class Program
    {
        static void Main()
        {
            Console.WriteLine(Method("www.codewars.com/katas/?page=1#about"));
        }

        public static string Method(string url)
        {
            if (url.Contains("#"))
                return url.Remove(url.IndexOf('#'));
            else
                return url;
        }
    }
}