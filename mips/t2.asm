.data
    VetorDados:.space 200 #40
    VetorPadrao: .space 20 

    print1: .asciiz "Informe o numero de dados a serem inseridos no vetor"
    print2: .asciiz "Informe um dados a ser inserido no vetor"
    print3: .asciiz "Vetor de dados: "
    print4: .asciiz "Vetor de padrao: "

.text
 .globl  main           
main:


# $s0 $s1 terao respectivamente vetor de dados e vetor padrao
# $s2 $s3 terao respectivamente as quantidades do vetor de dados e do vetor padrao
# $s7 é o contador de padroes
li  $v0, 4          
la $a0, print3   #printando vetorDados
syscall


la $s0 VetorDados 
addiu $sp, $sp, -4
sw $s0 0($sp)
jal carregaVetor
lw $s2, 0($sp) #tamanho do vetor de dados
 
 
li  $v0, 4          #printando vetor padrao
la $a0, print4
syscall


la $s1 VetorPadrao
sw $a1 0($sp)
jal carregaVetor
lw $s3, 0($sp) # tamanho do vetor padrao

li $s7,0 # contador de padrões inicia em 0
li $s4,0

addiu $s6, $s4,0# tamanho do vetor padrao+ posicao do vetor de dados 

addiu $sp, -16 # abrindo um total de 5 espaços na pilha, pois -4-16=-20 e 20/4=5
sw $s0,0($sp)  #endereço vetor dados
sw $s1,4($sp) #enderelo vetor padrao
sw $s3,8($sp)# tamanho vetor padrao




enquanto:beq $s6, $s2, Fim
li $s4,0 #posiçao no vetor de dados
sw $s4,12($sp)
li $s5,0 #posiçao no vetor padrao
sw $s5,16($sp)


jal encontraPadrao



addiu $s6,$s6,1# cont ++
j enquanto




Fim: li $v0, 10 #acaba o prog
syscall


carregaVetor:  li  $v0, 4          
    la $a0, print1  
    syscall
    
    li  $v0, 5         
    syscall
    
    move $t0, $v0 # bota o numero de dados em t0
    move $t1, $sp
    #lw $t1, 0($t1)# dolar t1 contem o endereço do vetor
    li $t2, 0 #começa na posição 0 o for 
 forDoCarrega:beq  $t2, $t0, fimForDoCarrega # quando acabar o vetor sai do for
 
    addiu $t2,$t2, 1# incrementa o contador
 
    li  $v0, 4          
    la $a0, print2  
    syscall
    
    li  $v0, 5       # agora o numero inserido pelo usuario esta no v0  
    syscall
    
    sw $v0, 0($t1)
    addiu $t1,$t1, 4
    j forDoCarrega  
    
    
fimForDoCarrega: sw $t0, 0($sp)
jr $ra

# fim do carrega vetor 


encontraPadrao: 

# recebendo dados por parametro
lw $t0, 0($sp)#endereço vetor dados
lw $t1, 4($sp) #endereço vetor padrao
lw $t2, 8($sp)#tam vetor padrao
lw $t3, 12($sp)#posição vetor dados 
lw $t4, 16($sp) #posição vetor padrao


bne $t3, 0, continua # guardando o $ra da primeira iteração para poder voltar para o enquanto
# esse ifsignifica  que se nao for igual ele continua o programa, caso contrario ele salva $ra
lw $ra, -4($sp)   # salvando o endereco de $ra para poder usar nos resuldado0 e resultado1

continua:

#addiu $sp, $sp, 16 # reseta a pilha mas deixa com um espaço porque 20-4=16

	mul $t5, $t3, 4 #posicao de vetor dados
  mul $t6, $t4, 4#posicao de vetor padrao
  
  addu $t5, $t0, $t5 #atualiza posicao de vetor dados
  addu $t6, $t1, $t6 #atualiza posicao de vetor padrao
  
  lw $t5, 0($t5)	#guarda o elemento de vetor dados que esta na posicao que foi atualizada
  lw $t6, 0($t6)  #guarda o elemento de vetor padrao que esta na posica que foi atualizada
  
  bne $t5, $t6, resultado0 #faz um if(vetDados[posDados] != vetPadrao[posPadrao])
  
  #usando o $t5 para duas coisas, aqui mudamos sua funcionalidade de vetDados[posDados] para tamPadrao -1, mas não tem problema porque depois do primeiro if vetDados[posDados] ao sera usado
  addiu $t5, $t2, -1 #antes de realizar proximo if, faz (tamPadrao -1)
  
  beq $t4, $t5, resultado1 #faz outro if(posPadrao == tamPadrao -1)
  
  addiu $t3, $t3, 1 #avanca pra proxima posicao de vetor dados
  addiu $t4, $t4, 1 #avanca pra proxima posicao de vetor padrao
  
  sw $t3, 12($sp)#posição vetor dados 
  sw $t4, 16($sp) #posição vetor padrao

  
  
  jal encontraPadrao
  
  
resultado0:
	li $t7, 0 
	sw $t7, -8($sp)
  lw	$ra, -4($sp)
  j 	$ra
    
resultado1:
  li $t7, 1
	sw $t7, -8($sp)
  lw	$ra, -4($sp)
  j 	$ra
  
  