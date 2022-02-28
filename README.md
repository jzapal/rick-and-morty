## How to run the project
To start the application one can either:
* install dependencies from the `requirements.txt` file and invoke `python main.py` from the "rick_and_morty" directory.
The code was tested and developed with python version 3.9.
* execute `docker build . -t rick_and_morty` to build the container and then `docker run -p 8000:8000 rick_and_morty` 
to start it.

GraphQL API will be available at `http://127.0.0.1:8000/graphql`

## How to run tests
To run tests install `pytest` package and then execute `pytest` command in the root directory. Please add 
`rick_and_morty` directory to `PYTHONPATH`.