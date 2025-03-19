# Random - Generator for random number and string

**Author:** [bowenliang123](https://github.com/bowenliang123)

**Github Repo:** https://github.com/bowenliang123/random

## Description

A Dify plugin to generate random number, string, UUID, prime number and etc.

## Tools

### Random String:

- Generate a random string with given length from alphabets and numbers.
- Input parameters:
    - `include_alphabets`: Include alphabets from both, either or none
      of [uppercase](https://docs.python.org/3/library/string.html#string.ascii_uppercase)
      or [lowercase](https://docs.python.org/3/library/string.html#string.ascii_lowercase) alphabets.
    - `include_numbers`: Whether to include [numbers](https://docs.python.org/3/library/string.html#string.digits)
    - `include_punctuation`: Whether to include punctuation characters from `!"#$%&'()*+,-./:;<=>?@[\]^_``{|}~`
- Output: eg. `TSUWUBoOIu4bZja7mdjTkKteaKVrhz` for requested length of 30.

### Random Number:

- Generate a random number in the given range of [ lower_bound, upper bound ] .
- Output: If the digits is set to 0, an integer will be generated.

  <img src="./_assets/img1.png" width="400px" >
  
  <img src="./_assets/img2.png" width="400px" >

### Random Prime Number:

- Generate a random prime number in the given range of [ lower_bound, upper bound ] .
- Output: A prime number, or `NaN` if no prime number is found.

### Random UUID:

- Generate a random string of UUID v4.

<img src="./_assets/img3.png" width="400px" >


