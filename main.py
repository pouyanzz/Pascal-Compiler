def get_size(type_name):
    if "char" in type_name:
        return 1
    elif "integer"in type_name :
        return 2
    elif "real" in type_name:
        return 4
    return "Wrong Syntax"

def get_array_size(array_declaration):
    dimensions = array_declaration[array_declaration.find('[')+1:array_declaration.find(']')].split(',')
    size = 1
    for dim in dimensions:
        bounds = dim.split('..')
        size *= (int(bounds[1]) - int(bounds[0]) + 1)
    return size

def main():
    input_file = 'input.txt' 
    output_file = 'output.txt'  

    with open(input_file, 'r') as file:
        lines = file.read().splitlines()

    variables = {}
    for line in lines:
        line = line.strip()
        if line:
            declarations = line.split(';')
            declarations = list(filter(lambda x: x != '', declarations))
            for declaration in declarations:
                parts = declaration.split(':')
                if len(parts) == 2:
                    names = parts[0].split(',')
                    var_type = parts[1].strip()

                    size = get_size(var_type)
                    for name in names:
                        if 'array' in declaration:  
                            array_size = get_array_size(declaration)  
                            variables[name.strip()] = size * array_size
                        else:
                            variables[name.strip()] = size

    sorted_vars = sorted(variables.items(), key=lambda x: x[0])

    with open(output_file, 'w') as file:
        for var, size in sorted_vars:
            file.write(f"{var} {size}\n")

    print(f"Output written to {output_file}")

if __name__ == "__main__":
    main()
