import argparse
import pprint

from comprehendApi import ComprehendApi

MODE_SINGLE = 'single'
MODE_BATCH = 'batch'


def run_demo(mode, input, outfile=None):
    api = ComprehendApi()
    result = None

    if mode == MODE_SINGLE:
        result = api.get_sentiment_singledoc(input)

    elif mode == MODE_BATCH:
        input_list = []
        # read file
        with open(input, "r") as f:
            for line in f:
                input_list.append(line)
        result = api.get_sentiment_batch(input_list)

    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(result)


if __name__ == '__main__':
    mode = [MODE_SINGLE, MODE_BATCH]
    parser = argparse.ArgumentParser()
    parser.add_argument("mode",
                        help="The mode of input", choices=[MODE_SINGLE, MODE_BATCH])

    parser.add_argument("input",
                        help="Single sentence for single mode. For batch mode provide an input file")

    parser.add_argument("--outfile",
                        help="Saves the results to the output file. Only relevant for batch mode")
    args = parser.parse_args()

    run_demo(args.mode, args.input, args.outfile)
