class UsefulClass():
    """
    Base class.
    Args:
        *args (list): list of arguments
        **kwargs (dict): dict of keyword arguments
    Attributes:
        self
    """

    def __init__(self, *args, **kwargs):
        pass

    @staticmethod
    def read_lines_to_array(filepath):
        """Reads lines from a text file and returns them as a list.

        Args:
            filepath: The path to the text file.

        Returns:
            A list of strings, where each string is a line from the file.
            Returns an empty list if the file cannot be opened.
            Returns None if the filepath is not a string
        """
        if not isinstance(filepath, str):
            return None
        try:
            with open(filepath, 'r') as file:
                lines = file.readlines()
                # Remove trailing newline characters
                cleaned_lines = [line.rstrip('\n') for line in lines]
                return cleaned_lines
        except FileNotFoundError:
            print(f"Error: File not found at {filepath}")
            return 
        except Exception as e: #catches any other potential exceptions
            print(f"An error occurred: {e}")
            return
        
    @staticmethod
    def read_lines_to_string(filepath):
        """Reads all lines from a text file and returns them as a single string.

        Args:
            filepath: The path to the text file.

        Returns:
            A string of all content from the file.
            Returns an empty string if the file cannot be opened.
            Returns None if the filepath is not a string
        """
        if not isinstance(filepath, str):
            return None
        try:
            with open(filepath, 'r') as file:
                file_content = file.read() #read the whole content at once
                return file_content
        except FileNotFoundError:
            print(f"Error: File not found at {filepath}")
            return ""  # Return an empty string
        except Exception as e: #catches any other potential exceptions
            print(f"An error occurred: {e}")
            return "" # Return an empty string