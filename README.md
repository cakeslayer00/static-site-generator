# static-site-generator

a little static site generator written from scratch in python, no frameworks. you drop markdown files in `content/`, throw your assets in `static/`, and it turns the whole thing into plain html in `docs/` using `template.html` as the shell. 

## usage

```bash
./main.sh     # build with basepath "/" and serve locally at http://localhost:8888
./build.sh    # build for production (basepath "/static-site-generator/")
./test.sh     # run the unit tests
```

`docs/` is what github pages serves, so it lives in the repo. edit content in `content/`, rebuild, done.
