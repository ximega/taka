### program types & registers
j - jax, jbx, jcx, jdx, jex, jfx
  - jay, jby, jcy, jdy, jey, jfy (system)

k - kax, kbx, kcx, kdx, kex
  - kay, kby, kcy, kdy, key (system)

l - lax, lbx, lcx, ldx
  - lay, lby, lcy, ldy (system)

m - max, mbx, mcx
  - may, mby, mcy (system)

n - nax, nbx
  - nay, nby (system)

### registers
[sys] - system registers
[bas] - default registers
[reg] - all registers (without difference)

### commands
| set
set [type]
| mov
mov [reg], [value]
| call
call [process]
| ret
ret
| equ
equ [reg], [reg#]
| mor
mor [reg], [reg#]
| les
les [reg], [reg#]
| h
h[command] ...[args]
| lose
lose %[bas]
| take
take %[bas]
| cln
cln [reg]
| sum
sum [syscall]
| syscall
syscall [system]
| inp 
inp ...[reg]
| add
add [reg], [reg#]

~ commands (system calls)
1x00 - writing
1x01 - closing
1x02 - input


### Some rules to use

##### syscall

you should use like this:
```
.main
    mov nax, "Hello,"+sp+"World!"
    mov nby, 1x00
    syscall nax, nby
```

Result: Hello, World!

##### multi- math operations

First register, is where result will be placed

```
.main
    mov nax, 5
    mov nbx, 6
    add nax, nbx
    cln nbx
    mov nbx, 10
    add nax, nbx
    cln nbx

    mov nby, 1x00
    syscall nax, nby
```

Result: 21