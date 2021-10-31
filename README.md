# MassRename

## About
MassRename is a command line tool for renaming batches of files. This removes the repetitive hassle of using your operating system's file explorer to manually rename the files.

I created the tool for my own personal use so I could quickly rename episodes of TV shows along with the subtitle files.

## How to install
Simply download the Python file and run it using a terminal - it will rename files from whatever directory the file is in.

## How to use 
Simply type "massrename.py" into the terminal and give your arguments. Make sure that massrename.py is in the directory with the files you want to rename.

Example:
```
massrename.py "showname - Episode {n}" --filetype mp4 --includes "showname ep-"
```
This command will rename every `.mp4` file that starts with `"showname ep-"` to `"showname - Episode {episode number}"`.

### Arguments
Here is a list of every argument you can use in the application. They are split into 3 lists, "filter arguments" (which filter the files effected by the massrename), "other arguments" which effects various other areas of how the application works and "name arguments" which will effect how files are named.

#### Filter arguments

Argument | Shorthand | Use | Allows multiple inputs | Notes
--- | --- | --- | --- | ---
name | N/A | The name you want to rename the files to | No | **Required**, this always comes first. See [name arguments](name_arguments) for details on how to format this argument
--filetype | -f | Filters to files that use the extentions specified | Yes | 
--includes | -i | Filters to files that include `-includes` | Yes | If your check includes spaces then put it in quotation marks 

If you want to define multiple checks (e.g. looking for files with both the `.srt` and `.mp4` extension) then add a space in between the arguments.

Example:
```
massrename --filetype srt mp4
```


#### Other arguments

Argument | Shorthand | Use | Allows multiple inputs | Notes
--- | --- | --- | --- | ---
--show-output | N/A | Shows various output messages - useful if massrename isn't filtering files how you expect it to | Takes no input

#### Name arguments
These can be used in the first "name" argument. If you don't have any of these arguments then renaming more than one file will be impossible as there will be no variation in filename, because of this massrename will automatically add a `(n)` at the end of the file (which operates in the exact same way that {n} does).

Character(s) | Use | Notes
--- | --- | ---
{n} | Incremental number (+1) | 

---

## License
Massrename uses the MIT license, see LICENSE for more details
