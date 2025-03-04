# ## Generalized `Vector` Class  

# **Objective**: Create a Python class `Vector` that represents a mathematical vector in an n-dimensional space, capable of handling any number of dimensions.

# ### **Task Description**

# 1. **Create a `Vector` class** that represents a vector in an n-dimensional space.  
#    - The class should support vectors of any number of dimensions, defined by an arbitrary number of components provided during initialization.

# 2. The class should provide functionality to:
#    - Perform vector operations such as addition, subtraction, and dot product.
#    - Handle scalar multiplication.
#    - Compute the magnitude (length) of the vector.
#    - Normalize the vector (return the unit vector).

# 3. The class should have methods for:
#    - Representing the vector as a string for easy display.
#    - Handling operations between vectors of the same dimension and raising appropriate errors when vectors of different dimensions are involved.

# ### **Example Usage**
# ```python
# # Create vectors
# v1 = Vector(1, 2, 3)
# v2 = Vector(4, 5, 6)

# # Print the vector
# print(v1)          # Output: Vector(1, 2, 3)

# # Addition
# v3 = v1 + v2
# print(v3)          # Output: Vector(5, 7, 9)

# # Subtraction
# v4 = v2 - v1
# print(v4)          # Output: Vector(3, 3, 3)

# # Dot product
# dot_product = v1 * v2
# print(dot_product) # Output: 32

# # Scalar multiplication
# v5 = 3 * v1
# print(v5)          # Output: Vector(3, 6, 9) 

# # Magnitude
# print(v1.magnitude())  # Output: 3.7416573867739413

# # Normalization
# v_unit = v1.normalize()
# print(v_unit)      # Output: Vector(0.267, 0.534, 0.801)
# ```
# ---

import math

class  Vector:
    ''' Creating a class to work with n dimensional vectors'''
    def __init__(self, *components):
        if len(components) == 0:
            raise ValueError("A vector must have at least one component.")
        self.components = components

    # for printing declared vector
    def __str__(self):
        return f"Vector{self.components}" 
    
    # creating method to return the length of the vector
    def __len__(self):
        return len(self.components)     
    
    # checking if vectors have same dimension
    def _check(self,other):
        if len(self)!=len(other):
            raise ValueError("Vectors must have same dimension")

    # adding vectors that have same dimension
    def __add__(self,other):
        self._check(other)
        return Vector(*[x+y for x,y in zip(self.components, other.components)])

    # subtracting vectors that have same dimension
    def __sub__(self,other):
        self._check(other)
        return Vector(*[x-y for x,y in zip(self.components, other.components)])
    
    # multiplying pairs and returning their sum
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            # Scalar multiplication
            return Vector(*[a * other for a in self.components])
        elif isinstance(other, Vector): 
            # Dot product       
            self._check(other)
            return sum(a * b for a, b in zip(self.components, other.components))
        else:
            raise TypeError("Can only multiply a vector by a scalar or another vector.")
    def __rmul__(self,other):
        return self.__mul__(other)

    def magnitude(self):
        return math.sqrt(sum(a**2 for a in self.components))
    
    def normalize(self):
        return f"Vector({','.join(str(round(a/self.magnitude(),3)) for a in self.components)})"
    
v1=Vector(1,2,3)
v2=Vector(4,5,6)
v3=v1+v2 
v4=v2-v1
dot_product=v1*v2
v5=v1*3 
v6=4*v1

print(v3) 
print(v4)     
print(dot_product)
print(v5)
print(v6)
print(v1.magnitude())
print(v1.normalize()) 
        