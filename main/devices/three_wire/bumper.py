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


    def press(self) -> None:
        """
        Presses the Bumper.

        :return: None
        """
        self.pressing = True
    

    def release(self) -> None:
        """
        Releases the Bumper.

        :return: None
        """
        self.pressing = False


    def value(self) -> int:
        """
        Gets the value of the Bumper.

        :return: The value of the Bumper.
        """

        if self.pressing:
            return 1
        
        return 0


    def pressing(self) -> bool:
        """
        Gets whether the Bumper is pressing.

        :return: Whether the Bumper is pressing.
        """
        
        return self.pressing