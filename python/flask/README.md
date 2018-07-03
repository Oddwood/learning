# How to use it

Within python/flask do:
```bash
$ docker build -t flaskapp .
$ docker run -d -p 5000:5000 flaskapp
```

In the browser navigate to: http://localhost:5000. You should see: 
Hello From Flask within Docker!!