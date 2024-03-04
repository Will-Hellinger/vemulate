class Bumper:
    pressing: bool = False
    port: str = ""


    def __init__(self, brain, port: str):
        """
        Initializes a new Bumper instance.
        
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
        Presses the Bumper.

        :return: None
        """
        Bumper.pressing = True
    

    @staticmethod
    def release() -> None:
        """
        Releases the Bumper.

        :return: None
        """
        Bumper.pressing = False


    @staticmethod
    def value() -> int:
        """
        Gets the value of the Bumper.

        :return: The value of the Bumper.
        """

        if Bumper.pressing:
            return 1
        
        return 0


    @staticmethod
    def pressing() -> bool:
        """
        Gets whether the Bumper is pressing.

        :return: Whether the Bumper is pressing.
        """
        
        return Bumper.pressing