import os
if os.path.exists('upflairs'):

    print("present")
else:
    os.makedirs('upflairs',exist_ok=True)
    print("not present")    

