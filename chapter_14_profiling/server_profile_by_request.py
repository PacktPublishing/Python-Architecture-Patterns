from http.server import BaseHTTPRequestHandler, HTTPServer
import math
from functools import wraps
import cProfile
from time import time


def profile_this(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        prof = cProfile.Profile()
        retval = prof.runcall(func, *args, **kwargs)
        filename = f'profile-{time()}.prof'
        prof.dump_stats(filename)
        return retval

    return wrapper


def check_if_prime(number):

    if number % 2 == 0 and number != 2:
        return False

    for i in range(3, math.floor(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False

    return True


def prime_numbers_up_to(up_to):
    primes = [number for number in range(1, up_to + 1)
              if check_if_prime(number)]

    return primes


def extract_param(path):
    '''
    Extract the parameter and transform into
    a positive integer. If the parameter is
    not valid, return None
    '''
    raw_param = path.replace('/', '')

    # Try to convert in number
    try:
        param = int(raw_param)
    except ValueError:
        return None

    # Check that it's positive
    if param < 0:
        return None

    return param


@profile_this
def get_result(path):
    param = extract_param(path)
    if param is None:
        return 'Invalid parameter, please add an integer'

    return prime_numbers_up_to(param)


class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):

        result = get_result(self.path)

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        return_template = '''
            <html>
                <head><title>Example</title></head>
                <body>
                    <p>Add a positive integer number in the path to display
                    all primes up to that number</p>
                    <p>Result {result}</p>
                </body>
            </html>
        '''

        body = bytes(return_template.format(result=result), 'utf-8')
        self.wfile.write(body)


if __name__ == '__main__':

    HOST = 'localhost'
    PORT = 8000

    web_server = HTTPServer((HOST, PORT), MyServer)
    print(f'Server available at http://{HOST}:{PORT}')
    print('Use CTR+C to stop it')

    # Capture gracefully the end of the server by KeyboardInterrupt
    try:
        web_server.serve_forever()
    except KeyboardInterrupt:
        pass

    web_server.server_close()
    print("Server stopped.")
