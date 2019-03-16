# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.

from __future__ import absolute_import, division, print_function

INCLUDES = """
#include <openssl/grasshopper.h>
"""

TYPES = """
typedef ... GH_KEY;
"""

FUNCTIONS = """
void GH_encrypt(const unsigned char *, unsigned char *,
                 const GH_KEY *);
void GH_decrypt(const unsigned char *, unsigned char *,
                 const GH_KEY *);
"""

CUSTOMIZATIONS = """
"""
