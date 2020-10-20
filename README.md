# Generate C++ Module

**gen_cc_mod** is shell tool for generating C++ modules.

Developed in **[bash](https://en.wikipedia.org/wiki/Bash_(Unix_shell))** code: **100%**.

[![gen_cc_mod shell checker](https://github.com/vroncevic/gen_cc_mod/workflows/gen_cc_mod%20shell%20checker/badge.svg)](https://github.com/vroncevic/gen_cc_mod/actions?query=workflow%3A%22gen_cc_mod+shell+checker%22)

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

[![GitHub issues open](https://img.shields.io/github/issues/vroncevic/gen_cc_mod.svg)](https://github.com/vroncevic/gen_cc_mod/issues) [![GitHub contributors](https://img.shields.io/github/contributors/vroncevic/gen_cc_mod.svg)](https://github.com/vroncevic/gen_cc_mod/graphs/contributors)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Shell tool structure](#shell-tool-structure)
- [Docs](#docs)
- [Copyright and licence](#copyright-and-licence)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

### Installation

Navigate to release **[page](https://github.com/vroncevic/gen_cc_mod/releases)** download and extract release archive.

To install **gen_cc_mod** type the following:

```
tar xvzf gen_cc_mod-x.y.z.tar.gz
cd gen_cc_mod-x.y.z
cp -R ~/sh_tool/bin/   /root/scripts/gen_cc_mod/ver.1.0/
cp -R ~/sh_tool/conf/  /root/scripts/gen_cc_mod/ver.1.0/
cp -R ~/sh_tool/log/   /root/scripts/gen_cc_mod/ver.1.0/
```

![alt tag](https://raw.githubusercontent.com/vroncevic/gen_cc_mod/dev/docs/setup_tree.png)

Or You can use docker to create image/container.

[![gen_cc_mod docker checker](https://github.com/vroncevic/gen_cc_mod/workflows/gen_cc_mod%20docker%20checker/badge.svg)](https://github.com/vroncevic/gen_cc_mod/actions?query=workflow%3A%22gen_cc_mod+docker+checker%22)

### Usage

```
# Create symlink for shell tool
ln -s /root/scripts/gen_cc_mod/ver.1.0/bin/gen_cc_mod.sh /root/bin/gen_cc_mod

# Setting PATH
export PATH=${PATH}:/root/bin/

# Generating module-pair (source+header file)
gen_cc_mod GTKMyOption
```

### Dependencies

**gen_cc_mod** requires next modules and libraries:
* sh_util [https://github.com/vroncevic/sh_util](https://github.com/vroncevic/sh_util)

### Shell tool structure

**gen_cc_mod** is based on MOP.

Code structure:
```
.
├── bin/
│   └── gen_cc_mod.sh
├── conf/
│   ├── gen_cc_mod.cfg
│   ├── gen_cc_mod_util.cfg
│   └── template/
│       ├── cc_editorconfig.template
│       ├── cc_source.template
│       └── h_header.template
└── log/
    └── gen_cc_mod.log
```

### Docs

[![Documentation Status](https://readthedocs.org/projects/gen_cc_mod/badge/?version=latest)](https://gen_cc_mod.readthedocs.io/projects/gen_cc_mod/en/latest/?badge=latest)

More documentation and info at:
* [https://gen_cc_mod.readthedocs.io/en/latest/](https://gen_cc_mod.readthedocs.io/en/latest/)
* [https://www.gnu.org/software/bash/manual/](https://www.gnu.org/software/bash/manual/)

### Copyright and licence

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright (C) 2017 by [vroncevic.github.io/gen_cc_mod](https://vroncevic.github.io/gen_cc_mod)

**gen_cc_mod** is free software; you can redistribute it and/or modify
it under the same terms as Bash itself, either Bash version 4.2.47 or,
at your option, any later version of Bash 4 you may have available.

Lets help and support FSF.

[![Free Software Foundation](https://raw.githubusercontent.com/vroncevic/gen_cc_mod/dev/docs/fsf-logo_1.png)](https://my.fsf.org/)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://my.fsf.org/donate/)
