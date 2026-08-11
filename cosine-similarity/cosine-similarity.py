import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    z = np.dot(a,b)
    print(z)
    z_mod_a = np.linalg.norm(a)
    z_mod_b = np.linalg.norm(b)
    print(z_mod_a)
    if z_mod_a == 0 or z_mod_b ==0:
        return 0.0
    
    sim = z/(z_mod_a*z_mod_b)
    
    return sim