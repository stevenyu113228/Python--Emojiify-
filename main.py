import sys
import obfuscate
import token_utils
import minification


if __name__ == '__main__':
    if len(sys.argv)!=3:
        print("Usage: %s <emoji_length> <filename.py>" % sys.argv[0])
        sys.exit(1)

    source = open(sys.argv[2]).read()
    replacement_length = int(sys.argv[1])

    tokens = token_utils.listified_tokenizer(source)
    source = minification.minify(tokens)

    tokens = token_utils.listified_tokenizer(source)
    obfuscate.obfuscate(source, tokens,replacement_length)

    result = '# -*- coding: emoji -*-\n'
    result += token_utils.untokenize(tokens)

    with open('out/out.py','w') as f:
        f.write(result)
    with open('out/run.py','w') as f:
        f.write('import out\n')

    print('Export successful ./out/out.py')
    print('Run the program with python3 ./out/run.py')
    # print(result)