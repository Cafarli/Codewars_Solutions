"""
You can paint an asperand by pixels in three steps:

First you paint the inner square, with a side of k.
Then you need to paint one pixel, that's laying diagonally relative to the inner square that you just painted ( the bottom-right corner of the inner square is touching the top-left corner of the pixel ). Let's call it the "bridge".
Finally, you will need to paint the outer shape, connected diagonally to the "bridge" ( see the picture for more information ).
Here are some examples of this:

Examples for 0<k<5

Your task is to find the number of pixels that need to be painted, for different k:

k = 1 => 11
k = 2 => 18
k = 3 => 26
k = 4 => 34

# Limitations are 1 ≤ k ≤ 1e9
The idea for this kata was taken from the Ukrainian Informatics Olympiad 2023.
"""

def count_pixels(k):
    first_line = 4*k + 5
    second_line = 1
    third_line = 4*k - 4 if k>1 else 1
    return  first_line + second_line + third_line
