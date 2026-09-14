# SPDX-License-Identifier: Apache-2.0

from hashlib import sha256
from pathlib import Path

ORIGINAL_SHA256 = '16ee6adb05c0d5753fa6add9ec2330a341cc3949561cc4050b22ab92e801958a'
PATCHED_SHA256 = 'ac3915b736d486980bf14d9a701f18ebaa9df36e40c8b751ebdfaafc33f6e68d'


def patch_keymaster(data: bytes) -> bytes:
    digest = sha256(data).hexdigest()
    if digest == PATCHED_SHA256:
        return data
    if digest != ORIGINAL_SHA256:
        raise ValueError(f'Unsupported Keymaster blob: {digest}')

    patched = bytearray(data)
    # Pass EVP_PKEY* to its accessor instead of reading the old type offset.
    for offset in (0x14e68, 0x14f04):
        patched[offset:offset + 4] = bytes.fromhex('e00315aa')  # mov x0, x21

    # Undefined symbol 99 is outside the GNU hash table (first symbol 121).
    # Its only callers are the two instructions above and their existing BLs.
    patched[0x6456:0x6464] = b'EVP_PKEY_id\0\0\0'
    if sha256(patched).hexdigest() != PATCHED_SHA256:
        raise ValueError('Keymaster fixup output hash mismatch')
    return bytes(patched)


def fixup_keymaster(ctx, file, file_path, **kwargs):
    path = Path(file_path)
    original = path.read_bytes()
    patched = patch_keymaster(original)
    if patched != original:
        path.write_bytes(patched)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Fix the Keymaster EVP_PKEY accessor')
    parser.add_argument('blob', type=Path)
    args = parser.parse_args()
    fixup_keymaster(None, None, args.blob)
    print(f'Keymaster SHA-256: {sha256(args.blob.read_bytes()).hexdigest()}')
