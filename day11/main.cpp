#include <iostream>
#include <vector>
#include <math.h>
#include <algorithm>
#include <numeric>
#include <fstream>
#include <string>

using namespace std;

struct ProblemInput{
    int w, h;
    vector<vector<int>> rows;
};

ProblemInput LoadInput(const char* filename){
    ProblemInput result;

    ifstream file(filename);
    if(file.is_open()){
        string line;
        while(getline(file, line)){
            vector<int> row;
            for(char c : line){
                row.push_back(c - '0');
            }
            if(row.size()){
                result.rows.push_back(row);
            }
        }
    }

    result.w = result.rows[0].size();
    result.h = result.rows.size();

    return result;
}

int part1(const ProblemInput& input){
    int days = 100;
    int flashes = 0;

    const int& w = input.w;
    const int& h = input.h;
    vector<vector<int>> rows = input.rows;

    for(int d=0; d<100; d++){
        // inc by one
        for(int x=0; x<w; x++)
            for(int y=0; y<h; y++)
                rows[y][x] += 1;

        vector<pair<int,int>> flashPoints;
        // initialise flash points
        for(int x=0; x<w; x++)
            for(int y=0; y<h; y++)
                if(rows[y][x] > 9){
                    flashPoints.push_back(make_pair(x, y));
                }

        while(flashPoints.size()){
            decltype(flashPoints) newFlashPoints;
            for(auto [x, y] : flashPoints){
                for(int x2 = std::max(0, x-1); x2 < std::min(w, x+2); x2++){
                    for(int y2 = std::max(0, y-1); y2 < std::min(h, y+2); y2++){
                        if(x2 == x && y2 == y)
                            continue;
                        rows[y2][x2] += 1;
                        if(rows[y2][x2] == 10){
                            newFlashPoints.push_back(make_pair(x2, y2));
                        }
                    }
                }
            }
            flashPoints = newFlashPoints;
        }

        for(int x=0; x<w; x++){
            for(int y=0; y<h; y++){
                if(rows[y][x] > 9){
                    rows[y][x] = 0;
                    flashes ++;
                }
            }
        }
    }

    return flashes;
}

int part2(ProblemInput input){
    int days = 0;

    const int& w = input.w;
    const int& h = input.h;
    vector<vector<int>> rows = input.rows;

    for(;; days++){
        int flashes = 0;
        
        // inc by one
        for(int x=0; x<w; x++)
            for(int y=0; y<h; y++)
                rows[y][x] += 1;

        vector<pair<int,int>> flashPoints;
        // initialise flash points
        for(int x=0; x<w; x++)
            for(int y=0; y<h; y++)
                if(rows[y][x] > 9){
                    flashPoints.push_back(make_pair(x, y));
                }

        while(flashPoints.size()){
            decltype(flashPoints) newFlashPoints;
            for(auto [x, y] : flashPoints){
                for(int x2 = std::max(0, x-1); x2 < std::min(w, x+2); x2++){
                    for(int y2 = std::max(0, y-1); y2 < std::min(h, y+2); y2++){
                        if(x2 == x && y2 == y)
                            continue;
                        rows[y2][x2] += 1;
                        if(rows[y2][x2] == 10){
                            newFlashPoints.push_back(make_pair(x2, y2));
                        }
                    }
                }
            }
            flashPoints = newFlashPoints;
        }

        for(int x=0; x<w; x++){
            for(int y=0; y<h; y++){
                if(rows[y][x] > 9){
                    rows[y][x] = 0;
                    flashes ++;
                }
            }
        }
        
        if(flashes == w * h){
            break;
        }
    }

    return days;
}

int main(){
    ProblemInput testinput = LoadInput("testinput.txt");
    ProblemInput fullinput = LoadInput("input.txt");

    cout << "part1 test: " << part1(testinput) << "\n";
    cout << "part1 full: " << part1(fullinput) << "\n";
    
    cout << "part2 test: " << part2(testinput) << "\n";
    cout << "part2 full: " << part2(fullinput) << "\n";
}
