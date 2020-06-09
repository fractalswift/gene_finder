import sys


# read the data
def read_data(source):
    with open(source, "r") as f:
        lines = [l for l in f if not l.startswith("##")]
    return lines


# clean the data
def clean_data(lines):

    data = [l.split(" ") for l in lines]

    # list comprehension and lambda to get rid of the empty spaces
    data = [list(filter(lambda c: c != "", row)) for row in data]

    return data


def create_lookup(data):
    # strip out the data we don't need a make a dict
    # (hash table) for rapid look up

    # first make unique keys by combing #Chrom column with
    #  Pos column
    keys = [row[0] + row[1] for row in data]

    # Get the ref column which contains the gene(?)
    values = [row[3] for row in data]

    # Now use them as keys in dict with the ref column
    gene_lookup = dict(zip(keys, values))

    return gene_lookup


def find_gene(chrom, pos, lookup_table):

    # concanate the chrom/pos colum so same format
    # as lookup table
    key = chrom + pos

    return lookup_table[key]


# execution
if __name__ == "__main__":

    try:
        source = sys.argv[1]
        chrom = sys.argv[2]
        pos = sys.argv[3]

        lines = read_data(source)
        data = clean_data(lines)
        lookup_table = create_lookup(data)
        gene = find_gene(chrom, pos, lookup_table)

        print(" ")
        print(f"The gene for {chrom} {pos} is: {gene}")
        print(" ")

    except Exception:
        print(" ")
        print("Something went wrong.")
        print("Are you sure you entered the data correctly?")
        print(" ")
