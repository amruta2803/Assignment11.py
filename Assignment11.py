import numpy as np
import pandas as pd

# Generate ten random numbers
np.random.seed(42)
data = np.random.randint(1, 101, 10)

# Create a Pandas Series
s = pd.Series(data)

print(s)