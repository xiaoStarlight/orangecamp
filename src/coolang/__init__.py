def load_cool_program(file: str):
    variables={}
    lines=file.strip().split()
    for line in lines:
        if line.startswith('(return)'):
            variable_name=line.strip('(return)').strip()
            if variable_name in variables:
                print(variables[variable_name])
            else:
                print("Undefined variable")
        else:
            eval_line(line,variables)


def eval_line(line,variables):
    if '+=' in line:
        line="".join(line.split())
        line = line.split('+=')
        if line[1].isdigit():
            variables[line[0]]+=int(line[1])
        else:
            variables[line[0]]+=variables(line[1])
    elif '-=' in line:
        line="".join(line.split())
        line = line.split('-=')
        if line[1].isdigit():
            variables[line[0]]-=int(line[1])
        else:
            variables[line[0]]-=variables(line[1])
    elif '*=' in line:
        line="".join(line.split())
        line = line.split('*=')
        if line[1].isdigit():
            variables[line[0]]*=int(line[1])
        else:
            variables[line[0]]*=variables(line[1])
    elif '/=' in line:
        line="".join(line.split())
        line = line.split('/=')
        if line[1].isdigit():
            variables[line[0]]//=int(line[1])
        else:
            variables[line[0]]//=variables(line[1])
    elif '=' in line:
        line = "".join(line.split())
        line=line.split('=')
        if line[1].isdigit():
            variables[line[0]]=int(line[1])
        else:
            variables[line[0]]=variables[line[1]]
