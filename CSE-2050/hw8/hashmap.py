class Hashmap:
    def __init__(self, num_buckets=16):
        """ initializes an empty Hashmap with the given number of buckets """
        self._num_buckets = num_buckets
        self._data = [[] for _ in range(num_buckets)]

    def __setitem__(self, user, value):
        """ Adds an item with the given user and value to the hashmap """
    
        # calculates the index of the bucket where the item will be stored
        bucket_index = self._get_bucket_index(user)
        # loops through each item in the bucket to see if the user already exists
        for item_index, (existing_user, _) in enumerate(self._data[bucket_index]):
            # if the user already exists, replace the value for that user with the new value
            if existing_user == user:
                self._data[bucket_index][item_index] = (user, value)
                break
        # if the user doesn't already exist in the bucket, add a new item with the given user and value
        else:
            self._data[bucket_index].append((user, value))

    def __getitem__(self, user):
        """ returns the value associated with the given key in the Hashmap, or raises an error if the key is not present """
        bucket_index = self._get_bucket_index(user)
        for existing_user, value in self._data[bucket_index]:
            if existing_user == user:
                return value
        raise KeyError(user)

    def __contains__(self, user):
        """ returns True if the given key is present in the Hashmap, false otherwise """
        bucket_index = self._get_bucket_index(user)
        for existing_user, _ in self._data[bucket_index]:
            if existing_user == user:
                return True
        return False

    def get_all_items(self):
        """ returns a list of tuples, where each tuple contains a key-value pair from the Hashmap """
        return [item for bucket in self._data for item in bucket]

    def _get_bucket_index(self, key):
        """ returns the bucket index for the given key """
        return hash(key) % self._num_buckets
