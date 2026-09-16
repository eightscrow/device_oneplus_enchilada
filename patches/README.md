# Framework patch

This unofficial enchilada build applies one local SystemUI change on top of
[VoltageOS/frameworks_base_new](https://github.com/VoltageOS/frameworks_base_new).
It synchronizes the notification background with its parent keyguard state when
initializing the background. The patch is not applied automatically by Android's
build system; apply it after syncing sources and before building.

- Upstream base: `660295868d60b2b7434db870cfe74f6e4df77086`
- Original change: `81a82daa39f2e3816e6f5c5119374dbe5a92e62d`
- Patched Git tree: `b64596c074753cddfceb78224c373c5519d8762f`

From the root of the Android source checkout, with a clean framework worktree
at the specified base:

```sh
git -C frameworks/base am ../../device/oneplus/enchilada/patches/frameworks_base/0001-Synchronize-notification-background-keyguard-state.patch
```

Verify `git -C frameworks/base rev-parse 'HEAD^{tree}'` against the patched tree
above. The resulting commit ID can differ because committer metadata differs.
Skip application only if the worktree is clean and already contains this exact
patch on the specified base. For a different upstream revision, review and rebase
the patch before building; do not force it through a conflict.

When syncing again, preserve local work. A checkout already containing this patch
must be returned to the pinned upstream base before reapplying it. No framework
fork is required; keep the source manifest pinned to the upstream base above.
