import os


def get_files(directory):
  obj = os.scandir(directory)

  entrylist = list(filter(lambda x: x.is_file(),obj))
  return list(map(lambda x: x.path,entrylist))

print(get_files('.'))
