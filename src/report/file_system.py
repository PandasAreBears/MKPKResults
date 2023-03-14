from pathlib import Path
from typing import Generator


class InjectionVariant:
    NONE = 0
    REVERSE_TCP = 1
    ENCRYPT_PASSWD = 2
    EGRESS_PASSWDS = 3


def get_standard_bins(num_bins: int) -> Generator[str, None, None]:
    """
    Yields the filepath to standard Linux binaries in /usr/bin.

    :param num_bins: The number of binaries to yield.
    """
    assert isinstance(num_bins, int)

    count: int = 0

    # Iterate all the files in the parent directory.
    for target in [path for path in Path("/usr/bin").glob("**/*") if path.is_file()]:
        if count < num_bins:
            yield str(target)
            count += 1

        else:
            break


def get_output_filepath(bin_name: str, variant: InjectionVariant) -> str:
    """
    Gets the filepath to output the injected binary to.

    :param bin_name: The name of the target binary.
    :variant: The injection variant that has been injected into the target.
    """
    output_name = ""
    match variant:
        case InjectionVariant.NONE:
            output_name = bin_name + "_original"
        case InjectionVariant.REVERSE_TCP:
            output_name = bin_name + "_reverse_tcp"
        case InjectionVariant.ENCRYPT_PASSWD:
            output_name = bin_name + "_encrypt"
        case InjectionVariant.EGRESS_PASSWDS:
            output_name = bin_name + "_egress_pswd"

    output_path = str(
        (Path(__file__).parent.parent.parent / "bin" / bin_name / output_name).resolve()
    )

    # Create the parent directory, if not exists.
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)

    return output_path
