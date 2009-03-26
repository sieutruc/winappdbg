#!/usr/bin/env python

# Copyright (c) 2009, Mario Vilas
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#     * Redistributions of source code must retain the above copyright notice,
#       this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice,this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the copyright holder nor the names of its
#       contributors may be used to endorse or promote products derived from
#       this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

from distutils.core import setup
from glob import glob
from os.path import join

setup(name          = 'winappdbg',
      version       = '1.0',
      description   = 'Windows application debugging engine',
      author        = 'Mario Vilas',
      author_email  = 'mvilas'+chr(64)+'gmail'+chr(0x2e)+'com',
      url           = 'U{http://sourceforge.net/projects/winappdbg/',
      packages      = ['winappdbg'],
      scripts       = glob(join('tools', '*.py')),
      requires      = ['ctypes'],
      platforms     = ['win32', 'cygwin'],
      classifiers   = [
                      'Development Status :: 5 - Production/Stable',
                      'Environment :: Console',
                      'Environment :: Win32 (MS Windows)',
                      'Intended Audience :: Developers',
                      'Natural Language :: English',
                      'Operating System :: Microsoft :: Windows',
                      'Programming Language :: Python',
                      'Topic :: Software Development :: Bug Tracking',
                      'Topic :: Software Development :: Debuggers',
                      'Topic :: Software Development :: Libraries :: Python Modules',
                      ],
     )
