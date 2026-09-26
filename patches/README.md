# Build patches

These patches accompany the unofficial VoltageOS enchilada device configuration.
Apply them after syncing the specified upstream revisions and before building.
Android's build system does not apply these files automatically. Preserve local
work and stop on conflicts or a different upstream base.

## Framework base and notification background

Use [VoltageOS/frameworks_base_new](https://github.com/VoltageOS/frameworks_base_new)
at `db91bd93ad97bcb60158fcc150198ac49fcf480b`. This includes the upstream
multi-audio ducking and mobile-data, Bluetooth and ringtone dialog fixes.

The existing notification patch synchronizes the background with its parent
keyguard state when initializing the background. Its original change is
`81a82daa39f2e3816e6f5c5119374dbe5a92e62d`; the patch content is unchanged.

From the Android source root, starting with the clean upstream framework base:

```sh
git -C frameworks/base am ../../device/oneplus/enchilada/patches/frameworks_base/0001-Synchronize-notification-background-keyguard-state.patch
```

Do not reapply a patch that is already present. Keep the manifest pinned to the
public upstream revision; preserve local commits or patches before syncing again.
No framework fork is required.
