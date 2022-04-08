#!/usr/bin/env python3

#
# This script will walk through all the tweet id files and
# hydrate them with twarc. The line oriented JSON files will
# be placed right next to each tweet id file.
#
# Note: you will need to install twarc, tqdm, and run twarc configure
# from the command line to tell it your Twitter API keys.
#

import gzip
import json
import sys

from tqdm import tqdm
from twarc import Twarc
from pathlib import Path

twarc = Twarc()
data_dirs = ['2020-10', '2020-11', '2020-12', '2021-01', '2021-02'] #modify to include all dirs you want to hydrate from


def main():
  if len(sys.argv) != 2 or sys.argv[1] not in ['-streaming', '-account']:
    print("Usage: hydrate.py -streaming or hydrate.py -account")
    exit(1)
  prefix = 'streaming-tweetids/' if sys.argv[1] == '-streaming' else 'account-tweetids/'
  
  if prefix == 'streaming-tweetids/':
    for data_dir in data_dirs:
      for path in Path(prefix+data_dir).iterdir():
          if path.name.endswith('.txt'):
              hydrate(path)
  else:
    for path in Path(prefix).iterdir():
      if path.name.endswith('.txt'):
        hydrate(path)

def _reader_generator(reader):
  b = reader(1024 * 1024)
  while b:
      yield b
      b = reader(1024 * 1024)


def raw_newline_count(fname):
  """
  Counts number of lines in file
  """
  f = open(fname, 'rb')
  f_gen = _reader_generator(f.raw.read)
  return sum(buf.count(b'\n') for buf in f_gen)


def hydrate(id_file):
  print('hydrating {}'.format(id_file))

  gzip_path = id_file.with_suffix('.jsonl.gz')
  if gzip_path.is_file():
      print('skipping json file already exists: {}'.format(gzip_path))
      return

  num_ids = raw_newline_count(id_file)

  with gzip.open(gzip_path, 'w') as output:
      with tqdm(total=num_ids) as pbar:
          for tweet in twarc.hydrate(id_file.open()):
              output.write(json.dumps(tweet).encode('utf8') + b"\n")
              pbar.update(1)


if __name__ == "__main__":
  main()