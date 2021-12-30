It's funny assembler-styled programming language

#### Hello World

Just main-styled without any processes

```nasm
START:

set n

.main:
    mov nax, "hello"+sp+"world!"
    
    mov nbx, nax
    cln nax

    ; print
    mov nby, 1x00
    syscall nbx, nby
    
    cln nax
    cln nbx

    call exit

.exit
    mov nay, 0
    mov nby, 1x01
    syscall nay, nby
 

END
```

With print process

```nasm
START:

set n

.main:
    mov nax, "hello"+sp+"world!"
    
    call print_message, nax

    call exit

.print_message
    inp nax

    mov nbx, nax

    lose nax

    mov nby, 1x00
    syscall nbx, nby

    cln nby
    cln nbx

    take nax
    
    ret

.exit
    mov nay, 0
    mov nby, 1x01
    syscall nay, nby
 

END
```