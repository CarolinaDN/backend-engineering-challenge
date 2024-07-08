import argparse

from unbabel_app.tasks.orchestrator import Orchestrator

def execute_from_command_line():
    """Store arguments and run application.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input_file",
        required=True,
        default=None,
        help="Path to input file"
    )
    parser.add_argument(
        "--window_size",
        "-ws",
        required=False,
        default=10,
        type=int,
        help="Window size in minutes. Defaults to 10"
    )
    parser.add_argument(
        "--nr_words",
        required=False,
        default=False,
        type=bool,
        help="If True it will return the moving average of words with window size defined. Defaults to False"
    )
    args = parser.parse_args()

    input_file = args.input_file
    window_size = args.window_size
    nr_words = args.nr_words
    
    orchestrator = Orchestrator(input_file, window_size, nr_words)

    return orchestrator.run_unbabel_cli()

if __name__ == "__main__":
    execute_from_command_line()