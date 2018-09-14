import argparse
import csv
import pprint

from comprehendApi import ComprehendApi

MODE_SINGLE = 'single'
MODE_BATCH = 'batch'


def write_result(result, outfile=None, encoding="utf-8"):
    if outfile is None:
        return

    with open(outfile, "w", encoding=encoding) as f:
        csv_writer = csv.writer(f, delimiter="|", quotechar='"')
        for l in result:
            csv_writer.writerow(l)

    print("The results have been saved to {}".format(outfile))


def run_demo(mode, input, outfile=None, max_threads=1, encoding="utf-8"):
    """
Runs a sample demo
    :param mode: Mode is either single or batch
    :param input: The input a text or a file for batch
    :param outfile:
    """

    result = None

    if mode == MODE_SINGLE:
        api = ComprehendApi()
        result = api.get_sentiment_singledoc(input)

    elif mode == MODE_BATCH:
        result = run_batch_demo(input, encoding, max_threads)

    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(result)
    write_result(result, outfile)


def run_batch_demo(input, encoding, max_threads):
    input_list = []
    api = ComprehendApi()
    # read file
    with open(input, "r", encoding=encoding) as f:
        for line in f:
            input_list.append(line.strip('\n'))
    result = api.get_sentiment_batch_bulk(input_list, max_threads=max_threads)
    return result


if __name__ == '__main__':
    mode = [MODE_SINGLE, MODE_BATCH]
    parser = argparse.ArgumentParser()
    parser.add_argument("mode",
                        help="The mode of input", choices=[MODE_SINGLE, MODE_BATCH])

    parser.add_argument("input",
                        help="Single sentence for single mode. For batch mode provide an input file")

    parser.add_argument("--outfile",
                        help="Saves the results to the output file. Only relevant for batch mode")

    parser.add_argument("--max-threads",
                        help="This is relevant only for {} mode. The number of threads used to process the requests".format(
                            MODE_BATCH), type=int, default=1)

    parser.add_argument("--encoding",
                        help="This is relevant only for {} mode. The number of threads used to process the requests".format(
                            MODE_BATCH), type=str, default="utf-8")
    args = parser.parse_args()

    run_demo(args.mode, args.input, args.outfile, args.max_threads, args.encoding)
