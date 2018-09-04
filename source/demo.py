import argparse
import csv
import pprint

from comprehendApi import ComprehendApi

MODE_SINGLE = 'single'
MODE_BATCH = 'batch'


def write_result(result, outfile=None):

    if outfile is None:
        return

    with open(outfile, "w") as f:
        csv_writer = csv.writer(f, delimiter="|", quotechar='"')
        for l in result:
            csv_writer.writerow(l)

    print("The results have been saved to {}".format(outfile))


def run_demo(mode, input, outfile=None):
    """
Runs a sample demo
    :param mode: Mode is either single or batcn
    :param input: The input a text or a file for batch
    :param outfile:
    """
    api = ComprehendApi()
    result = None

    if mode == MODE_SINGLE:
        result = api.get_sentiment_singledoc(input)

    elif mode == MODE_BATCH:
        input_list = []
        # read file
        with open(input, "r") as f:
            for line in f:
                input_list.append(line.strip('\n'))
        result = api.get_sentiment_batch_bulk(input_list)



    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(result)
    write_result(result, outfile)


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
