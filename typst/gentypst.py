import os, re


def gen_section(name, dirname):
    if dirname in ['.DS_Store', 'check']:
        return ''
    sect = []
    sect.append(f"= {name}\n")

    files = []
    for src in os.listdir(u"./%s/" % dirname):
        if src == '.DS_Store':
            continue
        fp = open(u"./%s/%s" % (dirname, src), mode="r", encoding="utf-8") # read the file
        code = fp.read().strip()
        fp.close()

        match = re.search(r'^((\d+) )?(.*?)(\.([^.]*))?$', src)
        index = int(match.group(2)) if match.group(1) else 99999
        title = match.group(3)
        extension = match.group(5)
        orig_name = u"./%s/%s" % (dirname, src)

        files.append( (index, title, extension, code, orig_name) )

    for (index, title, extension, code, orig_name) in sorted(files):
        if extension.lower() == 'bak':
            continue
        sect.append(f"== {title}\n")

        sect.append("#codeblock(\n```cpp")
        sect.append(code)
        sect.append('```\n)\n')

    return "\n".join(sect)


doc = []
os.chdir(u"../src/")
# os.chdir(u"./src/")
for section in os.listdir(u"."):
    match = re.search(r'^(\d+) (.*)$', section)
    (index, name) = (int(match.group(1)), match.group(2)) if match else (99999, section)
    doc.append((index, name, section))

fp = open("../typst/code.typ", mode="w", encoding="utf-8")

fp.write("#import \"template.typ\": codeblock\n\n")
fp.write("\n\n".join([gen_section(item[1], item[2]) for item in sorted(doc)]))

# print("#import \"template.typ\": codeblock\n")
# print("\n\n".join([gen_section(item[1], item[2]) for item in sorted(doc)]))
