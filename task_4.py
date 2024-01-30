import requests
import time


def retry(attempts: int, delayed: bool):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(1, attempts + 1):
                try:
                    response = func(*args, **kwargs)
                    print(f"Attempt {attempt}: Status Code {response.status_code}, Error: None")
                    return response
                except Exception as e:
                    print(f"Attempt {attempt}: Status Code None, Error: {str(e)}")
                    if attempt < attempts:
                        if delayed:
                            delay_time = attempt * 2 + 3
                            print(f"Retrying in {delay_time} seconds...")
                            time.sleep(delay_time)
                            print("Retrying...")
                        else:
                            print("Retrying immediately...")
                    else:
                        print(f"All attempts failed. Returning the original exception.")
                        raise e

        return wrapper

    return decorator


@retry(attempts=3, delayed=False)
def get_python() -> requests.Response:
    return requests.get('https://python.org', timeout=0.05)

response = get_python()


@retry(attempts=3, delayed=False)
def get_python2() -> requests.Response:
    return requests.get('https://python.org', timeout=0.05)


response2 = get_python2()
