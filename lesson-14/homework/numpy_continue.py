# Task 1. Write a Python function that converts a temperature from Fahrenheit to Celsius. 
# Use `numpy.vectorize` to apply this function to an array of temperatures: `[32, 68, 100, 212, 77]`. 
#    - Formula: $C = (F - 32) \times \frac{5}{9}$

import numpy as np
'''
arr=np.array([32, 68, 100, 212, 77])
@np.vectorize
def temp_converter(temp):
    return round(((temp-32)*(5/9)),2)
print(temp_converter(arr))        


# Task 2. Create a custom function that takes two arguments: a number and a power. 
# Use `numpy.vectorize` to calculate the power for each pair of numbers in two arrays: `[2, 3, 4, 5]` and `[1, 2, 3, 4]`.

nums=np.array([2, 3, 4, 5])
pows=np.array([1, 2, 3, 4]) 
@np.vectorize
def power(num,pow):
    return num**pow 
print(power(nums,pows))


# Task 3. Solve the system of equations using `numpy`:
# 4x + 5y + 6z = 7
# 3x - y + z = 4
# 2x + y - 2z = 5

A = np.array([
    [4, 5, 6],        # Coefficients
    [3, -1, 1],
    [2, 1, -2]
])

b = np.array([7, 4, 5])       #  Constants   
solution = np.linalg.solve(A, b)
print("Solution (x, y, z):", solution)

# Task 4. Given the electrical circuit equations below, solve for $I_1, I_2, I_3$ (currents in the branches):

# $$
# \begin{cases}
# 10I_1 - 2I_2 + 3I_3 = 12 \\
# -2I_1 + 8I_2 - I_3 = -5 \\
# 3I_1 - I_2 + 6I_3 = 15
# \end{cases}
# $$

A=np.array([
    [10,-2,3],
    [-2,8,-1],
    [3,-1,6], 
])
B=np.array([12,-5,15])
solution = np.linalg.solve(A, B)
print("Solution (I_1, I_2, I_3):", solution)

'''


# **Image Manipulation with NumPy and PIL**

# Image file: `images/birds.jpg`. Your task is to perform the following image 
# manipulations using the **NumPy** library while leveraging **PIL** for reading and saving the image.

# **Instructions:**

# 1. **Flip the Image**:
#    - Flip the image horizontally and vertically (left-to-right and up-to-down).

# 2. **Add Random Noise**:
#    - Add random noise to the image.

# 3. **Brighten Channels**:
#    - Increase the brightness of the channels (r.g. red channel) by a fixed value (e.g., 40). 
# Clip the values to ensure they stay within the 0 to 255 range.

# 4. **Apply a Mask**:
#    - Mask a rectangular region in the image (e.g., a 100x100 area in the center) 
# by setting all pixel values in this region to black (0, 0, 0).

# **Requirements:**
# - Use the **PIL** module onyl to:
#   - Read the image.
#   - Convert numpy array to image.
#   - Save the modified image back to a file.
# - Perform all manipulations using NumPy functions. Avoid using image editing functions from PIL or other libraries.


# **Bonus Challenge**:
# - Create a function for each manipulation (e.g., `flip_image`, `add_noise`, `brighten_channels`, `apply_mask`) 
# to promote modularity and reusability of code.

# --- 
import numpy as np
from PIL import Image

def flip_image(image_array):
    """Flips the image using indexing."""
    flipped = image_array[::-1, ::-1]  # Flips vertically and horizontally
    return flipped

def add_noise(image_array, noise_level=30):
    """Adds random noise using NumPy."""
    noise = np.random.randint(-noise_level, noise_level, image_array.shape, dtype=np.int16)
    noisy_image = image_array + noise  # Add noise
    return np.clip(noisy_image, 0, 255).astype(np.uint8)  # Clip values

def brighten_channels(image_array, brightness_value=40):
    """Brightens each channel using NumPy indexing."""
    brightened = image_array + brightness_value
    return np.clip(brightened, 0, 255).astype(np.uint8)

def apply_mask(image_array, mask_size=(100, 100)):
    """Applies a black mask at the center of the image using indexing."""
    h, w, _ = image_array.shape
    cx, cy = w // 2, h // 2  # Center coordinates
    mx, my = mask_size[0] // 2, mask_size[1] // 2
    image_array[cy-my:cy+my, cx-mx:cx+mx] = [0, 0, 0]  # Set pixels to black
    return image_array

def main():
    image_path = r"C:\Users\acer nitro\OneDrive\Desktop\Data_science\Pythonhomeworks\lesson-14\homework\images\birds.jpg"
    
    # Load image and convert to NumPy array
    image = Image.open(image_path)
    image_array = np.array(image)

    # Apply transformations
    flipped = flip_image(image_array)
    noisy = add_noise(image_array)
    brightened = brighten_channels(image_array)
    masked = apply_mask(image_array.copy())  # Use copy to avoid modifying original
    path=r'Pythonhomeworks\lesson-14\homework/'
    # Save images
    Image.fromarray(flipped).save(path+"images/flipped_birds.jpg")
    Image.fromarray(noisy).save(path+"images/noisy_birds.jpg")
    Image.fromarray(brightened).save(path+"images/brightened_birds.jpg")
    Image.fromarray(masked).save(path+"images/masked_birds.jpg")

    print("Image manipulations completed and saved successfully!")

if __name__ == "__main__":
    main()
