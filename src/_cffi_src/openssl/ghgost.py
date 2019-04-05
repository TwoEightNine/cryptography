# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.

from __future__ import absolute_import, division, print_function

INCLUDES = """
#include <openssl/ghgost.h>
#include <stdint.h>
"""

TYPES = """
typedef ... GHGOST_KEY;
"""

FUNCTIONS = """
void GHGOST_encrypt(const unsigned char *, unsigned char *,
                    const GHGOST_KEY *);
void GHGOST_decrypt(const unsigned char *, unsigned char *,
                    const GHGOST_KEY *);
int GHGOST_set_encrypt_key(const unsigned char *, const int,
                           GHGOST_KEY *);
int GHGOST_set_decrypt_key(const unsigned char *, const int,
                           GHGOST_KEY *);
"""

CUSTOMIZATIONS = """
"""
