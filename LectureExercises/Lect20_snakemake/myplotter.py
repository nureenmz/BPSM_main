#!/usr/bin/env python3

import pandas as pd

import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

from argparse import ArgumentParser

a = ArgumentParser()
a.add_argument("-o", "--output")
a.add_argument("input", nargs='+')
args = a.parse_args()

dfs = [ pd.read_csv(f) for f in args.input ]

with PdfPages(args.output, keep_empty=False) as pdf:
    for df in dfs:
        df.plot(kind="scatter", x='X', xlim=(0,df['X'].max()+2),
                                y='Y', ylim=(0,df['Y'].max()+2))
        for _, row in df.iterrows():
            plt.annotate(row['Animal'], (row['X'],row['Y']))
        plt.subplots_adjust(left=0.2, right=0.8)
        pdf.savefig()
        plt.close()
