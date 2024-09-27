# Codeforces CLI Template

A simple CLI tool to generate a template file for Codeforces problem solving in C++.

## Installation Instructions

To set up this tool globally on your system, follow these steps:

### 1. Move the Script to a Directory in Your `$PATH`
Ensure that the script is located in a directory that is part of your system's `$PATH`. A common location is `/usr/local/bin`:

```bash
sudo mv /path/to/your/script.py /usr/local/bin/codeforce
```

### 2. Add Executable Permissions
Make sure the script is executable:

```bash
sudo chmod +x /usr/local/bin/codeforce
```

### 3. Verify the Script Permissions
The script should have executable permissions. To verify, run:

```bash
ls -l /usr/local/bin/codeforce
```

The output should display something like:

```
-rwxr-xr-x 1 user group size date /usr/local/bin/codeforce
```

### 4. Run the CLI Tool
Once the script is set up, you can use the `codeforce` command to generate your template file. The usage is as follows:

```bash
codeforce [filename]
```

- If no filename is provided, the default `problem.cpp` will be created.
- If a filename is specified, it will create that file with a `.cpp` extension if it does not already exist.

Example:

```bash
codeforce problem_A
```

This will create a file named `problem_A.cpp` in the current directory.

## Example C++ Template

The generated file contains a typical template for competitive programming using C++:

```cpp
#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

void solve() {
    // Write your solution here
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
}
```

- The template sets up a basic input/output configuration using `ios_base::sync_with_stdio` for fast I/O.
- It includes a `solve()` function, which is called for each test case.
- The `int main()` function handles multiple test cases.

## Notes

- Ensure your Python installation is correctly configured and the shebang (`#!/usr/bin/python3`) points to the correct Python interpreter. You can check by running:

```bash
which python3
```

- If you run into permission issues, check that both the file and directory have the appropriate permissions. Use `chmod` to adjust them as needed.

---

