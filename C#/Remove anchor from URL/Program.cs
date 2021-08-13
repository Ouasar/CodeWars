using System;

namespace Remove_anchor_from_URL
{
    static class Program
    {
        static void Main()
        {
            Console.WriteLine(Method("www.codewars.com/katas/?page=1#about"));
        }

        static string Method(string url) => url.Contains("#") ? url.Remove(url.IndexOf('#')) : url;
    }
}