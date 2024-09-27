#!/usr/bin/python3

import argparse 
import os

EXTENSION = ".cpp"

def gen_file(file_name="problem.cpp"):
    content = """#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

void solve() {

}

int main() {
    ios_base::sync_with_stdio();
    cin.tie(0);
    cout.tie(0);
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
}    
"""
    if os.path.exists(file_name):
        print("File exists already")
        return
    if not file_name.endswith(EXTENSION):
        file_name += EXTENSION
    with open(file_name, 'w') as file:
        file.write(content)
        print("File has been created, good luck!")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', nargs='?', help="name of file")
    args = parser.parse_args()

    if args.filename:
        gen_file(args.filename)
    else:
        gen_file()
    
if __name__ == "__main__":
    main()




