#!/usr/bin/env/python3
"""
Use index_range to find the correct indexes to paginate the dataset
correctly and
return the appropriate page of the dataset (i.e. the correct list of
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate the start and end index for the pagination.

    Args:
    - page (int): The page number (1-indexed).
    - page_size (int): The number of items per page.

    Returns:
    - tuple: A tuple containing the start index and the end index.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Pagination:
    def __init__(self, data: list, page_size: int):
        """
        Initialize the pagination class.

        Args:
        - data (list): The list of items to paginate.
        - page_size (int): The number of items per page.
        """
        self.data = data
        self.page_size = page_size

    def get_page(self, page: int) -> list:
        """
        Retrieve a single page of items.

        Args:
        - page (int): The page number to retrieve (1-indexed).

        Returns:
        - list: The list of items on the requested page.
        """
        start_index, end_index = index_range(page, self.page_size)
        return (self.data[start_index:end_index])
