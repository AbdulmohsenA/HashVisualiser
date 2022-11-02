# HashVisualiser

This is a basic python program to visualise hash functions as an image.

## For your function.
### INPUT
Seed value which ranges from 1 to 25000 (or the amount of pixels in the image)

### OUTPUT
You can output any Real number (+/-), the program will normalize the values to be from 0 to 255.

### Process
For each seed, the program will pass the seed value, which is the pixel position, to your function. Then will take the normalized output and color it accordingly. For example, the first pixel's normalized output is 90. Then it will be colored rgb(90, 90, 90) which is dark grey

## NOTES
- You may get weird shapes when your hash outputes a very large number and this is due to integer limits.
- Try to use numpy calculations (e.g. np.sin() instead of math.sin())
