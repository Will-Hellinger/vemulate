class Limit():
    def __init__(self, brain, port: str):
        """
        Initializes a new limit instance.

        :param brain: The brain to use.
        :param port: The port to use.
        """
        
        self.pressing_: bool = False
        self.port_type: str = "three_wire"

        if brain.request_port(port, self.port_type):
            self.port = port
        else:
            raise Exception("Port already in use.")


    def press(self) -> None:
        """
        Presses the limit.

        :return: None
        """

        self.pressing_ = True
    

    def release(self) -> None:
        """
        Releases the limit.

        :return: None
        """

        self.pressing_ = False


    def value(self) -> int:
        """
        Gets the value of the limit.

        :return: The value of the limit.
        """

        if self.pressing_:
            return 1
        
        return 0


    def pressing(self) -> bool:
        """
        Gets whether the limit is pressing.

        :return: Whether the limit is pressing.
        """
        
        return self.pressing_