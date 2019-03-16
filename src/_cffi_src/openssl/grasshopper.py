# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.

from __future__ import absolute_import, division, print_function

INCLUDES = """
#include <openssl/grasshopper.h>
"""

TYPES = """
struct gh_key_st {
    ...;
};
typedef struct gh_key_st GH_KEY;
"""

FUNCTIONS = """
void GH_encrypt(const unsigned char *in, unsigned char *out,
                 const GH_KEY *key);
void GH_decrypt(const unsigned char *in, unsigned char *out,
                 const GH_KEY *key);
"""

CUSTOMIZATIONS = """
"""
