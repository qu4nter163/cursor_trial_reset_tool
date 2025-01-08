import os
import uuid
import binascii
import re

class IDGenerator:
    def __init__(self):
        pass

    MACHINE_ID_PREFIX = "auth0|user_"

    @staticmethod
    def generate_random_hex(length: int) -> str:
        """
        Generate a random hex string of the specified length.
        """
        random_bytes = os.urandom(length // 2)  # Generate length / 2 bytes
        return binascii.hexlify(random_bytes).decode()

    @staticmethod
    def generate_machine_id() -> str:
        """
        Generate a machine ID with the prefix 'auth0|user_'.
        """
        random_part = IDGenerator.generate_random_hex(64)  # 64 hex chars
        return f"{IDGenerator.MACHINE_ID_PREFIX}{random_part}"

    @staticmethod
    def generate_mac_machine_id() -> str:
        """
        Generate a MAC machine ID as a random 64-character hex string.
        """
        return IDGenerator.generate_random_hex(64)

    @staticmethod
    def generate_device_id() -> str:
        """
        Generate a device ID in UUID format.
        """
        new_uuid = uuid.uuid4()
        return str(new_uuid)

    @staticmethod
    def generate_sqm_id() -> str:
        """
        Generate an SQM ID with braces.
        """
        return f"{{{IDGenerator.generate_device_id()}}}"

    @staticmethod
    def validate_id(id_string: str, id_type: str) -> bool:
        """
        Validate the format of different ID types.
        """
        if id_type == "machineID":
            # Check length (11 characters prefix + 64 characters hex string)
            if not id_string.startswith(IDGenerator.MACHINE_ID_PREFIX):
                return False
            hex_part = id_string[len(IDGenerator.MACHINE_ID_PREFIX):]
            return len(hex_part) == 64 and IDGenerator.is_hex_string(hex_part)
        elif id_type == "macMachineID":
            return len(id_string) == 64 and IDGenerator.is_hex_string(id_string)
        elif id_type == "deviceID":
            return IDGenerator.is_valid_uuid(id_string)
        elif id_type == "sqmID":
            return id_string.startswith("{") and id_string.endswith("}") and \
                   IDGenerator.is_valid_uuid(id_string[1:-1])
        return False


    @staticmethod
    def is_hex_string(s: str) -> bool:
        """
        Check if a string is a valid hex string.
        """
        try:
            binascii.unhexlify(s)
            return True
        except binascii.Error:
            return False

    @staticmethod
    def is_valid_uuid(uuid_string: str) -> bool:
        """
        Validate whether a string conforms to UUID format.
        """
        try:
            uuid_obj = uuid.UUID(uuid_string)
            return str(uuid_obj) == uuid_string
        except ValueError:
            return False


# Example usage
if __name__ == "__main__":
    generator = IDGenerator()

    machine_id = generator.generate_machine_id()
    print(f"Generated Machine ID: {machine_id} (Valid: {generator.validate_id(machine_id, 'machineID')})")

    mac_machine_id = generator.generate_mac_machine_id()
    print(f"Generated MAC Machine ID: {mac_machine_id} (Valid: {generator.validate_id(mac_machine_id, 'macMachineID')})")

    device_id = generator.generate_device_id()
    print(f"Generated Device ID: {device_id} (Valid: {generator.validate_id(device_id, 'deviceID')})")

    sqm_id = generator.generate_sqm_id()
    print(f"Generated SQM ID: {sqm_id} (Valid: {generator.validate_id(sqm_id, 'sqmID')})")
