import subprocess
from pathlib import Path


class InjectionVariant:
    NONE = 0
    REVERSE_TCP = 1
    ENCRYPT_PASSWD = 2
    EGRESS_PASSWDS = 3


def inject_binary(mkpk_filepath: str, target_filepath: str, output_filepath: str):
    """
    Injects a Makka Pakka program into a target binary and stores the result.

    :param mkpk_filepath: The file path to the makka pakka program to inject.
    :param target_filepath: The file path to the binary to be injected into.
    :param output_filepath: The file path to store the result to.
    """

    Path(output_filepath).parent.mkdir(parents=True, exist_ok=True)

    command: str = (
        "mkpk " f"{mkpk_filepath} " f"{target_filepath} " f"-o {output_filepath} " f"-e"
    )

    proc = subprocess.run(command, shell=True, capture_output=True)

    if proc.returncode != 0:
        print(f"Failed to inject into {target_filepath}.")
