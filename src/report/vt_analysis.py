import time

import vt

client: vt.Client = None


def vt_analysis_start():
    global client
    client = vt.Client("")


def vt_analysis_scan(target_filepath: str) -> vt.object.Object:
    global client
    start_time = time.time()
    print(f"Sending analysis request for {target_filepath}")

    with open(target_filepath, "rb") as f:
        while True:
            try:
                analysis = client.scan_file(f, wait_for_completion=True)
                break
            except Exception as e:
                # Resilience for network connection dropouts.
                print(
                    f"Encouterned error while trying to scan {target_filepath}"
                )
                print(e)
                time.sleep(100)

    print(
        f"Analysis for {target_filepath} complete, took \
{time.time() - start_time} seconds."
    )

    return analysis


def vt_analysis_end():
    client.close()
