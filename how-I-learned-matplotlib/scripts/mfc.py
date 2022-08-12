from pylab import *

size = 256,16
dpi = 72.0
figsize= size[0]/float(dpi),size[1]/float(dpi)
fig = figure(figsize=figsize, dpi=dpi)
fig.patch.set_alpha(0)
axes([0,0,1,1], frameon=False)

for i in range(1,11):
    r,g,b = np.random.uniform(0,1,3)
    plot([i,],[1,],'s', markersize=8, markerfacecolor=(r,g,b,1),
             markeredgewidth=.1,  markeredgecolor=(0,0,0,.5))
xlim(0,11)
xticks([]),yticks([])
savefig('../figures/mfc.png', dpi=dpi)
