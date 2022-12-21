BASE_COMMAND = 'terraform apply' # can swap this out for `terraform plan` as well

def parse_file(filepath):
    ret = []
    file = open(filepath, 'r')
    lines = file.read().split('\n')
    for line in lines:
        if line == '':
            continue
        line = line.split(' ')
        if line[0] == 'module' or line[0] == 'resource':
            ret.append(line)
    return ret

def omit_quotes(text):
    if text[0] == '"' and text[len(text)-1] == '"':
        return text[1:len(text)-1]

def generate_commands(parsed_file):
    command = BASE_COMMAND
    num_targets, num_modules, num_resources = 0, 0, 0
    for line in parsed_file:
        if line[0] == 'module':
            module_name = omit_quotes(line[1])
            command += ' -target="module.{0}"'.format(module_name)
            num_targets += 1
            num_modules += 1
        if line[0] == 'resource':
            resource_type = omit_quotes(line[1])
            resource_name = omit_quotes(line[2])
            command += ' -target="{0}.{1}"'.format(resource_type, resource_name)
            num_targets += 1
            num_resources += 1
    print('{0} TARGETS FOUND:\n---------------\n- {1} modules\n- {2} resources\n'.format(num_targets, num_modules, num_resources))
    return command

# example command:
# terraform apply -target="module.module_name" -target="resource_type.resource_name"
def main():
    parsed_file = parse_file('./input.txt')
    print('COMMAND TO RUN:\n---------------\n'+ generate_commands(parsed_file) + '\n')

if __name__ == '__main__':
    main()