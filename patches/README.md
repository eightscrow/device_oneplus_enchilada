# Build patches

Apply from the Android source root after syncing these revisions:

| Project | Source | Revision |
| --- | --- | --- |
| frameworks/base | VoltageOS/frameworks_base_new | db91bd93ad97bcb60158fcc150198ac49fcf480b |

```sh
git -C frameworks/base am ../../device/oneplus/enchilada/patches/frameworks_base/0001-Synchronize-notification-background-keyguard-state.patch
```

Do not reapply patches already present in the source tree.
