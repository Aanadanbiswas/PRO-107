import pandas as pd
import csv
import plotly.express as px

df = pd.read_csv(r'studentMarks.csv')

means = df.groupby(['student_id','level'],as_index=False)['attempt'].mean()

print(means)

fig = px.scatter(means, x = 'student_id', y = 'level', color = 'attempt', size = 'attempt')

fig.show()