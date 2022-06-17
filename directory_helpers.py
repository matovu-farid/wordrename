import os
import errno
from file_helpers import get_files, replace_all, wordrename_file
def get_directories(directory_string):
   return directory_string.split(',')

def wordrename_directory(directory_name,replaced,replaced_with,output):
  directories  = get_directories(directory_name)
  for directory in directories:
    files = get_files(directory)
    
    for filepath in files:
      dir_output_name =  create_output_name(filepath,replaced,replaced_with)
      wordrename_file(filepath,replaced,replaced_with,dir_output_name)

def create_directory(path):
  try:
    os.mkdir(path)
  except OSError as e:
    if(e.errno == errno.EEXIST):
      print("Directory already exists")
    else :
      print (f"Creation of the directory failed at \n {e}")

def create_output_name(filepath,replaced,replaced_with):
  absolute_path = os.path.abspath(filepath)
  parent=os.path.dirname(absolute_path)
  grand_parent = os.path.dirname(parent)
  new_parent = os.path.join(grand_parent,replaced_with)
  create_directory(new_parent)
  base_name = os.path.basename(absolute_path)
  output_basename = replace_all(base_name,replaced,replaced_with)
  return os.path.join(grand_parent,replaced_with,output_basename)
  

  
