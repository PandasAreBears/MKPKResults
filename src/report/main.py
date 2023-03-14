from pathlib import Path

from file_system import get_output_filepath
from file_system import get_standard_bins
from file_system import InjectionVariant
from result_csv import result_csv_end
from result_csv import result_csv_start
from result_csv import write_result_to_file
from vt_analysis import vt_analysis_end
from vt_analysis import vt_analysis_scan
from vt_analysis import vt_analysis_start


def main():
    result_csv_start()
    vt_analysis_start()

    i: int = 1
    for original_file in get_standard_bins(100):
        # Resume...
        if i < 81:
            i += 1
            continue

        original_bin_name = Path(original_file).name
        print(f"Running analysis for {original_bin_name} variants. {i}/100")

        target = get_output_filepath(original_bin_name, InjectionVariant.NONE)
        analyse_file(original_bin_name, target)

        target = get_output_filepath(original_bin_name, InjectionVariant.REVERSE_TCP)
        analyse_file(original_bin_name, target)

        target = get_output_filepath(original_bin_name, InjectionVariant.ENCRYPT_PASSWD)
        analyse_file(original_bin_name, target)

        target = get_output_filepath(original_bin_name, InjectionVariant.EGRESS_PASSWDS)
        analyse_file(original_bin_name, target)

        i += 1

    vt_analysis_end()
    result_csv_end()


def analyse_file(original_file: str, bin_file: str):
    analysis = vt_analysis_scan(bin_file)
    write_result_to_file(original_file, bin_file, analysis)


if __name__ == "__main__":
    main()
