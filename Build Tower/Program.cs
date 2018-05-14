using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

#region Not Done

namespace Build_Tower
{
    class Program
    {
        private static string block = "*";

        static void Main(string[] args)
        {
            foreach (var O in TowerBuilder(3))
            {
                Console.WriteLine(O);
            }
        }

        public static string[] TowerBuilder(int nFloors)
        {
            List<string> floorArray = null;

            for (int i = 1; i < nFloors; i++)
            {
                if (nFloors - i != 0)
                {
                    string floor = block;
                    floorArray.Add("");

                    floor.Insert(floor.Length, "").Insert(0, "");
                }
            }

            return new string[] { };
        }
    }
}

#endregion