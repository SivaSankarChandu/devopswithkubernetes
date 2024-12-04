import time
import uuid
from datetime import datetime

def main():
    random_string = str(uuid.uuid4())
    print("Application started with random string:", random_string)
    while True:
        print(f"{datetime.utcnow().isoformat()}: {random_string}")
        time.sleep(5)

if __name__ == "__main__":
    main()
