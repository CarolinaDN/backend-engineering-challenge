from .dataload import load_data
from .cleandata import clean_data
from .moving_avg import moving_average
from .output import output_data

class Orchestrator:
    def __init__(self, input_file, window_size, nr_words):
        self.input_file = input_file
        self.window_size = window_size
        self.nr_words = nr_words
    
    def run_unbabel_cli(self):
        """Read file, prepare the data and create moving avergae.
        """
        df_translations = load_data(self.input_file)

        df_transl_resample = clean_data(df_translations)

        moving_avg = moving_average(self.window_size, self.nr_words, df_transl_resample)

        print(moving_avg)

        output_data(moving_avg)

