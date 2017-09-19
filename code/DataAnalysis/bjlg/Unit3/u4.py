import matplotlib.pyplot as plt
import numpy as np

a = np.arange(0.0,5.0,0.02)
plt.plot(a,np.cos(2*np.pi*a),'r--')
plt.ylabel('纵轴(值)',fontproperties='SimHei',fontsize=20,color='green')
plt.xlabel('横轴(值)',fontproperties='SimHei',fontsize=20)

# $是一种Latex语法
plt.title(r'正弦波示例 $y=cos(2\pi x)$',fontproperties='SimHei',fontsize=25)
plt.annotate(r'$\mu=100$',xy=(2,1),xytext=(3,1.5),arrowprops=dict(facecolor='blue',shrink=0.1,width=2))

# 使数字前的负号能正确显示
plt.rcParams['axes.unicode_minus'] = False 

plt.axis([-1,6,-2,2])

plt.grid(True)

plt.show()