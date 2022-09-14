using System;
using NUnit.Framework;
using Printer_Errors;


namespace Printer_Errors_Test
{
    [TestFixture]
    public static class PrinterTests
    {
        [Test]
        public static void testOne()
        {
            var lettersParam = "aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz";

            Assert.AreEqual("3/56", Program.PrinterError(lettersParam));
        }
    }
}