
def myzip(it1, it2):
    """Implement zip function for 2 collections."""
    # Use zip and iter to create an iterator of tuples
    return zip(iter(it1), iter(it2))
