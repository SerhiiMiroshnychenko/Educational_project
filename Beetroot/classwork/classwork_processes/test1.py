import hashlib
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor


def hash_one(n):
    """A somewhat CPU-intensive task."""

    for i in range(1, n):
        hashlib.pbkdf2_hmac("sha256", b"password", b"salt", i * 10000)

    return "done"


def hash_all(n):
    """Function that does hashing in serial."""

    with ProcessPoolExecutor(max_workers=10) as executor:
        for arg, res in zip(range(n), executor.map(hash_one, range(n), chunksize=2)):
            pass

    return "done"


if __name__ == "__main__":
    hash_all(20)