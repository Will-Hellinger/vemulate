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


    @staticmethod
    def press() -> None:
        """
        Presses the limit.

        :return: None
        """
        Limit.pressing = True
    

    @staticmethod
    def release() -> None:
        """
        Releases the limit.

        :return: None
        """
        Limit.pressing = False


    @staticmethod
    def value() -> int:
        """
        Gets the value of the limit.

        :return: The value of the limit.
        """

        if Limit.pressing:
            return 1
        
        return 0


    @staticmethod
    def pressing() -> bool:
        """
        Gets whether the limit is pressing.

        :return: Whether the limit is pressing.
        """
        
        return Limit.pressing