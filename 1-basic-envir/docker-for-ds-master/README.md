# 👨🏼‍💻 docker-for-ds
A practical introduction to Docker for data scientists, showing how to use and combine Jupyter and MSSQL Server in local isolated Docker containers.

The medium post [here](https://medium.com/applied-data-science/the-full-stack-data-scientist-part-2-a-practical-introduction-to-docker-1ea932c89b57) for the longer tutorial. 


## 🐳 Starting with Docker

- Install Docker. This is a straightforward download from the [docs](https://docs.docker.com/install/).

- Open up the app and make sure there's a green light telling you it's running.

- Follow the [hello-world tutorial](https://docs.docker.com/samples/library/hello-world/) to double check the installation works properly.

## 🆙 Walkthrough

We will be running two separate Docker containers:

1. An ubuntu xenial container to run python code in Jupyter notebooks

2. An MSSSQL Server linux container to host our  database

Open a terminal in the root of the repo and run the following commands:

```docker-compose build```

*Builds the images with docker-compose.yml acting as the configuration*

```docker-compose up -d```

*Spins up the containers*

```docker-compose exec app bash```

*Runs bash from inside the 'app' container*

You will be inside the container's terminal now, run:

```jupyter notebook --ip 0.0.0.0 --no-browser --allow-root```

Using the provided token, enter this into your browser

```http://localhost:8888/?token=URTOKEN```


✅ The token provides a security measure to make sure hackers can't access your code and data!


🎮 Running the notebook will extract Ninja's current Fortnite stats and load them into a fortnite table in your MSSQL instance. View your output table in a database management app. I like to use DBeaver.

## How to only build the Jupyter environment

Open a terminal and navigate to /app, then run

```docker build -t ds . ```

*builds image with tag 'ds'*

```docker run --rm -it -p 8888:8888 ds```

*runs the ds image with notebook ports mapped*