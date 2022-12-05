
section .text
    default rel
    global main
    extern printf

main:
OUTER_LOOP:
    mov     eax, 0
    mov dword [iter_counter], 0
INNER_LOOP:
    

    ; sum += 2 * b 
    mov eax, [b]
    mov ebx, 2
    mul ebx
    add [sum], eax 
    
    ; sum += c
    mov eax, [c]
    add [sum], eax 

    ; sum -= i 
    mov eax, [iter_counter]
    sub [sum], eax 

    inc dword [iter_counter]
    mov eax, [iter_counter]
    cmp eax, [iter_total]
    jne INNER_LOOP
    
    
    
    
    dec byte [loop_count]
    cmp byte [loop_count], 0
    jne OUTER_LOOP
    
    ; Call printf
    ; push rbp 
    ; mov	rdi, fmt
    ; mov	rsi, sum
    ; mov	rax, 0
    ; call printf wrt ..plt
    ; pop	rbp		
    ; Call printf end

    mov     ebx, 0
    mov     eax, 1
    int     0x80
    
section .data
    b db 3
    c db 4
    loop_count db 2
    iter_total dd 100000000
    iter_counter dd 0
    sum dd 0
    fmt:    db "%llu", 10, 0
segment .bss

