#!/usr/bin/python

# creates a variable dictionary from the given sources or source trees


import argparse
from collections import OrderedDict
import functools
import json
import locale
import os
from subprocess import call
import sys




parser = argparse.ArgumentParser(description='Create a dictionary from sources.')
parser.add_argument('--ext', help="The extension of the files to examine. Set this to vocabulary.json to read previously generated results.", action="store")
parser.add_argument('--out', help="The output filename", action="store")
parser.add_argument('sources', help="The files or directories to search", nargs=argparse.REMAINDER)
args = parser.parse_args()


PROCESS_PID = str(os.getpid())
SED_PATHNAME = os.path.join(os.path.dirname(sys.argv[0]), 'generateCodeVocabulary.sed')




def findVocabularyFromSourceFile(filename):
    print "finding vocabulary from " + filename
    # remove the comments from the input file
    call(["cloc-1.62.pl", "--force-lang-def=/Users/peter/.cloc.lang_def", "--strip-comments=nc", "--original-dir", "--quiet", "--report-file=/dev/null", filename])
    original_no_comments_filename = filename + ".nc"
    no_comments_filename = "/tmp/generateCodeVocabulary." + PROCESS_PID + ".nc"
    os.rename(original_no_comments_filename, no_comments_filename)
    # replace all characters that may not be in identifiers [~`@#%^&*()-+={}[]|\:;<>,.] or that delimit strings ore regexps ['"/]
    words_filename = "/tmp/generateCodeVocabulary." + PROCESS_PID + ".tokens"
    with open(words_filename, 'w') as words_file:
        # FIX: get path from ARGV[0]
        call(["sed", '-E', '-f', SED_PATHNAME, no_comments_filename], stdout=words_file)
    # count the tokens
    call(["sort", "-o", words_filename, words_filename])
    vocabulary_filename = "/tmp/generateCodeVocabulary." + PROCESS_PID + ".vocab"
    call(["uniq", "-c", words_filename, vocabulary_filename])
    return readVocabularyFromCountNamesFile(vocabulary_filename)


def readVocabularyFromCountNamesFile(filename):
    vocabulary = {}
    with open(filename) as f:
        for line in f:
            tokens = line.split()
            if len(tokens) == 2:
                (count, name) = tokens
                vocabulary[name] = int(count)
    return vocabulary


def readVocabularyFromJSONFile(filename):
    print "reading JSON from " + filename
    with open(filename) as f:
        vocabulary = json.load(f, encoding='ascii');
    return vocabulary


def lexicalSortKey(s):
    # TODO: figure out how to remove characters from a unicode string, and create a more general solution
    a = s.encode('ascii','ignore')
    return str.translate(a, None, '_$')
    


def writeVocabularyAsJSON(file_or_name, vocabulary):
    if isinstance(file_or_name, str):
        f = open(file_or_name, 'w')
    elif isinstance(file_or_name, file):
        f = file_or_name
    else:
        raise Exception('invalid file_or_name')
    ordered = OrderedDict()
    # TODO: cannot get the "correct" form to work:  key=functools.cmp_to_key(locale.strcoll)
    sorted_names = sorted(vocabulary.keys(), key=lexicalSortKey)
    for name in sorted_names:
        ordered[name] = vocabulary[name]
    json_text = json.dumps(ordered, indent=4)
    f.write(json_text)
    #for name in sorted(vocabulary):
    #    f.write("{0} {1}\n".format(name, vocabulary[name]))
    if isinstance(file_or_name, str):
        f.close()


def mergeVocabulary(full_vocabulary, vocabulary):
    for name, count in vocabulary.iteritems():
        if name in full_vocabulary:
            full_vocabulary[name] += count
        else:
            full_vocabulary[name] = count


def findVocabularyFromFiles(ext, pathnames):
    full_vocabulary = {}
    use_json = (ext == 'vocabulary.json')
    for pathname in pathnames:
        if os.path.isfile(pathname):
            _mergeVocabularyFromFile(full_vocabulary, use_json, pathname)
        elif os.path.isdir(pathname):
            for root, dirs, files in os.walk(pathname):
                for file in files:
                    if file.endswith(ext):
                        filename = os.path.join(root, file)
                        _mergeVocabularyFromFile(full_vocabulary, use_json, filename)
    return full_vocabulary


def _mergeVocabularyFromFile(full_vocabulary, use_json, pathname):
    if (use_json):
        vocabulary = readVocabularyFromJSONFile(pathname)
    else:
        vocabulary = findVocabularyFromSourceFile(pathname)
    mergeVocabulary(full_vocabulary, vocabulary)




if len(args.sources) == 0:
    print "Error: no source specified"
    exit(1)
if (args.ext):
    if (args.ext[0] == '.'):
        ext = args.ext
    else:
        ext = '.' + args.ext
else:
    print "Error: no extension specified"
    exit(1)


vocabulary = findVocabularyFromFiles(args.ext, args.sources)
output = args.out if args.out else sys.stdout
writeVocabularyAsJSON(output, vocabulary)



sys.exit(0)

