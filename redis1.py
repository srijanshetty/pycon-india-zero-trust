from lib.redis_core import Connection

def main():
    r = Connection()

    r.set('event', 'pycon')

    print(f"Value: {r.get('event')}")

    print("Keys", r._conn.keys())

if __name__ == '__main__':
    main()
