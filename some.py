
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
}
  
sp = " "        

def main(jax=jax, jbx=jbx, jcx=jcx, jdx=jdx, jex=jex, jfx=jfx, jay=jay, jby=jby, jcy=jcy, jdy=jdy, jey=jey, jfy=jfy):
    jax = "a"+sp+"number:"
    prompt(jax)
    print_message(jax)
    exit()
def print_message(jax=jax):

    jbx = jax
    buffer["jax"] = jax
    jax = 0
    jby = '1x00'
    if jby == '1x00': print(jbx)
    if jby == '1x01': return(jbx)
    if jby == '1x02': jbx = input(jbx)
    jby = 0
    jbx = 0
    jax = buffer["jax"]
    buffer["jax"] = 0
    return
def prompt(jax=jax):

    jbx = jax
    jax = 0
    jby = '1x02'
    if jby == '1x00': print(jbx)
    if jby == '1x01': return(jbx)
    if jby == '1x02': jbx = input(jbx)
    jax = jbx
    return
def exit():

    jay = 0
    jby = '1x01'
    if jby == '1x00': print(jay)
    if jby == '1x01': return(jay)
    if jby == '1x02': jay = input(jay)


if __name__ == '__main__': main()
    