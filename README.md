# Student resources for Thinkful's Big Data with Spark

This repo contains the notebooks, datasets, and server code that you'll need for the Big Data with Spark specialization in Thinkful's data science program.

Fork this repo to your own GitHub account, and clone a local version on your machine.

## Running this repo with Docker

The notebooks in this repo use Spark. To get a Spark instance running locally, you'll need to launch these notebooks within a Thinkful-made Docker container.

Use the following command to start the container, replacing `/path/to/big-data-student-resources` with the local path that corresponds to this repo on your machine:

```
docker run -d --rm -p 8888:8888 -v /path/to/big-data-student-resources:/home/ds/notebooks thinkfulstudent/pyspark:2.2.1
```

Go to [`localhost:8888/tree`](localhost:8888/tree) in your browser to access your notebooks. 

For full instructions on setting up Docker, refer back to [this assignment](https://courses.thinkful.com/data-201v1/assignment/6.8.2).