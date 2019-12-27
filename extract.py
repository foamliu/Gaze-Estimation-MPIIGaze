import tarfile


def extract_tar(filename):
    print('Extracting {}...'.format(filename))
    with tarfile.open(filename) as tar:
        tar.extractall('data')


if __name__ == "__main__":
    extract_tar('data/MPIIGaze.tar.gz')
