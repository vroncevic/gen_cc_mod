<img align="right" src="https://raw.githubusercontent.com/vroncevic/gen_cc_mod/dev/docs/gen_cc_mod_logo.png" width="25%">

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

![Debian Linux OS](https://raw.githubusercontent.com/vroncevic/gen_cc_mod/dev/docs/debtux.png)

Navigate to release **[page](https://github.com/vroncevic/gen_cc_mod/releases)** download and extract release archive.

To install **gen_cc_mod** type the following

```
tar xvzf gen_cc_mod-x.y.tar.gz
cd gen_cc_mod-x.y
cp -R ~/sh_tool/bin/   /root/scripts/gen_cc_mod/ver.x.y/
cp -R ~/sh_tool/conf/  /root/scripts/gen_cc_mod/ver.x.y/
cp -R ~/sh_tool/log/   /root/scripts/gen_cc_mod/ver.x.y/
```

Self generated setup script and execution
```
./gen_cc_mod_setup.sh 

[setup] installing App/Tool/Script gen_cc_mod
	Sun 05 Dec 2021 01:32:04 PM CET
[setup] copy App/Tool/Script structure
[setup] remove github editor configuration files
[setup] set App/Tool/Script permission
[setup] create symbolic link of App/Tool/Script
[setup] done

/root/scripts/gen_cc_mod/ver.2.0/
├── bin/
│   ├── center.sh
│   ├── display_logo.sh
│   └── gen_cc_mod.sh
├── conf/
│   ├── gen_cc_mod.cfg
│   ├── gen_cc_mod.logo
│   ├── gen_cc_mod_util.cfg
│   └── template/
│       ├── cc_editorconfig.template
│       ├── cc_source.template
│       └── h_header.template
└── log/
    └── gen_cc_mod.log

4 directories, 10 files
lrwxrwxrwx 1 root root 50 Dec  5 13:32 /root/bin/gen_cc_mod -> /root/scripts/gen_cc_mod/ver.2.0/bin/gen_cc_mod.sh
```

Or You can use docker to create image/container.

### Usage

```
# Create symlink for shell tool
ln -s /root/scripts/gen_cc_mod/ver.x.y/bin/gen_cc_mod.sh /root/bin/gen_cc_mod

# Setting PATH
export PATH=${PATH}:/root/bin/

# Generating module-pair (source+header file)
gen_cc_mod GTKMyOption

gen_cc_mod ver.2.0
Sun 05 Dec 2021 01:33:41 PM CET

[check_root] Check permission for current session? [ok]
[check_root] Done

    	                                                     
                                                                                      
                                                                                  ██  
                                                                                 ░██  
    █████   █████  ███████         █████   █████        ██████████   ██████      ░██  
   ██░░░██ ██░░░██░░██░░░██       ██░░░██ ██░░░██      ░░██░░██░░██ ██░░░░██  ██████  
  ░██  ░██░███████ ░██  ░██      ░██  ░░ ░██  ░░        ░██ ░██ ░██░██   ░██ ██░░░██  
  ░░██████░██░░░░  ░██  ░██      ░██   ██░██   ██       ░██ ░██ ░██░██   ░██░██  ░██  
   ░░░░░██░░██████ ███  ░██ █████░░█████ ░░█████  █████ ███ ░██ ░██░░██████ ░░██████  
    █████  ░░░░░░ ░░░   ░░ ░░░░░  ░░░░░   ░░░░░  ░░░░░ ░░░  ░░  ░░  ░░░░░░   ░░░░░░   
   ░░░░░                                                                               
    	                                                     
    		Info   github.io/gen_cc_mod ver.2.0 
    		Issue  github.io/issue
    		Author vroncevic.github.io

[gen_cc_mod] Loading basic and util configuration!
100% [================================================]

[load_conf] Loading App/Tool/Script configuration!
[check_cfg] Checking configuration file [/root/scripts/gen_cc_mod/ver.2.0/conf/gen_cc_mod.cfg] [ok]
[check_cfg] Done

[load_conf] Done

[load_util_conf] Load module configuration!
[check_cfg] Checking configuration file [/root/scripts/gen_cc_mod/ver.2.0/conf/gen_cc_mod_util.cfg] [ok]
[check_cfg] Done

[load_util_conf] Done

[gen_cc_mod] Generating file [GTKMyOption.cc]
[gen_cc_mod] Generate file [GTKMyOption.h]
[gen_cc_mod] Generating file [.editorconfig]
[gen_cc_mod] Set owner!
[gen_cc_mod] Set permission!
[logging] Checking directory [/root/scripts/gen_cc_mod/ver.2.0/log/]? [ok]
[logging] Write info log!
[logging] Done

[gen_cc_mod] Done
[check_tool] Checking tool [/usr/bin/tree]? [ok]
[check_tool] Done

.
├── GTKMyOption.cc
└── GTKMyOption.h

```

### Dependencies

**gen_cc_mod** requires next modules and libraries
* sh_util [https://github.com/vroncevic/sh_util](https://github.com/vroncevic/sh_util)

### Shell tool structure

**gen_cc_mod** is based on MOP.

Shell tool structure
```
sh_tool/
├── bin/
│   ├── center.sh
│   ├── display_logo.sh
│   └── gen_cc_mod.sh
├── conf/
│   ├── gen_cc_mod.cfg
│   ├── gen_cc_mod.logo
│   ├── gen_cc_mod_util.cfg
│   └── template/
│       ├── cc_editorconfig.template
│       ├── cc_source.template
│       └── h_header.template
└── log/
    └── gen_cc_mod.log
```

### Docs

[![Documentation Status](https://readthedocs.org/projects/gen_cc_mod/badge/?version=latest)](https://gen-cc-mod.readthedocs.io/projects/gen_cc_mod/en/latest/?badge=latest)

More documentation and info at
* [https://gen_cc_mod.readthedocs.io/en/latest/](https://gen-cc-mod.readthedocs.io/en/latest/)
* [https://www.gnu.org/software/bash/manual/](https://www.gnu.org/software/bash/manual/)

### Copyright and licence

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright (C) 2017 - 2024 by [vroncevic.github.io/gen_cc_mod](https://vroncevic.github.io/gen_cc_mod)

**gen_cc_mod** is free software; you can redistribute it and/or modify
it under the same terms as Bash itself, either Bash version 4.2.47 or,
at your option, any later version of Bash 4 you may have available.

Lets help and support FSF.

[![Free Software Foundation](https://raw.githubusercontent.com/vroncevic/gen_cc_mod/dev/docs/fsf-logo_1.png)](https://my.fsf.org/)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://my.fsf.org/donate/)
