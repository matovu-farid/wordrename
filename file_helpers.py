import os
import sys

def replace_all(input:str, replaced: str,replaced_with:str):
  normal = input.replace(replaced,replaced_with)
  plural = normal.replace(f"{replaced}s",f"{replaced_with}s")
  title = plural.replace(f"{replaced.title()}",f"{replaced_with.title()}")
  lower = title.replace(f"{replaced.lower()}",f"{replaced_with.lower()}")
  sanitized = lower.replace(f"{replaced.upper()}",f"{replaced_with.upper()}")
  return sanitized

def get_files(directory):
  obj = os.scandir(directory)
  entrylist = list(filter(lambda x: x.is_file,obj))
  return list(map(lambda x: x.path,entrylist))

def generate_files(input_name,replaced,replaced_with,output_name):

    file = open(input_name,"r")
    extension = os.path.splitext(input_name)[1]
    created_name = f"{input_name}_output{extension}"
    output = open(output_name or created_name,"w")
    lines= file.readlines()

    output_array = []
    for line in lines:
      sanitized = replace_all(line,replaced, replaced_with)
      output_array.append(sanitized)


    output.writelines(output_array)  

    file.close()
    output.close()
    print("Rename succesfull 😀")

def wordrename_file(input_name,replaced,replaced_with,output_name):

  replaced_array = replaced.split(',')
  with_array = replaced_with.split(',')
  if len(replaced_array) != len(with_array):
    print("The input replaced anguments must match those they are replaced with")
    sys.exit(5)
  for i in range(len(replaced_array)):
    generate_files(input_name,replaced_array[i],with_array[i],output_name)
