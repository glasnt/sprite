## sprite

🚧👷‍♀️ Work in progress


`pillow-test` outputs text,  `pillow-html` generates html. Pipe to a file to see fancy. 


```shell
time python pillow-html.py firebros.png > output.html && open output.html
```

for non-1:1 images, optional parameter 'step' for how the 'step' size (e.g. in `128.png`, it's 8 pixels per stitch):

```shell
python pillow-test.py 128.png 8
```


