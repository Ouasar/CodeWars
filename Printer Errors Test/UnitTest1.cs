using System;
using NUnit.Framework;
using Printer_Errors;


namespace Printer_Errors_Test
{
    [TestFixture]
    public static class PrinterTests
    {
        [Test]
        public static void test1()
        {
            Console.WriteLine("Testing PrinterError");
            string s = "aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz";
            Assert.AreEqual("3/56", Printer.PrinterError(s));
        }
    }
}