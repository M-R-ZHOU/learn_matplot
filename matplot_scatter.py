import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation
n = 1024
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)
T = np.arctan2(Y,X)
plt.scatter(X,Y,c=T,s=10*np.abs(X**2+Y**2),alpha=0.5)
#SCATTER  中的参数若为一个定值则所有的标记大小一样，若传入向量则根据一定的规则标记大小不一
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))
#在图里面嵌套图
fig = plt.figure(2)
x = [1,2,3,4,5,6,7]
y = [1,3,4,2,5,8,6]
ax1 = fig.add_axes([0.1,0.1,0.8,0.8])
ax1.plot(x,y,'b--')
ax2 = fig.add_axes([0.2,0.6,0.25,0.25])
ax2.plot(y,x,'k+--')
ax3 = fig.add_axes([0.6,0.2,0.25,0.25])
ax3.plot(y[::-1],x,'rp--')
#添加次坐标轴
x = np.arange(0,10,0.1)
y1 = 0.05*x**2
y2 = 3*x+10
fig,ax = plt.subplots()
ax_2 = ax.twinx()
ax.plot(x,y1,'g-')
ax_2.plot(x,y2,'b--')
ax.set_xlabel('X data')
ax.set_ylabel('Y1',color = 'g')
ax_2.set_ylabel('Y2',color = 'b')

x = np.arange(0,2*np.pi,0.01)
_fig,ax = plt.subplots()
ax.spines['left'].set_position(('data',0))
line, = ax.plot(x,np.sin(x),'rp-')

#面对更加复杂的子图划分，应用起来跟方便，也已容易理解
plt.figure()
ax_a = plt.subplot2grid((3,3),(0,0),rowspan=1,colspan=3)
ax_b = plt.subplot2grid((3,3),(1,0),rowspan=1,colspan=2)
ax_c = plt.subplot2grid((3,3),(1,2),rowspan=2,colspan=1)
ax_d = plt.subplot2grid((3,3),(2,0))
ax_e = plt.subplot2grid((4,3),(2,1))

def animate(i):
    line.set_ydata(np.sin(x+i/10))
    return line
def init():
    line.set_ydata(np.sin(x))
    return line

ani = animation.FuncAnimation(fig=_fig,func=animate,frames=1000,init_func=init,interval=20,blit=False)
plt.show()
