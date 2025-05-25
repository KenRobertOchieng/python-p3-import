# module6.py

# Your own function
def function1():
    print("Function 1 in module6")

# ✅ CORRECT relative imports
from .module3 import function1 as f3
from .module4 import function1 as f4
from .module5 import function1 as f5

# Call them all
f3()
f4()
f5()
function1()
