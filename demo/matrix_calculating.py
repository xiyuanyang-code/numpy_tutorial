'''
Author: Xiyuan Yang   xiyuan_yang@outlook.com
Date: 2025-03-06 12:49:19
LastEditors: Xiyuan Yang   xiyuan_yang@outlook.com
LastEditTime: 2025-03-15 22:19:29
FilePath: /numpy_tutorial/demo/matrix_calculating.py
Description: 
Do you code and make progress today?
Copyright (c) 2025 by Xiyuan Yang, All Rights Reserved. 
'''
import numpy as np

A = np.array([[12, -6, -4],[-6, 18, -3], [-4, 2, 2]])

print(np.linalg.matrix_rank(A))