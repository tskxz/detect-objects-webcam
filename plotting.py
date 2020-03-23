from moviment import df
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource

df["Start_string"] = df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_string"] = df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

cds = ColumnDataSource(df)

plotting = figure(x_axis_type='datetime', height=100, width=500, title="Motion Graph")
plotting.yaxis.minor_tick_line_color = None
plotting.ygrid[0].ticker.desired_num_ticks = 1

hover = HoverTool(tooltips=[("Start", "@Start_string"), ("End", "@End_string")])
plotting.add_tools(hover)

quadrant = plotting.quad(left="Start", right="End", bottom=0, top=1, color='green', source=cds)

output_file("Graph.html")
show(plotting)
