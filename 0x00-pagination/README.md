# 0x00. Pagination

| `Back-end` |

![meme1](./images/meme1.png)
![meme2](./images/meme2.png)
![meme3](./images/meme3.png)

## Resources

### Read or Watch

+ [REST API Design: Pagination](https://intranet.alxswe.com/rltoken/7Kdzi9CH1LdSfNQ4RaJUQw)

+ [HATEOAS](https://intranet.alxswe.com/rltoken/tfzcEbTSdMYSYxsspJH_oA)

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

+ How to paginate a dataset with simple page and page_size parameters
+ How to paginate a dataset with hypermedia metadata
+ How to paginate in a deletion-resilient manner

## Requirements

+ All your files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
+ All your files should end with a new line
+ The first line of all your files should be exactly `#!/usr/bin/env python3`
+ A `README.md` file, at the root of the folder of the project, is mandatory
+ Your code should use the `pycodestyle` style (version 2.5.*)
+ The length of your files will be tested using `wc`
+ All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
+ All your functions should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`
+ A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
+ All your functions and coroutines must be type-annotated.

## Setup: `Popular_Baby_Names.csv`

[use this data](https://intranet.alxswe.com/rltoken/NBLY6mdKDBR9zWvNADwjjg) file for your project

## Tasks

### 0. Simple helper function

Write a function named `index_range` that takes two integer arguments page and page_size.

The function should return a tuple of size two containing a start index and an end index corresponding to the range of indexes to return in a list for those particular pagination parameters.

Page numbers are 1-indexed, i.e. the first page is page 1.