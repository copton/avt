import dictionary
import re
from guppy import *

class Dictionary(dictionary.Dictionary):
    dict_file = RequiredFeature("dictionary.trans_de_en.dict_file", isInstanceOf(str))

    def search(self, pattern):
        regex = re.compile(pattern)
        f = open(self.dict_file)
        res = []
        for line in f.readlines():
            if line.startswith('#'):
                continue
            parts = line.split('::')
            if len(parts) != 2:
                continue
            de, en = parts
            if regex.search(en):
                de_parts = map(str.strip, de.split('|'))
                en_parts = map(str.strip, en.split('|'))
                assert len(de_parts) == len(en_parts)
                test = False
                first = False
                for i in range(len(de_parts)):
                    for l1 in en_parts[i].split(';'):
                        for l2 in l1.split(' '):
                            for l3 in l2.split('-'):
                                if l3 == pattern:
                                    if i == 0:
                                        out = "%s: %s\n" % (en_parts[i], de_parts[i])
                                        test = True
                                        first = True
                                    else:
                                        if not first:
                                            out = "%s: %s\n" % (en_parts[0], de_parts[0])
                                            first = True
                                        out += "\t%s: %s\n" % (en_parts[i], de_parts[i])
                                        test = True

                if test:
                    res.append(out)

        return res
            
