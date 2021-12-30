def check(cfile, token):
    if token[0] == 'call':
        if not token[2]:
            cfile.write(f"""
    {token[1].replace(",", "")}()\n""")
            return

        cfile.write(f"""
    {token[1].replace(",", "")}({token[2]})""")
    elif token[0] == 'mov':
        if token[2] in ['1x00', '1x01', '1x02']:
            cfile.write(f"""
    {token[1].replace(",", "")} = '{token[2].replace(",", "")}'""")
            return

        cfile.write(f"""
    {token[1].replace(",", "")} = {token[2]}""")
    elif token[0] == 'ret':
        cfile.write("\n    return\n")

    elif token[0] == 'syscall':
        cfile.write(f"""
    if {token[2]} == '1x00': print({token[1].replace(",", "")})
    if {token[2]} == '1x01': return({token[1].replace(",", "")})
    if {token[2]} == '1x02': {token[1].replace(",", "")} = input({token[1].replace(",", "")})""")

    elif token[0] == 'lose':
        cfile.write(f"""
    buffer["{token[1]}"] = {token[1]}
    {token[1]} = 0""")

    elif token[0] == 'take':
        cfile.write(f"""
    {token[1]} = buffer["{token[1]}"]
    buffer["{token[1]}"] = 0""")

    elif token[0] == 'cln':
        cfile.write(f"""
    {token[1]} = 0""")

    elif token[0] == 'add':
        cfile.write(f"""
    {token[1].replace(",", "")} = {token[1].replace(",", "")} + {token[2]}""")

    elif token[0] == 'min':
        cfile.write(f"""
    {token[1].replace("m", "")} = {token[1].replace(",", "")} - {token[2]}""")

    elif token[0] == 'mul':
        cfile.write(f"""
    {token[1].replace("m", "")} = {token[1].replace(",", "")} * {token[2]}""")

    elif token[0] == 'div':
        cfile.write(f"""
    {token[1].replace("m", "")} = {token[1].replace(",", "")} / {token[2]}""")

def check_cond(cfile, token_):
    kw = token_[0][1:]
    if kw == 'call':
        if not token_[2]:
            cfile.write(f"""
        {token_[1].replace(",", "")}()""")
            return
        cfile.write(f"""
        {token_[1].replace(",", "")}({token_[2]})""")
    elif kw == 'mov':
        if token_[2] in ['1x00', '1x01', '1x02']:
            cfile.write(f"""
    {token_[1].replace(",", "")} = '{token_[2].replace(",", "")}'""")
            return

        cfile.write(f"""
        {token_[1].replace(",", "")} = {token_[2]}""")
    elif kw == 'ret':
        cfile.write("\n        return")

    elif kw == 'syscall':
        cfile.write(f"""
        if {token_[2]} == '1x00': print({token_[1].replace(",", "")})
        if {token_[2]} == '1x01': return({token_[1].replace(",", "")})
        if {token_[2]} == '1x02': {token_[1].replace(",", "")} = input({token_[1].replace(",", "")})""")

    elif kw == 'lose':
        cfile.write(f"""
        buffer["{token_[1]}"] = {token_[1]}
        {token_[1]} = 0""")

    elif kw == 'take':
        cfile.write(f"""
        {token_[1]} = buffer["{token_[1]}"]
        buffer["{token_[1]}"] = 0""")

    elif kw == 'cln':
        cfile.write(f"""
        {token_[1]} = 0""")

    elif kw == 'add':
        cfile.write(f"""
        {token_[1].replace(",", "")} = {token_[1].replace(",", "")} + {token_[2]}""")

    elif kw == 'min':
        cfile.write(f"""
        {token_[1].replace(",", "")} = {token_[1].replace(",", "")} - {token_[2]}""")

    elif kw == 'mul':
        cfile.write(f"""
        {token_[1].replace(",", "")} = {token_[1].replace(",", "")} * {token_[2]}""")

    elif kw == 'div':
        cfile.write(f"""
        {token_[1].replace(",", "")} = {token_[1].replace(",", "")} / {token_[2]}""")

def compile_it():
    file_name = input("file name:\n")
    program_started = False
    tokens: list[tuple[str, str, str, int]] = []

    file = open(file_name).read().split('\n')

    for position in range(len(file)):
        line = file[position]

        if line == "START:":
            program_started = True
            continue
        elif not (line.startswith("START:") or line.startswith("set")) and not program_started:
            raise Exception("Program was not started")

        line_s = line.strip().split(" ")
        kw = line_s[0]

        if kw in ('', ' ', ';', '\t'): continue

        try:
            name = line_s[1]
        except IndexError:
            name = None
        try:
            value = line_s[2]
        except IndexError:
            value = None
        tokens.append((kw, name, value, position))

    file_name_s = file_name.split('.')
    file_name_without_ext = ''.join(file_name_s[0:len(file_name_s)-1])

    cfile = open(file_name_without_ext + '.py', 'w+')

    prev_proc = str()
    for token in tokens:
        if token[0] == 'set':
            if token[1] == 'n': 
                cfile.write("""
nax = 0
nbx = 0
nay = 0
nby = 0 
buffer = {}
buffer["nax"] = 0
buffer["nbx"] = 0
buffer["nay"] = 0
buffer["nby"] = 0       
sp = " "    
""")
            if token[1] == 'm':
                cfile.write("""
max = 0
mbx = 0
mcx = 0
may = 0
mby = 0
mcy = 0
buffer = {}
buffer["max"] = 0
buffer["mbx"] = 0
buffer["mcx"] = 0
buffer["may"] = 0
buffer["mby"] = 0
buffer["mcy"] = 0     
sp = " "      
""")
            if token[1] == 'l':
                cfile.write("""
lax = 0
lbx = 0
lcx = 0
ldx = 0
lay = 0
lby = 0
lcy = 0
ldy = 0
buffer = {
    "lax": 0,
    "lbx": 0,
    "lcx": 0,
    "ldx": 0,
    "lay": 0,
    "lby": 0,
    "lcy": 0,
    "ldy": 0
}
sp = " "  
""")
            if token[1] == 'k':
                cfile.write("""
kax = 0
kbx = 0
kcx = 0
kdx = 0
kex = 0
kay = 0
kby = 0
kcy = 0
kdy = 0
key = 0
buffer = {
    "kax": 0,
    "kbx": 0,
    "kcx": 0,
    "kdx": 0,
    "kex": 0,
    "kay": 0,
    "kby": 0,
    "kcy": 0,
    "kdy": 0,
    "key": 0
}
sp = " "  
""")
            if token[1] == 'j':
                cfile.write("""
jax = 0
jbx = 0
jcx = 0
jdx = 0
jex = 0
jfx = 0
jay = 0
jby = 0
jcy = 0
jdy = 0
jey = 0
jfy = 0
buffer = {
    "jax": 0,
    "jbx": 0,
    "jcx": 0,
    "jdx": 0,
    "jex": 0,
    "jfx": 0,
    "jay": 0,
    "jby": 0,
    "jcy": 0,
    "jdy": 0,
    "jey": 0,
    "jfy": 0
}\n  
sp = " "        
""")
            else:
                raise Exception("Unkown set for registers")

        if token[0].startswith(".main"):
            prev_proc = '.main'
            if tokens[0][1] == 'n':
                cfile.write("""
def main(nax=nax, nbx=nbx, nay=nay, nby=nby):""")
            if tokens[0][1] == 'm':
                cfile.write("""
def main(max=max, mbx=mbx, mcx=mcx, may=may, mby=mby, mcy=mcy):""")
            if tokens[0][1] == 'm':
                cfile.write("""
def main(lax=lax, lbx=lbx, lcx=lcx, ldx=ldx, lay=lay, lby=lby, lcy=lcy, ldy=ldy):""")
            if tokens[0][1] == 'k':
                cfile.write("""
def main(kax=kax, kbx=kbx, kcx=kcx, kdx=kdx, kex=kex, kay=kay, kby=kby, kcy=kcy, kdy=kdy, key=key):""")
            if tokens[0][1] == 'j':
                cfile.write("""
def main(jax=jax, jbx=jbx, jcx=jcx, jdx=jdx, jex=jex, jfx=jfx, jay=jay, jby=jby, jcy=jcy, jdy=jdy, jey=jey, jfy=jfy):""")
        elif token[0].startswith("."):
            prev_proc = token[0]

            next_token = tokens[tokens.index(token)+1]
            atrs = []
            if next_token[0] == 'inp':
                regs = next_token[1].split(',')
                [atrs.append(reg) for reg in regs]

            regs = []
            for atr in atrs: regs.append(f"{atr}={atr}")
            regs = ",".join(regs)

            cfile.write(f"def {token[0].replace('.', '')}({regs}):\n")
        
        check(cfile, token)

        if token[0] == 'equ':
            cfile.write(f"""
    if {token[1].replace(",", "")} == {token[2]}:""")
            for ind in range(tokens.index(token)+1, len(tokens)):
                token_ = tokens[ind]
                if token_[0].startswith("h"):
                    check_cond(cfile, token_)
                else: break

        elif token[0] == 'mor':
            cfile.write(f"""
    if {token[1].replace(",", "")} > {token[2]}:""")
            for ind in range(tokens.index(token)+1, len(tokens)):
                token_ = tokens[ind]
                if token_[0].startswith("h"):
                    check_cond(cfile, token_)
                else: break

        elif token[0] == 'les':
            cfile.write(f"""
    if {token[1].replace(",", "")} < {token[2]}:""")
            for ind in range(tokens.index(token)+1, len(tokens)):
                token_ = tokens[ind]
                if token_[0].startswith("h"):
                    check_cond(cfile, token_)
                else: break

    cfile.write("""\n\n
if __name__ == '__main__': main()
    """)

    

if __name__ == '__main__':
    compile_it()