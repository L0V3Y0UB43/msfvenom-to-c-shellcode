This python script formats the shellcode that is created by 'msfvenom -f c'.
as 'msfvenom -p windows/x64/exec CMD=calc.exe -f c' creates shellcode like this 

```
"\x4d\x72\x20\x50\x6f\x6f\x70\x79\x42\x75\x74\x68\x6f\x6c\x65\x0a"
"\x4d\x72\x20\x50\x6f\x6f\x70\x79\x42\x75\x74\x68\x6f\x6c\x65\x0a"
"\x4d\x72\x20\x50\x6f\x6f\x70\x79\x42\x75"
```
You can paste it in a file and run the python code lik 
```
python3 code.py shellcode.txt
```

The output will be
```
unsigned char rawShellcode[] = {
	0x4d, 0x72, 0x20, 0x50, 0x6f, 0x6f, 0x70, 0x79, 0x42, 0x75, 0x74, 0x68, 0x6f, 0x6c, 0x65, 0x0a,
	0x4d, 0x72, 0x20, 0x50, 0x6f, 0x6f, 0x70, 0x79, 0x42, 0x75, 0x74, 0x68, 0x6f, 0x6c, 0x65, 0x0a,
	0x4d, 0x72, 0x20, 0x50, 0x6f, 0x6f, 0x70, 0x79, 0x42, 0x75
};
```

Or you could just do this command on the bin file lol.
'calc.bin' is used for example
```
echo  "unsigned char buf[] = {"
xxd -p calc.bin | tr -d '\n' | sed 's/\(..\)/0x\1, /g' | fold -w 108 | sed 's/^/    /' | sed '$ s/, $//; $ a\};'
```
