import time


FORWARD: str = "forward"
REVERSE: str = "reverse"
VOLT: str = 'volt'
DEGREES: str = 'degrees'


class Motor:
    spinning: bool = False
    direction: str = "forward"
    port: str = ""
    rpm: int = 0
    reverse: bool = False
    motor_rotation: int = 0
    voltage: float = 0.0

    start_spinning: float = 0.0


    def __init__(self, brain, port: str, gear_setting: str = "18:1", reverse: bool = False) -> None:
        """
        Initializes a new LED instance.

        :param brain: The brain to use.
        :param port: The port to use.
        """

        if brain.request_port(port):
            self.port = port
        else:
            raise Exception("Port already in use.")

        self.reverse = reverse

        match gear_setting:
            case "18:1":
                self.rpm = 200
            case "36:1":
                self.rpm = 100
            case "6:1":
                self.rpm = 600
            case _:
                raise Exception("Invalid gear setting.")
        
        print(self.rpm)


    @staticmethod
    def set_reversed(is_reversed: bool) -> None:
        """
        Sets whether the motor is reversed.

        :param is_reversed: Whether the motor is reversed.
        :return: None
        """

        Motor.reverse = is_reversed
    

    @staticmethod
    def set_velocity(velocity: int) -> None:
        """
        Sets the velocity of the motor.

        :param velocity: The velocity to set.
        :return: None
        """

        Motor.rpm = velocity
    

    @staticmethod
    def reset_rotation() -> None:
        """
        Resets the rotation of the motor.

        :return: None
        """

        Motor.motor_rotation = 0
    

    @staticmethod
    def rotation() -> int:
        """
        Gets the rotation of the motor.

        :return: The rotation of the motor.
        """

        return Motor.motor_rotation
    

    @staticmethod
    def set_rotation(rotation: int) -> None:
        """
        Sets the rotation of the motor.

        :param rotation: The rotation to set.
        :return: None
        """

        if rotation < 0:
            rotation = (rotation * -1)

        if rotation > 360:
            Motor.motor_rotation = rotation % 360

        Motor.motor_rotation = rotation
    

    @staticmethod
    def spin(direction: str, volts: float = 10.0, unit: str = VOLT) -> None:
        """
        Spins the motor.

        :return: None
        """

        if unit != VOLT:
            raise Exception("Invalid unit.")
        
        if volts < -12 or volts > 12:
            raise Exception("Invalid voltage.")

        Motor.voltage = volts
        Motor.direction = direction
        Motor.spinning = True
        Motor.start_spinning = time.time()
    

    @staticmethod
    def stop() -> None:
        """
        Stops the motor.

        :return: None
        """

        if Motor.spinning:
            rotation_amount = round((time.time() - Motor.start_spinning) * ((Motor.rpm * 360) * 60))

            Motor.motor_rotation += rotation_amount

            if Motor.motor_rotation > 360:
                Motor.motor_rotation = Motor.motor_rotation % 360

        Motor.spinning = False
    

    @staticmethod
    def spin_for(direction: str, amount: int, unit: str) -> None:
        """
        Spins the motor for a certain amount.

        :direction: The direction to spin the motor.
        :amount: The amount to spin the motor.
        :unit: The unit to spin the motor.
        :return: None
        """

        if unit != DEGREES:
            raise Exception("Invalid unit.")
        
        if (Motor.motor_rotation + amount) > 360:
            Motor.motor_rotation = (Motor.motor_rotation + amount) % 360
        else:
            Motor.motor_rotation += amount
        
        print(Motor.rpm)

        Motor.direction = direction
        Motor.spinning = True

        time_to_spin: float = amount / (Motor.rpm * 360 * 60)

        while time.time() < time_to_spin:
            time.sleep(0.001)
    

    @staticmethod
    def spin_to_position(amount: int, unit: str) -> None:
        """
        Spins the motor to a certain position.

        :amount: The amount to spin the motor.
        :unit: The unit to spin the motor.
        :return: None
        """

        if unit != DEGREES:
            raise Exception("Invalid unit.")
        
        Motor.motor_rotation = amount
        Motor.spinning = True

        time_to_spin: float = (Motor.motor_rotation - amount) / (Motor.rpm * 360 * 60)

        if time_to_spin < 0:
            time_to_spin = (time_to_spin * -1)

            time_to_spin = 360 - (time_to_spin % 360)

        while time.time() < time_to_spin:
            time.sleep(0.001)