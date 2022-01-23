
Or you could run it as regular single page app like this:

```python 

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")
layout = dcc.Graph(figure=fig)



```

now we have a different figure 

```python


fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", marginal_y="violin",
           marginal_x="box", trendline="ols", template="simple_white")
app.layout=dcc.Graph(figure=fig)

```

And here's a different dataset

```
df = px.data.tips()
fig = px.bar(df, x="sex", y="total_bill", color="smoker", barmode="group")

layout = dcc.Graph(figure=fig)
```