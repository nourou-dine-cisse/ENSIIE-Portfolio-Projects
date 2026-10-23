#import sys
#sys.path.append('Path to where you put MLRPlotting')
import matplotlib.pyplot as plt
from MLRPlotting import static_plotter

# import custom plotting tools
static_plotter = static_plotter.Visualizer()

cost_1 = [1,2,7,9]
cost_2 = [9,6,3,1]
# plot the cost function history for two runs
static_plotter.plot_cost_histories([cost_1,cost_2],start=0,points=True,labels=[r'Test_1',r'Test_2'])
