#mode' Parameter Attributes
#Character	                    What it's used for?
##  'r'	        Open for reading (default). If the file doesn't exist, FileNotFoundError will raise.
##  'a'	        Open for writing. It will append to the end of the file if it already exists. If there is no file, it will create it.
##  'w'	        Open for writing. It will be overwritten if the file already exists. If there is no file, it will create it.
##  'x'	        Open for exclusive creation, it will fail if the file already exists.
##  'b'	        Open in binary mode.
##  't'	        Open as a text file (default).
##  '+'	        Open for updating (reading and writing).


# open() function executes opening the file for reading ('r') as a text ('t'). In other words, 
# it defaults to 'r' or 'rt' which means open for reading in text mode.


# Another important point we should cover about mode is that you can choose the format in which you want to open the file as text ('t') or binary ('b'). According to the official related Python documentation, files opened in 'binary' mode return contents as bytes objects without any decoding. In 'text' mode, the contents of the file are returned as str, the bytes having been first decoded using a platform-dependent encoding or using the specified encoding if given.

#In this case, if you want to open a binary file for writing you should set the mode as 'wb'. On the other hand, if you want to work with a text file you don't need to specify 't' since the default value of mode is already set as 't'. So, when opening and writing a text file it's enough to set the mode as 'w'.

#Finally, let us examine the differences between the use of 'w' and 'a'. Both options are used to modify the file or to write new data to the file. However, when you use 'a', the data you want to write will be added at the bottom of the file and combined with existing content, whereas using 'w' will delete the existing content and add new content each time. 