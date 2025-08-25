import requests
from utils.library import Lib as lib

if __name__ == '__main__':
    # in thong tin hiep ngu ra day
    a = lib()
    a.read_data()
    a = requests.get("https://google.com")
    print(f"Status: {str(a.status_code)}")
    pass