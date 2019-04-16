# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.

from __future__ import absolute_import, division, print_function

INCLUDES = """
#include <openssl/aegis.h>
"""

TYPES = """
"""

FUNCTIONS = """
void AEGIS_encrypt(const uint8_t *key, const uint8_t *iv,
                   const uint8_t *msg, size_t msglen,
                   const uint8_t *ad, size_t adlen,
                   uint8_t *cipher, uint8_t *tag);
                   
int AEGIS_decrypt(const uint8_t *key, const uint8_t *iv,
                  const uint8_t *cipher, size_t cipherlen,
                  const uint8_t *ad, size_t adlen,
                  const uint8_t *tag, uint8_t *msg);
"""

CUSTOMIZATIONS = """
"""
