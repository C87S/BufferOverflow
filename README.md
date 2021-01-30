# BufferOverflow **Work In Progress*

Basic Steps for conducting buffer overflow

**Pre Requisites**
* [Immunity Debugger Installed](https://www.immunityinc.com/products/debugger/)
* [Mona.py](https://github.com/corelan/mona)

**Steps**
1. Open Immunity then open the target application, press `F9` to run the app
2. Use 00-crash the system to attempt to crash the application with A's.
3. Generate pattern (Can be done via Metasploit or Mona.py) when app crashes Immunity will show pattern in EIP field use 02
4. Use pattern generator to identify specific pattern position
5. Use 03 locate the EIP, As upto the EIP and replace EIP with Bs, confirm with EIP
6. Use 04 to look for bad characters, As upto EIP, the Bs, then bad chars, manually look for where they mess up, tweak the .py file to strip out bad chars but take note. *May be possible to do this with Mona, research*
7. Use Mona to search for jump function *add command*
8. Use 05 to put the jump function into the EIP, test it works with a breakpoint.
9. Use msfvenom to generate payload.
10. Creat final payload, padding, EIP, Nop Sled, payload, padding
