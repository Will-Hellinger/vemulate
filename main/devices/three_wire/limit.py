class Limit():
    pressing: bool = False
    port: str = ""


    def __init__(self, brain, port: str):
        """
        Initializes a new limit instance.

        :param brain: The brain to use.
        :param port: The port to use.
        """
        
        if brain.request_port(port):
            self.port = port
        else:
            raise Exception("Port already in use.")


    def press(self) -> None:
        """
        Presses the limit.

        :return: None
        """

        self.pressing = True
    

    def release(self) -> None:
        """
        Releases the limit.

        :return: None
        """

        self.pressing = False


    def value(self) -> int:
        """
        Gets the value of the limit.

        :return: The value of the limit.
        """

        if self.pressing:
            return 1
        
        return 0


    def pressing(self) -> bool:
        """
        Gets whether the limit is pressing.

        :return: Whether the limit is pressing.
        """
        
        return self.pressing