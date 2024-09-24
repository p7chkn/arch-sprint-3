import argparse

def main():
    parser = argparse.ArgumentParser(description="Run different parts of the application.")

    parser.add_argument(
        "--worker",
        action="store_true",
        help="Run worker instead of API"
    )
    parser.add_argument(
       "--consumer",
        action="store_true",
        help="Run consumer instead of API"
    )

    args = parser.parse_args()
    if args.worker:
        from presentation.woker.run import run
        run()
    elif args.consumer:
        from presentation.consumer.run import run
        run()
    else:
        from presentation.api.run import run_app
        run_app()


if __name__ == "__main__":
    main()