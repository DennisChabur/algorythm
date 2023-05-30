class HashTable:

    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()

    def create_buckets(self):
        return [[] for _ in range(self.size)]

    def put_value(self, key, value):
        hashed_key = hash(key)
        bucket = self.hash_table[hashed_key]
        contains_key = False

        for index, record in enumerate(bucket):
            record_key, record_value = record

            if record_key == key:
                contains_key = True
                break

        if contains_key:
            if bucket[index] == None:
                bucket[index] = (key, value)
            # else:
            #     bucket[index] += value
        else:
            bucket.append((key, value))

    def get_value(self, key):
        hashed_key = hash(key)
        bucket = self.hash_table[hashed_key]
        contains_key = False

        for index, record in enumerate(bucket):
            record_key, record_value = record

            if record_key == key:
                contains_key = True
                break

        if contains_key:
            return record_value
        else:
            return "No record found"

    def remove_value(self, key):
        hashed_key = hash(key)
        bucket = self.hash_table[hashed_key]
        contains_key = False

        for index, record in enumerate(bucket):
            record_key, record_value = record

            if record_key == key:
                contains_key = True
                break

        if contains_key:
            print('next pair "key-val" removed:')
            return bucket.pop(index)
        else:
            return "No record found"

    def replays_value(self, key, value):
        hashed_key = hash(key)
        bucket = self.hash_table[hashed_key]
        contains_key = False

        for index, record in enumerate(bucket):
            record_key, record_value = record

            if record_key == key:
                contains_key = True
                break

        if contains_key:
            bucket[index] = (key, value)
        else:
            print("No record found")

ht = HashTable(10)

print(ht.create_buckets())
ht.put_value(1, 'hello')
ht.put_value(2, 'my')
ht.put_value(3, 'dear')
ht.put_value(4, 'friend')
ht.put_value(1, 'goodbye')
for x in range(1, 5):
    print(ht.get_value(x))
print('--------------')
print(ht.remove_value(3))
ht.replays_value(4, 'enemy')
print('--------------')
for x in range(1, 5):
    print(ht.get_value(x))
