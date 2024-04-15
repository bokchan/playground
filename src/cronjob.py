from contextflow_integration.bg_detection import detect_bg_testing_pattern

data = [{"name": "test", "glooko_code": "test", "frequency": "daily"}]


def run_cron_job() -> None:
    print(detect_bg_testing_pattern(data))


if __name__ == "__main__":
    run_cron_job()
