# 0x02. Minimum Operations

This project is part of the ALX curriculum and focuses on finding the minimum number of operations needed to achieve exactly `n` characters in a text file using only "Copy All" and "Paste" operations.

## Table of Contents
- [Requirements](#requirements)
- [Algorithm](#algorithm)
- [Usage](#usage)
- [Example](#example)
- [Function Documentation](#function-documentation)
- [Files](#files)
- [License](#license)

## Requirements

- Allowed editors: vi, vim, emacs
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should be documented
- Your code should use the PEP 8 style (version 1.7.x)
- All files must be executable

## Algorithm

To solve this problem, we use the concept of prime factorization. The minimum number of operations needed to achieve exactly `n` characters can be determined by summing the prime factors of `n`.

For example, to get 9 characters:
- Prime factors of 9 are 3 and 3.
- Operations: 3 (first 3) + 3 (second 3) = 6 operations.

## Usage

To use the `minOperations` function, you need to import it and call it with the desired number of characters:

```python
#!/usr/bin/python3
from 0-minoperations import minOperations

n = 4
print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))

n = 12
print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))

