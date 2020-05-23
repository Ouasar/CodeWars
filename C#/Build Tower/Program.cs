using System;
using System.Collections.Generic;

#region Not Done

namespace Build_Tower
{
    internal class Program
    {
        private static void Main(string[] args)
        {
            foreach (var O in TowerBuilder(3)) Console.WriteLine(O);
        }

        public static string[] TowerBuilder(int nFloors)
        {
            var floorArray = new List<string>();
            var block = "*";

            for (var i = 1; i < nFloors; i++)
            {
                if (nFloors - i != 0)
                {
                    var floor = block;
                    floorArray.Add("");

                    floor.Insert(floor.Length, "").Insert(0, "");
                }
            }

            return new string[] { };
        }
    }
}

#endregion