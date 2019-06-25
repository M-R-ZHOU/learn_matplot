import  numpy as np
import matplotlib.pyplot as plt

plt.figure()
x = np.linspace(-3,3,51)
y1 = 2*x + 2
y2 = x**2 + 1
line1, = plt.plot(x,y1,color='red')
line2, = plt.plot(x,y2,color='blue',linestyle='--')
left, right = plt.xlim()
plt.ylim(-2,3)
plt.xlim(-3,3)
plt.legend(handles = (line1,line2,),labels=('line_1','line_2',),loc='best')
# loc代表图例放置位置的参数，一般有'best' 'upper right' 'upper left' 'lower right'
plt.xticks(np.linspace(-3,3,21))
plt.yticks([-2,-1.8,-1,1.22,3,],[r'$really\ bad$',r'$bad\ \alpha$',r'$normal$',r'$good$',r'$really\ good$',])
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))
# 'data'是参数 还可以设置'outward'与'axes' 'axes'的定位方式是比例

#Annotation
#*************method1
x0 = 0.6
y0 = round(x0**2 + 1,2)
x_1 = -0.4
y_1 = round(x_1**2 + 1,2)
#两种方式指定标记的点，指定文本起点，都已绝对坐标形式
#或者指定文本起点时已相对坐标的形式指定
plt.annotate(r'$x^2+1=%s$' %y0, xy=(x0,y0),xytext=(1,1),
             arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=.2'),fontsize=16)
plt.annotate(r'$x^2+1=%s$' %y_1, xy=(x_1,y_1),xycoords = 'data',xytext=(-150,-100), textcoords = 'offset points',
             arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=-.3'),fontsize=16)

#*************method2
plt.text(1,-1,r'$this\ is\ my\ graph\ \mu\ \sigma_i\ \alpha_t$',fontdict={'size':16,'color':'red'})
plt.scatter(x0,y0,s=50,color='b')
plt.plot([x0,x0],[y0,0],'k--',linewidth=2)
plt.show()


