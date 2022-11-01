"""
Python charting lecture
19/11/2021
"""
#!/usr/local/bin/python3
import os, subprocess, seaborn
import matplotlib.pyplot as plt
import numpy as np

dir() # loaded modules
dir(plt) # what's in plt module

# sinusoid curve
x= np.linspace(0,20,1000)
y= np.sin(x)

plt.figure(figsize=(7,7)) # default size to inches, res 100 dpi
plt.plot(x, y, 'ko', linewidth=2, color='red', label='somelabel') # default puts it as y-value
plt.plot(x,x*2,'r--',  x,x**2,'bs',  x,x+1,'g^')
plt.axis([0,6,0,20]) # xmin, xmax, ymin, ymax
plt.legend(loc='upper right') # default Top Left
plt.xlabel('This is the x-axis')
plt.ylabel('This is the y-axis')
plt.title('This is the title')
plt.savefig('foo.png', transparent=True) # saves image to file, do before show!
plt.show() # stdout
plt.show(block=False) # prevents image from blocking command line
plt.close()

a= x+2
b= y*5
line1,line2= plt.plot(x,y, a,b) # setp() to manipulate individual lines of the plot
plt.setp(line1, color='r', linewidth=6.0)
plt.setp(line2, color='b', linewidth=2.0)
plt.savefig()

# subplots
fig1= plt.figure(1) # put plt.figure as variable to be able to save
plt.subpolot(numrows, numcold, fignum) # subplot(211) = subplot(2,1,1)
plt.subplot(211)
plt.plot(something)
plt.subplot(212)
plt.plot(something2)
plt.xlabel()
plt.ylabel()
plt savefig()

fig2 = plt.figure(2) # second figure

fig1.savefig('title', transparent=True)
fig2.savefig('title2', transparent=True)

# make histogram, produce three sets of values
# n= number of counts in bin
# bins= left hand edge of each bin
# patches= indiv patches used to create histogram
# facecolor= histogram color
mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000) # dataset of IQ values
n, bins, patches= plt.hist(x, 50, density=True, stacked=True, facecolor='#ee42f4', alpha=0.5)
plt.xlabel('Intelligence quotient value')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.axis([40, 160, 0, 0.03])# axis ranges
plt.text(60, .025, r'$\mu=100,\ \sigma=15$') # annotating the chart
plt.axvline(x=mu+(2*sigma),linewidth=4, color='r')
plt.text(mu+(2.1*sigma), .025, r'$\mu + 2\sigma$') # annotating the axvline
plt.grid(True)
# plt.setp(patches[10], facecolor='g') # change color of 9th rectangle
plt.savefig("Chart_11.png",transparent=True)
plt.show()

# anotation of text
plt.annotate('Annotation', xy=(peak, 1), xytext=(2.5, 1.5),
            arrowprops=dict(facecolor='#42f442', shrink=0.05),
            ) # also move the ylim to fit the annotation into figure

# example plot non-linear
y = np.random.normal(loc=0.5, scale=0.4, size=1000)
y= y[(y>0)&(y>1)]
y.sort()
x= np.arange(len(y))

plt.figure(figsize=(20,10))
plt.subplot(221) # linear
plt.plot(x, y, 'r-',linewidth=3.0)
plt.yscale('linear')
plt.title('LINEAR')
plt.grid(True)
plt.subplot(222) # log
plt.plot(x, y, 'g-',linewidth=3.0)
plt.yscale('log')
plt.title('LOG')
plt.grid(True)
plt.subplot(223) # symmetric log
plt.plot(x, y - y.mean(), 'm-',linewidth=3.0)
plt.yscale('symlog', linthreshy=0.05)
plt.title('SYMLOG')
plt.grid(True)
plt.subplot(224) # log-odds @ log of the odds z/(1-z)
plt.plot(x, y, 'b-',linewidth=3.0)
plt.yscale('logit')
plt.title('LOGIT')
plt.grid(True)

## EXERCISES

# make a chart which shows the AT content in a sliding window
ecoli= open('ecoli.txt').read().replace('\n','')[0:100000]
window= 10000
AT=[]
for start in range(len(ecoli) - window):
    win = ecoli[start:start+window]
	AT.append((win.count('A')+win.count('T')) / window)

plt.figure(figsize=(20,10))
plt.plot(AT, label="AT",linewidth=3)
plt.ylabel('Fraction of bases')
plt.xlabel('Position on genome')
plt.title("Base composition in the E coli genome")
plt.legend()
plt.savefig("Chart_16A.png",transparent=True)
plt.show(block=False)

# draw a plot of protein conservation based on the alignment similarities
alignment= open('alignment.txt').read().split('\n')
alignment= np.array(alignment)

# split the string by each character
alignment2= []
for i in np.arange(0,50):
	out= list(alignment[i])
	alignment2.append(out)

# measure conservation by unique aa residues in the column
cons= []
conslessthan2= []
for i in np.arange(0,2013):
	out= len(list(set(np.array(alignment2)[:,i])))
	cons.append(out)
	if out <= 2:
		conslessthan2.append(out)

plt.figure(figsize=(20,5))
plt.plot(np.arange(0,len(cons)), cons, alpha=1)
for i in np.arange(0,len(cons)):
	plt.axvline(conslessthan2[i], color='red', alpha=0.15)
#plt.savefig('Alignment_conservation.png', transparent=True)
plt.show(block=False)