# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.

from __future__ import absolute_import, division, print_function

INCLUDES = """
#include <openssl/ghgost.h>
"""

TYPES = """
typedef ... GHGOST_KEY;
"""

FUNCTIONS = """
void GHGOST_encrypt(const unsigned char *in, unsigned char *out,
                    const GHGOST_KEY *key);

void GHGOST_decrypt(const unsigned char *in, unsigned char *out,
                    const GHGOST_KEY *key);

void GHGOST_set_key(const unsigned char *userKey, const int bits,
                           GHGOST_KEY *key);

void GHGOST_get_mac_key(const GHGOST_KEY *key, unsigned char *mac_key);
"""

CUSTOMIZATIONS = """
"""
