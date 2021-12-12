using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace day12
{
    class Cave{
        public Cave(string key, List<string> initialConnections){
            this.key = key;
            connectedTo = initialConnections;
            isSingleUse = Char.IsLower(key, 0);
            beenExploredAtStep = -1;
        }
        public string key;
        public List<string> connectedTo{ get; set; }
        public bool isSingleUse { get; set; }
        public int beenExploredAtStep { get; set; }
    }

    class Program
    {
        static public List<Cave> caves;
        static public int CountPathsPart1(Cave current, int depth){
            int pathCount = 0;
            current.beenExploredAtStep = depth;

            foreach(string key in current.connectedTo){
                Cave node = caves.Find(c => c.key == key);
                if(node.key == "end"){
                    pathCount ++;
                }
                else if(node.beenExploredAtStep == -1 || !node.isSingleUse){
                    pathCount += CountPathsPart1(node, depth+1);
                }
            }
            current.beenExploredAtStep = -1;
            return pathCount;
        }
        static public int Part1(List<Cave> data){

            caves = data;
            var start = caves.Find(c => c.key == "start");
            start.beenExploredAtStep = 0;
            return CountPathsPart1(start, 1);
        }
        static void Main(string[] args)
        {
            var testcaves = LoadCaves("testinput.txt");
            var fullcaves = LoadCaves("input.txt");

            int result = Part1(testcaves);
            Console.WriteLine($"Part1 test: {result}");
            result = Part1(fullcaves);
            Console.WriteLine($"Part1 full: {result}");
        }

        static List<Cave> LoadCaves(string filename){
            var caves = new List<Cave>();
            var lines = File.ReadLines(filename);
            foreach(string line in lines){
                var both = line.Split('-');
                if(!line.Any())
                    continue;

                var left = both[0];
                var right = both[1];

                if(!caves.Any(c => c.key == left)){
                    Cave node = new Cave(left, new List<string>{right});
                    caves.Add(node);
                }
                else{
                    var node = caves.Find(c => c.key == left);
                    if(!node.connectedTo.Contains(right))
                        node.connectedTo.Add(right);
                } 

                if(!caves.Any(c => c.key == right)){
                    Cave node = new Cave(right, new List<string>{left});
                    caves.Add(node);
                }
                else{
                    var node = caves.Find(c => c.key == right);
                    if(!node.connectedTo.Contains(left))
                        node.connectedTo.Add(left);
                } 
            }
            return caves;
        }
    }
}
