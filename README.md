# JSON obfuscator

Simple JSON obfuscator tool which replaces all the strings in a file with unicode escape sequences, making it more difficult for a human reader to analyse it. Output JSON file (obfuscate.py) is valid and equivalent to the input.

# Running

Run obfuscate.py

```
'Please enter the name of input file below (w/o extension):'
```
Enter file name of JSON in question and press enter.

```
input
```

Process will begin and display affected strigs and thier new values.

```
name \u006e\u0061\u006d\u0065
...
```

Press enter to close the program.

Please check obfuscated.json and replacement mapping file.txt for tranlation.