from fastapi import FastAPI, Request
import time

app = FastAPI()


# The code demonstrates the use of middleware in FastAPI for logging requests and responses.
#  - The log_middleware function is defined to handle the middleware logic.
#  - It takes in a Request object and a call_next function that represents the next middleware or endpoint to be executed.
#  - Inside the middleware function, you can perform actions before and after the route is executed. In this example,
#    it logs the request method and URL before the route is called and the response status code after the route is executed.
#  - The app.middleware("http") statement registers the middleware function to be executed for every HTTP request.
#  - The hello_world endpoint is a simple example that returns a JSON response with a "message" key.


def log_middleware(request: Request, call_next):
    # Perform actions before the route is executed
    print(f"Request received: {request.method} {request.url}")
    start_time = time.time()
    response = call_next(request)
    end_time = time.time()

    duration = end_time - start_time
    print(f"Duration: {duration}")
    return response


app.middleware("http")(log_middleware)


@app.get("/")
def hello_world():
    return {"message": "Hello, World!"}
