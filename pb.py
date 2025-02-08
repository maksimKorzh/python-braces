import sys

def process_line(line, indent_level):
  stripped_line = line.strip()
  parts = []
  temp = ''
  
  for char in stripped_line:
    if char in "{}":
      if temp:
        parts.append(temp)
        temp = ''
      parts.append(char)
    else:
      temp += char
  
  if temp:
    parts.append(temp)
  
  return parts

def convert_pb_to_py(input_file, output_file):
  try:
    with open(input_file) as f:
      content = f.read()
    
    output = []
    indent_level = 0
    indent_space = '    '
    
    for line in content.splitlines():
      parts = process_line(line, indent_level)
      
      for part in parts:
        part = part.strip().replace(';', '\n' + indent_space * indent_level)
        
        if part == '}':
          indent_level -= 1
          continue
        
        if part == '{':
          output[-1] += ':'
          indent_level += 1
          continue
        
        if part:
          output.append(f'{indent_space * indent_level}{part}')
    
    with open(output_file, 'w') as w:
      w.write('\n'.join(output))
  
  except Exception as e:
    print('Usage: python3 pb.py input.pb output.py')
    print(f'Error: {e}')

if __name__ == "__main__":
  if len(sys.argv) != 3:
    print('Usage: python3 pb.py input.pb output.py')
  else:
    convert_pb_to_py(sys.argv[1], sys.argv[2])
